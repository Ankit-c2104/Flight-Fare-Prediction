# Flight-Fare-Prediction

The purpose of this project is to learn and apply different feature engineering techniques on the data, visualize, analyze and make conclusion based on the visualization and also to learn deployment using Heroku. another aim was to leart doing front-end using Streamlit.



1.Dropped Null values

2.Combined all the same airlines

3.Dropping 'Route' and 'Additional info' columns

4.Our model is not capable of understanding columns like Date_of_Journey(object), 
  so we will have to make seperate columns for date, month and year

5.Laebl Encoding on Total_Stops
- before label_encoding - 'non-stop', '2 stops', '1 stop', '3 stops', '4 stops'
- after label_encoding - 4, 1, 0, 2, 3

6.Extracting Dep_Hour and Dep_min from Dep_Time using pd.datetime as Dep_Time is of 
  object datatype and cannot be understand by the model

7.extracting Arrival_Hour and Arrival_min from Dep_Time using pd.datetime as Dep_Time is of 
object datatype and cannot be understand by the model

8. Handling the Duration column

9. Handling the categorical columns by performing OneHotEncoding

10. Doing prediction using RandomForestClassifier nd XGBclassifier

11. Performing HyperParameter Tunning on these two models

12. The final accuracy was improved by 5% using HyperParameter Tunning and XGBclassifier cam out as the winner

