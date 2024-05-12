# Welcome to GroupIT repository :)


## 3 in 1 code with clasifier:

### INPUT:
    - images folder path
    - masks foler path
    - path for the output file .csv with results of all 3 featues and the probability of a lesion to be melanoma
### OUTPUT:
    - .csv with results of all 3 featues and the probability of a lesion to be melanoma  

#### Output understanding:
##### image_path     
##### color_score   
              ( 1 - relatively dull or monochromatic,  
                2 - some color variation, but it may lack intensity or diversity,   
                3 - significant color variation with vibrant and diverse hues,   
                4 - intense and varied colors, resembling a rainbow )  
                 
##### symmetry_score 
               ( 1 - none symmetry      
                 2 - low symmetry        
                 3 - moderate symmetry       
                 4 - perfect symmetry )         
##### blue_white_score 
                 ( 0 - blue-white veil not detected,
                   1 - blue-white veil detected)  
  
##### probability_0 
    [0;1] confidance that the lesion belongs to class 0 (non melanoma)  
##### probability_1  
    [0;1] confidance that the lesion belongs to class 1 (melanoma)  
  
Example, if probability_0 is 0.7 and probability_1 is 0.3 for a particular image-mask pair, it means that the classifier is 70% confident that the pair belongs to class 0 and 30% confident that it belongs to class 1.
    
    
        
The classifier is: "trained_random_forest_classifier.pkl" on the main page of the repository.
Please input the paths with " / " not " \ "   
  
    
#### example of inputs:  
     - image_folder = "C:/Users/cieci/OneDrive/Dokumenty/GitHub/G/images_orginal"  
     - mask_folder = "C:/Users/cieci/OneDrive/Dokumenty/GitHub/G/masks_orginal"  
     - output_csv = "C:/Users/cieci/OneDrive/Dokumenty/GitHub/G/results.csv"  

  
output:
- csv file with scores of 3 features, and probabilites of a melanoma



### Tour through the repository:
- report.pdf
- 
### folders:

- assymetry
    - single code for assymetry test (Jupyter Source File (.ipynb)), with precise description of every step.
    - comparison_assymetry.csv ran over group_G dataset, code results compared with 
      human opinion.
    - additional folder with resized_masks and cropped_and_rotated_masks that helped us
      during the process of running the assymetry code. (checking if the minimum bounding
      box is looking good)
  
  
- blue-white veil 
    - single code for blue-white veil test (Jupyter Source File (.ipynb)), with precise description of every step.
    - comparison_blue_white_veil.csv ran over group_G dataset, code results compared with 
      human opinion.
    - additional folder "blue_white_veil_internet" with additional dataset (melanoma that
      have blue white veils detected by doctors) to check if the code is detecting
      correctly downloaded from: 
       https://dermoscopedia.org/02-Blue_white_structures
       (dermoscopedia)
       https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3160648/ 
       (National Institutes of Health)
       https://www.researchgate.net/figure/a-c-Melanoma-images-with-Blue-white-Veil-b-veil-mask-by-Alg-1-The-red-areas-are_fig1_260127898
       (ResearchGate)
      with it's results.
      
- color
    - single code for color test (Jupyter Source File (.ipynb)), with precise description of every step.
    - comparison_color.csv ran over group_G dataset, code results compared with 
      human opinion.
      
- graphs (graphs used in report)

- images_oginal & masks_orginal (orginal images and masks for group G provided on the
  beginig of this cours)
    
- midway (file containing files uploaded for the midway of the project)

- result_for_other_groups_images (code 3_in_1_code_output) ran over other groups images,
  and masks giving us a slightly bigger data set to work on.

 

claifiers we concidered:
- SVC
- KNN
- decission tree
- random forest 
