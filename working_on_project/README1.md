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

### moreover:
- 3_in_1_code_output_csv (Jupyter Source File (.ipynb)) - single code that uses color_test, assymetry_test and blue_white_veil_test, to output the results for this 3 features,
  in a csv file.
  
- classifier_and_probability (Jupyter Source File (.ipynb)) - code, where we compared classifier: random forest,  KNN, decision tree, their learning curves, confusion matrices and probabilities.

- for_classifier (.csv) sheet with 568 images, and their 3 features scores, on which our classifier was trained on.
 
- trained_random_forest_classifier.pkl  - trained classifier 

 
