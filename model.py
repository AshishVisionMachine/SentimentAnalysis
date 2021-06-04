import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


class Sentimentmodel:
    def __init__(self,par=""):
        self.par=par
        
    def model_train(self,input,label):
        inputs = keras.Input(shape=(3,3,32), name="img")
        x = layers.Conv2D(32, 3, activation="relu")(inputs)
        x = layers.Conv2D(64, 3, activation="relu")(x)
        block_1_output = layers.MaxPooling2D(3)(x)

        x = layers.Conv2D(64, 3, activation="relu", padding="same")(block_1_output)
        x = layers.Conv2D(64, 3, activation="relu", padding="same")(x)
        block_2_output = layers.add([x, block_1_output])

        x = layers.Conv2D(64, 3, activation="relu", padding="same")(block_2_output)
        x = layers.Conv2D(64, 3, activation="relu", padding="same")(x)
        block_3_output = layers.add([x, block_2_output])

        x = layers.Conv2D(64, 3, activation="relu")(block_3_output)
        x = layers.GlobalAveragePooling2D()(x)
        x = layers.Dense(256, activation="relu")(x)
        x = layers.Dropout(0.5)(x)
        outputs = layers.Dense(10)(x)

        model = keras.Model(inputs, outputs, name="toy_resnet")
        
        return model
      
        
    def model_compile(self,model):
        model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=keras.optimizers.RMSprop(),
    metrics=["accuracy"],
    )
    
        return model
    
    def model_fit(self,model,x_train,y_train,batchsize,epoc,vsplit):
        history = model.fit(x_train, y_train, batch_size=batchsize, epochs=epoc, validation_split=vsplit)
        
        return model
        
    def model_predict(self,model,x_test,y_test,verbs):
        test_scores = model.evaluate(x_test, y_test, verbose=verbs)
        
    

    
