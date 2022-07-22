import tensorflow as tf
import numpy as np
from tensorflow import keras

# Salary Model
def salary_model(y_new):
    xs = [0,1,2,3,4,5,6]
    ys = [0.5,0.6,0.7,0.8,0.9,1.0,1.1]
    reduce_retracing=True
    model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
    model.compile(optimizer="sgd", loss='MeanSquaredError') 
    model.fit(xs, ys, epochs=500)
    return model.predict([y_new]) [0] [0]



    
prediction = salary_model([8.0])
print()
print(prediction*100, "thousand dollars")