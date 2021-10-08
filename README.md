# Recognize A-Z Handwriting
![image](https://user-images.githubusercontent.com/87701461/136596606-f5997149-6f1e-40d1-93af-4e4795b41c35.png)
![image](https://user-images.githubusercontent.com/87701461/136596622-222573fa-6d66-4187-bd03-00bb7e4c00b1.png)


## Introduction

As a final course project, so I chose a project related to neural networks as it is an area in great development.
This project consisted in, recognize A-Z handwriting. Based on dataset, the machine was trainned with models LGBM and CNN.
The main goal is identify the best model, and adjust to work in all cases.

## Steps
1. The chosen database was found on Kaggle: https://www.kaggle.com/sachinpatel21/az-handwritten-alphabets-in-csv-format?select=A_Z+Handwritten+Data.csv
2. The data was previewed. For that, Python was used.
3. Then, trained the models LGBM and CNN and checked the auc score for train and test. 
4. The best model was CNN.
5. it was necessary to treat the preview images for the model to be able to make the prediction.

## Conclusion

-CNN model is better than LGBM for image analysis
-LGBM sees each pixel individually
-CNN analyzes set of pixels
-Image handling is very important for the CNN model to work correctly, such as image color, position and rotation.
-CNN model is widely used in image and video analysis, and is in great development.

## Future projects
The next step would be to identify handwiring words.
