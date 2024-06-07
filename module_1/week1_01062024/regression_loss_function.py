import random
import math

def mae(predict, target):
    return abs(predict - target)

def mse(predict, target):
    return (predict - target) ** 2

def rmse(predict, target):
    return math.sqrt(mse(predict, target))

def main():
    num_samples = input("Nhập số lượng sample: ")
    if not num_samples.isnumeric():
        print("number of samples must be an integer number")
        return
    num_samples = int(num_samples)

    loss_name = input("Nhập loss name (MAE, MSE, RMSE): ")
    samples = []
    total_loss = 0

    for i in range(num_samples):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)
        samples.append((predict, target))

        if loss_name == "MAE":
            loss_value = mae(predict, target)
        elif loss_name == "MSE":
            loss_value = mse(predict, target)
        elif loss_name == "RMSE":
            loss_value = rmse(predict, target)
        
        total_loss = total_loss + loss_value
        print(f"Loss name: {loss_name}, sample: {i}, pred: {predict}, target: {target}, loss: {loss_value}")

if __name__ == "__main__":
    main()
