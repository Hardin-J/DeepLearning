import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Dense,Flatten,Activation
from tensorflow.keras.models import Sequential

(x_train,y_train), (x_test,y_test) = tf.keras.datasets.mnist.load_data()
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

gs = 255
x_train /= gs
x_test /= gs

print("Features matrix: ",x_train.shape)
print("Target matrix: ",x_test.shape)
print("Features matrix: ",y_train.shape)
print("Target matrix: ",y_test.shape)

fig, ax = plt.subplots(10, 10)
k = 0

for i in range(10):
    for j in range(10):
        ax[i][j].imshow(x_train[k].reshape(28,28),aspect='auto')
        k+=1
plt.show()
model = Sequential([
    Flatten(input_shape=(28,28)),
    Dense(256,activation='sigmoid'),
    Dense(128,activation='sigmoid'),
    Dense(10,activation='sigmoid')
    ])
model.compile(optimizer = 'adam', loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(x_train,y_train, epochs = 10, batch_size=1000, validation_split = 0.2)
res= model.evaluate(x_test,y_test,verbose=0)

print('test loss , test accuarcy:', res)
