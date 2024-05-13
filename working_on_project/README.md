# Tour through the folder:

## folders:

## Assymetry
- single code for assymetry test (Jupyter Source File (.ipynb)), with precise description of every step.
      
##### INPUT: mask path 
##### OUTPUT: asymmetry score

##### Destription:

    1. Double the black-background so the roation won't cut the mask
    2. Find the longest diameter
    3. Rotate over the longest diameter
    4. Crop the image to the minimum bounding box
    5. Calculate pixel difference, (folding vertically, and horizontally)
    6. Output score

###### score description:
    range[1-4]   
    1 - none symmetry     
    2 - low symmetry      
    3 - moderate symmetry     
    4 - perfect symmetry       

- comparison_assymetry.csv ran over group_G dataset, code results compared with 
      human opinion.
- additional folder with resized_masks and cropped_and_rotated_masks that helped us
      during the process of running the assymetry code. (checking if the minimum bounding
      box is looking good)
  
  
## Blue-white veil 
- single code for blue-white veil test (Jupyter Source File (.ipynb)), with precise description of every step.

##### INPUT: image path, mask path
##### OUTPUT: yes(1)/ no(0) if the blue-white veil is detected

##### Description:
    1. Load images
    2. convert image to HSV color space
    3. create mask for blue and combine with orginal mask
    4. return ratio of blue-white0veil part/ full size of image range [0;1]
    5. if ratio >0.1 : 1, else : 0


##### WARNING: do not uplad masks that have blue pen marks around lesion, then the result is not reliable

- comparison_blue_white_veil.csv ran over group_G dataset, code results compared with 
      human opinion.
- additional folder "blue_white_veil_internet" with additional dataset (melanoma that
      have blue white veils detected by doctors) to check if the code is detecting
      correctly downloaded from: https://dermoscopedia.org/02-Blue_white_structures(dermoscopedia)
       https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3160648/ (National Institutes of Health)
       https://www.researchgate.net/figure/a-c-Melanoma-images-with-Blue-white-Veil-b-veil-mask-by-Alg-1-The-red-areas-are_fig1_260127898(ResearchGate)
      with it's results.
      
## Color
- single code for color test (Jupyter Source File (.ipynb)), with precise description of every step.
  
##### INPUT: image path and mask path
##### OUTPUT: color score

##### Destription:
     1. Load image and mask using PIL
     2. Convert imag and mask to numpy arrays 
     3. Get coordinates, crop
     4. Calculate the variance of colors within the lesion
     5. Compute the colorfulness score as the sum of variances across all color channels.
     6. Output
    
- comparison_color.csv ran over group_G dataset, code results compared with 
      human opinion.
  
 ##### Moreover:     
- graphs (graphs used in report)

- images_oginal & masks_orginal (orginal images and masks for group G provided on the
  beginig of this cours)
    
- midway (file containing files uploaded for the midway of the project)


- 3_in_1_code_output_csv (Jupyter Source File (.ipynb)) - single code that uses color_test, assymetry_test and blue_white_veil_test, to output the results for this 3 features,
  in a csv file.
  
- classifier_and_probability (Jupyter Source File (.ipynb)) - code, where we compared classifier: random forest,  KNN, decision tree, their learning curves, confusion matrices and probabilities.

- for_classifier (.csv) sheet with 568 images, and their 3 features scores, on which our classifier was trained on.
 


 
