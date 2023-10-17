import pandas as pd
import numpy as np 
from keras.models import load_model
from sklearn.preprocessing import StandardScaler


data_train = pd.read_csv('df_combined.csv')
X_train = data_train[['total_purchase', 'frequency_purchase']].values
scaler = StandardScaler()
scaler.fit(X_train)

def realice_prediction(value_purchase, value_frequency):
    model = load_model('data_customer_classification.h5')
    
    new_values = np.array([[value_purchase, value_frequency]])  

    new_values = scaler.transform(new_values)

    prediction = model.predict(new_values)

    result = np.argmax(prediction, axis=1) + 1 

    return result

test = realice_prediction(1525, 25)

if test[0] == 1:
    print('Qualified customer low')
elif test[0] == 2:
    print('Qualified customer Medium')
else:
    print('Qualified customer High')