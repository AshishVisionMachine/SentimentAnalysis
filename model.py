import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


class Sentimentmodel:
    def __init__(self,par=""):
        self.par=par
        
    def model_train(self,input,label):
        #print("model_train input is {}",input[0,:])
        #input=np.reshape(input[0,:],(784,))
        inputs = keras.Input(shape=(784,))
        dense = layers.Dense(64, activation="relu")
        x = dense(inputs)
        x = layers.Dense(64, activation="relu")(x)
        #outputs = layers.Dense(10)(x)
        output = dense(10 , activation = 'softmax')(x)
        model = keras.Model(inputs=inputs, outputs=outputs, name="sentiment_model")
        
        return model
      
        
#  def model_save(self):
    
#    def 