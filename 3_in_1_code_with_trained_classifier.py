from PIL import Image
import cv2
import numpy as np
import csv
import os
import joblib  


def calculate_color_score(image_path, mask_path):
   
    image = Image.open(image_path)
    mask = Image.open(mask_path).convert('L')

    # PIL image to numpy array
    rgb_img = np.array(image)
    mask = np.array(mask)

    # find coordinates of the lesion in the mask
    lesion_coords = np.where(mask != 0)
    min_x = min(lesion_coords[0])
    max_x = max(lesion_coords[0])
    min_y = min(lesion_coords[1])
    max_y = max(lesion_coords[1])
    cropped_lesion = rgb_img[min_x:max_x, min_y:max_y]

    # variance of colors within the lesion
    color_variance = np.var(cropped_lesion, axis=(0, 1))

    # colorfulness score as the sum of variances across all channels
    colorfulness_score = np.sum(color_variance)

    # colorfulness score
    if colorfulness_score > 10000:
        color_score = 4
    elif colorfulness_score > 5000:
        color_score = 3
    elif colorfulness_score > 1000:
        color_score = 2
    else:
        color_score = 1

    return color_score


def calculate_symmetry_score(mask_image):
    def double_black_background(input_image):
        # image to grayscale (if it's not already)
        if len(input_image.shape) > 2:
            input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

        
        height, width = input_image.shape[:2]

        # create a new image with double black background
        new_img = np.zeros((height * 2, width * 2), dtype=np.uint8)

        # put the original image in the center of the new image (so during rotating the lesion wont be outside the image)
        offset_x = (width // 2)
        offset_y = (height // 2)
        new_img[offset_y:offset_y+height, offset_x:offset_x+width] = input_image

        return new_img

    def find_longest_diameter(mask_image):
        # find the longest diameter of the lesion in the mask
        contours, _ = cv2.findContours(mask_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contour = max(contours, key=cv2.contourArea)
        rect = cv2.minAreaRect(contour)
        return rect



    def rotate_image(image, angle):
        # dimensions of the image
        h, w = image.shape[:2]

        # rotation matrix
        rotation_matrix = cv2.getRotationMatrix2D((w/2, h/2), angle, 1)

        # rotation
        rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

        return rotated_image

    def crop_to_sides(mask_image, rect):
        # angle of rotation 
        angle = rect[2]
        
        if angle > 90:
            angle -= 180

        # rotate 
        rotated_mask = rotate_image(mask_image, angle)

        # find contours of the rotated lesion
        contours, _ = cv2.findContours(rotated_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # bounding of the rotated lesion
        x, y, w, h = cv2.boundingRect(contours[0])

        # crop the rotated mask image (minimum bounding box)
        cropped_mask = rotated_mask[y:y+h, x:x+w]

        return cropped_mask


    def calculate_pixel_differences(mask_image):

        # number of pixels 
        total_pixels = mask_image.size

        # get center of the mask
        center_x = mask_image.shape[1] // 2
        center_y = mask_image.shape[0] // 2

        # split into left and right halves
        left_half = mask_image[:, :center_x]
        right_half = mask_image[:, center_x:]

        # pixel count differences on each half vertically
        left_pixel_count_vertical = cv2.countNonZero(left_half)
        right_pixel_count_vertical = cv2.countNonZero(right_half)
        vertical_difference = abs(left_pixel_count_vertical - right_pixel_count_vertical)

        # split into top and bottom halves
        top_half = mask_image[:center_y, :]
        bottom_half = mask_image[center_y:, :]

        # pixel count differences on each half horizontally
        top_pixel_count_horizontal = cv2.countNonZero(top_half)
        bottom_pixel_count_horizontal = cv2.countNonZero(bottom_half)
        horizontal_difference = abs(top_pixel_count_horizontal - bottom_pixel_count_horizontal)

        # calculate the fraction of similarity vertically
        vertical_similarity = 1 - (vertical_difference / total_pixels)

        # calculate the fraction of similarity horizontally
        horizontal_similarity = 1 - (horizontal_difference / total_pixels)

        return vertical_similarity, horizontal_similarity

    def calculate_similarity_score(vertical_similarity, horizontal_similarity):
        if vertical_similarity > 0.95 and horizontal_similarity > 0.95:
            return 4
        elif vertical_similarity > 0.91 and horizontal_similarity > 0.91:
            return 3
        elif vertical_similarity > 0.8 and horizontal_similarity > 0.8:
            return 2
        else:
            return 1

    
    masked_image = double_black_background(mask_image)
    longest_diameter = find_longest_diameter(masked_image)
    cropped_mask = crop_to_sides(masked_image, longest_diameter)
    vertical_similarity, horizontal_similarity = calculate_pixel_differences(cropped_mask)
    similarity_score = calculate_similarity_score(vertical_similarity, horizontal_similarity)
    return similarity_score


def calculate_blue_white_score(image_path, mask_path):

    # load the image and mask
    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

    # resize the mask to match the dimensions of the image
    if image.shape[:2] != mask.shape[:2]:
        print("Image and mask dimensions do not match. Resizing mask...")
        mask = cv2.resize(mask, (image.shape[1], image.shape[0]))

    # image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # range for blue colors in HSV
    lower_blue = np.array([100, 50, 50])  
    upper_blue = np.array([140, 255, 255])  

    # range for detecting white or very light colors
    lower_white = np.array([0, 0, 200])  
    upper_white = np.array([180, 25, 255])  

    # Create a mask for blue and white colors
    blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
    white_mask = cv2.inRange(hsv_image, lower_white, upper_white)
    
    # if there is no blue detected, return 0 (problem with white-dry skin on the photos)
    if cv2.countNonZero(blue_mask)==0:
        return 0
    else:
        # combine the blue and white masks
        combined_color_mask = cv2.bitwise_or(blue_mask, white_mask)

        # combine the color mask with the original lesion mask
        combined_mask = cv2.bitwise_and(mask, mask, mask=combined_color_mask)

        # area of blue-white veil
        blue_white_area = cv2.countNonZero(combined_mask)

        # area of the lesion (non-zero pixels in the mask)
        lesion_area = cv2.countNonZero(mask)

        # ratio of blue-white veil area to lesion area
        ratio = blue_white_area / lesion_area

        if ratio > 0.1:
            return 1
        else:
            return 0


def calculate_probabilities(features, classifier):
    probabilities = classifier.predict_proba([features])
    return probabilities[0]


def calculate_features(image_path, mask_path):
    
    color_score = calculate_color_score(image_path, mask_path)

    
    mask_image = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

    
    symmetry_score = calculate_symmetry_score(mask_image)

    
    blue_white_score = calculate_blue_white_score(image_path, mask_path)

    return color_score, symmetry_score, blue_white_score


def process_images(image_folder, mask_folder, output_csv, classifier):
    results = []

    # iterate over files in the image folder
    for image_filename in os.listdir(image_folder):
        if image_filename.endswith(".png"):  # Check if PNG image
            image_path = os.path.join(image_folder, image_filename)
            mask_filename = image_filename.split('.')[0] + '_mask.png' 
            mask_path = os.path.join(mask_folder, mask_filename)

            try:
                print(f"Processing image: {image_path}, mask: {mask_path}")

                # calculate features
                features = calculate_features(image_path, mask_path)

                # calculate probabilities
                probabilities = calculate_probabilities(features, classifier)

                results.append({
                    'image_path': image_filename,
                    'color_score': features[0],
                    'symmetry_score': features[1],
                    'blue_white_score': features[2],
                    'probability_0': probabilities[0],  # Probability for class 0
                    'probability_1': probabilities[1]   # Probability for class 1
                })
            except FileNotFoundError:
                print(f"File not found: {image_filename}. Skipping...")

    # output results to CSV
    write_results_to_csv(results, output_csv)


def write_results_to_csv(results, output_csv):
    fieldnames = ['image_path', 'color_score', 'symmetry_score', 'blue_white_score', 'probability_0', 'probability_1']

    with open(output_csv, mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)


if __name__ == "__main__":
    # load the trained classifier
    classifier = joblib.load("trained_random_forest_classifier.pkl")

    image_folder = input("Enter the folder containing images: ")
    mask_folder = input("Enter the folder containing masks: ")
    output_csv = input("Enter the path for the output CSV file: ")

    # process images
    process_images(image_folder, mask_folder, output_csv, classifier)
    print("done:)")