# Employee-performance-analysis-INX-Future-inc-

## End to end ML project with Flask deployment
This machine learning project aims to analyse and find the factors related to an employee's performance and attrition. It then predicts the performance rating and the user input is taken from the webpage using flask API

### Problem statement 
INX Future Inc, is one of the leading data analytics and automation solutions provider with over 15 years of global business presence. In recent years, the employee performance indexes are not healthy and this has become a growing concern among the top management. The CEO Mr. Brain, decided to initiate a data science project, which analyzes the current employee data and find the core underlying causes of the performance issues. He also expects a clear indicators of non-performing employees, so that any penalization of non-performing employee, if required, may not significantly affect other employee morals.
The following insights are expected from this project:

- Department wise performances
- Top 3 Important Factors effecting employee performance.
- A trained model which can predict the employee performance based on factors as inputs.
- Recommendations to improve the employee performance based on insights from analysis.

### Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

### Project Structure
This project has four major parts :
1. model.py - This contains code fot our Machine Learning model to predict employee salaries absed on trainign data in 'EP.xls' file.
2. app.py - This contains Flask APIs that receives employee details through GUI or API calls, computes the precited value based on our model and returns it.
3. funcs.py - This contains the common functions needed in model.py and app.py
4. Employee prediction analysis.pptx - This contains the insights
5. templates - This folder contains the HTML template to allow user to enter employee detail and displays the predicted employee salary.

### Running the project
1. Ensure that you are in the project home directory. Create the machine learning model by running below command -
```
python model.py
```
This would create a serialized version of our model into a file model.pkl

2. Run app.py using below command to start Flask API
```
python app.py
```
By default, flask will run on port 5000.

3. Navigate to URL http://localhost:5000

Enter valid values in all input boxes and hit Predict.

If everything goes well, you should  be able to see the predcited salary value on the HTML page!
![alt text](http://www.thepythonblog.com/wp-content/uploads/2019/02/Result.png)
