import numpy
import pandas
import statsmodels.api as sm

file_path = pandas.read_csv('titanic_data.csv')

predictions = {}

df = pandas.read_csv('test.csv')

for passenger_index, passenger in df.iterrows():
    
    # your code here
    Pclass = passenger['Pclass']
        
    passenger_id = passenger['PassengerId']
    if passenger['Sex'] == 'female' or passenger['Age']<18 and passenger['Pclass']==1 :
        predictions[passenger_id] = 1
    else:
        predictions[passenger_id] = 0
    
    print("{0},{1}".format(passenger_id,predictions[passenger_id]))
    #df['Survived'] = predictions[passenger_id] 