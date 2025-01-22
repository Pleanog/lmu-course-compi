import torch
from torch.nn import Module, Sequential, Linear, ReLU
from torch.optim import SGD, Adam, Adagrad
from torch.nn.functional import mse_loss
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from tqdm import trange

class Net(Module):
    '''The simple net as shown in the exercise.'''
    pass
    # TODO Add your network architecture 

if __name__ == "__main__":
    torch.manual_seed(42)

    # Visualization of the dataset
    coordinates, labels = make_circles(500, noise=0.05)
    for (x1,x2),y in zip(coordinates, labels):
        plt.scatter(x1, x2, color="orange" if y else "blue")
    plt.show()

    # TODO Add your network instance and the optimizer for the net's parameters
    for epoch in trange(250):
        for x,y in zip(coordinates.tolist(), labels.tolist()):
            # TODO Add your network training loop (zero the gradient, forward(), backward(), update step)
            pass