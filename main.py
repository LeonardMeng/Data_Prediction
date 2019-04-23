import numpy as py
import DataLoad as dataload
import ModelTrain as modeltrain
import DataPrediction as dataprediction


def main():
    data_train = dataload.load_data_train()
    modeltrain.Train_Model(data_train)
    data_pre = dataload.load_data_pre()
    pre_result = dataprediction.Predict_Data(data_pre)
    print("真实值为 930291366.85 预测结果为：%f" % (pre_result))


if __name__ == '__main__':
    main()
