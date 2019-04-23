import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Activation

def load_y():
    f = open("./y_mean_std.txt", "r")
    y_mean = f.read();
    y_mean = y_mean.split(" ")
    f.close()
    return y_mean

def Predict_Data(data_pre):
    model = Sequential()
    model.add(Dense(data_pre.shape[1], input_dim=data_pre.shape[1], kernel_initializer="uniform"))
    print(data_pre.shape[1])
    model.add(Activation('relu'))
    model.add(Dense(1, input_dim=data_pre.shape[1]))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.load_weights('./modelweight')
    mean_std = load_y()
    pre_result = model.predict(data_pre) * float(mean_std[1]) + float(mean_std[0])
    print(model.summary())
    return pre_result
