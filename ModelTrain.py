import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Activation



def Train_Model(data_train):
    modelfile = './modelweight'
    y_mean_std = "./y_mean_std.txt"
    data_train = np.matrix(data_train)
    data_mean = np.mean(data_train, axis=0)
    data_std = np.std(data_train, axis=0)
    data_train = (data_train - data_mean) / data_std
    x_train = data_train[:, 0:(data_train.shape[1] - 1)]
    y_train = data_train[:, data_train.shape[1] - 1]
    model = Sequential()
    model.add(Dense(x_train.shape[1], input_dim=x_train.shape[1], kernel_initializer="uniform"))
    model.add(Activation('relu'))
    model.add(Dense(1, input_dim=x_train.shape[1]))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(x_train, y_train, epochs=4000, batch_size=x_train.shape[0])
    model.save_weights(modelfile)
    y_mean = data_mean[:, data_train.shape[1] - 1]
    y_std = data_std[:, data_train.shape[1] - 1]
    print("训练完毕")
    f = open(y_mean_std, "w")
    mean_std = str(y_mean.astype(str)) + " " + str(y_std.astype(str))
    mean_std = mean_std.replace("[", "")
    mean_std = mean_std.replace("]", "")
    mean_std = mean_std.replace("'", "")
    f.write(mean_std)