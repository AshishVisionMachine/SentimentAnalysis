import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
#from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
max_features = 20000
embedding_dim = 128
sequence_length = 500


class Sentimentmodel:
    def __init__(self,par=""):
        self.par=par
        
    def model_train(self):
       
    

        inputs = tf.keras.Input(shape=(None,), dtype="int64")
        x = layers.Embedding(max_features, embedding_dim)(inputs)
        x = layers.Dropout(0.5)(x)
        
        x = layers.Conv1D(128, 7, padding="valid", activation="relu", strides=3)(x)
        x = layers.Conv1D(128, 7, padding="valid", activation="relu", strides=3)(x)
        x = layers.GlobalMaxPooling1D()(x)
        
        x = layers.Dense(128, activation="relu")(x)
        x = layers.Dropout(0.5)(x)
        
        predictions = layers.Dense(1, activation="sigmoid", name="predictions")(x)

        model = tf.keras.Model(inputs, predictions)

        return model
      
        
    def model_compile(self,model):
        model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

    
        return model
    
    def model_fit(self,model,x_train,y_train,x_test,y_test,batchsize=4,epochs=10,vsplit=0.2):
        train_ds=x_train,y_train
        val_ds=x_test,y_test
        model.fit(train_ds, validation_data=val_ds, epochs=epochs)
        
        return model
        
    def model_predict(self,model,x_test,y_test,verbs):
        test_scores = model.evaluate(test_ds)


    def vectorize_text(text, label):
        text = tf.expand_dims(text, -1)
        return vectorize_layer(text), label


    
