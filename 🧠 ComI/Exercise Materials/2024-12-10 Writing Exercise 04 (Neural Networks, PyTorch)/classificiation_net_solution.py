import torch
from torch.nn import Module, Sequential, Linear, ReLU
from torch.optim import SGD, Adam, Adagrad
from torch.nn.functional import mse_loss
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from tqdm import trange

class Net(Module):
    '''The simple net as shown in the exercise.'''
    def __init__(self) -> None:
        super().__init__()
        self.model = Sequential(
            Linear(2,2),
            ReLU(),
            Linear(2,1)
        )

    def forward(self, x):
        return self.model(x)

if __name__ == "__main__":
    torch.manual_seed(42)

    coordinates, labels = make_circles(500, noise=0.05)
    for (x1,x2),y in zip(coordinates, labels):
        plt.scatter(x1, x2, color="orange" if y else "blue")
    #plt.show()
    plt.clf()

    net = Net()
    alpha = 0.1
    optimizer = SGD(net.parameters(), lr=alpha)
    for epoch in trange(250):
        losses = []
        for x,y in zip(coordinates.tolist(), labels.tolist()):
            optimizer.zero_grad()
            y_pred = net(torch.tensor(x))
            loss = mse_loss(y_pred, torch.tensor(y).float().unsqueeze(-1))
            loss.backward()
            losses.append(loss.item())
            optimizer.step()
        plt.scatter(epoch, sum(losses)/len(losses))
    plt.xlabel("Epoch")
    plt.ylabel("MSE Loss")
    plt.show()