import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

#To read data from file and choose the selected features into dependant variables and performance rating into independant variable
def read_file():
    file = r'EP.xls'
    data= pd.read_excel(file)
    final_cols = ['EmpEnvironmentSatisfaction','EmpLastSalaryHikePercent','EmpWorkLifeBalance',
              'ExperienceYearsInCurrentRole','YearsSinceLastPromotion','YearsWithCurrManager',
              'ExperienceYearsAtThisCompany','EmpDepartment','OverTime','EmpJobRole']
    X = data[final_cols]
    Y = data.loc[:,['PerformanceRating']]
    return X,Y

#One hot encode the categorical data
def prep_input(df):
    #One hot encode categorical columns
    X = pd.get_dummies(df, ['EmpDepartment','OverTime','EmpJobRole'])
    return X

#Map the number input from html to the actual data
def map_cat_col(data):
    labelEncoder = LabelEncoder()
    category_col = ['EmpDepartment','OverTime','EmpJobRole']
    mapping_dict = {}
    for col in category_col:
        data[col] = labelEncoder.fit_transform(data[col])
        le_name_mapping = dict(zip(labelEncoder.classes_,labelEncoder.transform(labelEncoder.classes_)))
        mapping_dict[col] = le_name_mapping
    return mapping_dict

#Find the actual over time data from the map
def get_key_OverTime(val,mapping_dict):
    for key, value in mapping_dict['OverTime'].items():
         if val == value:
                return key
     
#Find the actual employee department data from the map       
def get_key_EmpDepartment(val,mapping_dict):
    for key, value in mapping_dict['EmpDepartment'].items():
         if val == value:
                return key
   
#Find the actual employee job role data from the map         
def get_key_EmpJobRole(val,mapping_dict):
    for key, value in mapping_dict['EmpJobRole'].items():
         if val == value:
                return key

                