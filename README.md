# Welcome to GroupIT repository :)


## 3 in 1 code, with trained clasifier (either .py or .ipynb in working_on_project folder):
description how to use the code and how to interprete the scores:

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
     - image_folder = "C:/Users/cieci/OneDrive/Dokumenty/GitHub/G/working_on_project/images_orginal"  
     - mask_folder = "C:/Users/cieci/OneDrive/Dokumenty/GitHub/G/working_on_project/masks_orginal"  
     - output_csv = "C:/Users/cieci/OneDrive/Dokumenty/GitHub/G/results.csv"  

  
output:
- csv file with scores of 3 features, and probabilites of a melanoma

 ### trained_random_forest_classifier.pkl  - trained classifier 
 ### report.pdf 
