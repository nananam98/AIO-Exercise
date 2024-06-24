import torch
import torch.nn as nn

class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        sum_exp_x = torch.sum(exp_x, dim=-1, keepdim=True)
        return exp_x / sum_exp_x

class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        c = torch.max(x, dim=0, keepdim=True)[0]
        exp_x = torch.exp(x - c)
        sum_exp_x = torch.sum(exp_x, dim=0, keepdim=True)
        return exp_x / sum_exp_x

if __name__ == "__main__":
    x = torch.tensor([1, 2, 3000000000])

    softmax = Softmax()
    print("Softmax:", softmax(x))

    softmax_stable = SoftmaxStable()
    print("Softmax Stable:", softmax_stable(x))
