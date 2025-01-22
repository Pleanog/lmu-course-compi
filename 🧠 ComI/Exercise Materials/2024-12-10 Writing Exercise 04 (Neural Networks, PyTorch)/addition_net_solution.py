import torch
from torch.nn import Module, Sequential, Linear, ReLU
from torch.optim import SGD, Adam, Adagrad
from tqdm import trange
import matplotlib.pyplot as plt

class Net(Module):
    '''The simple net as shown in the exercise.'''
    def __init__(self) -> None:
        super().__init__()
        self.model = Sequential(
            # TODO 1) Replicate the simple addition network architecture
            Linear(2,2),
            ReLU(),
            Linear(2,1)
        )

    def forward(self, x):
        return self.model(x)

if __name__ == "__main__":
    torch.manual_seed(42)

    net = Net()
    for alpha in [0.1, 0.5, 0.9]:
        # TODO 2) Intitialize the optimizer for the network's parameters
        optimizer = SGD(net.parameters(), lr=alpha)
        losses = []
        num_episodes = trange(100) 
        for episode in num_episodes:
            # sample two random, positive input floats
            x = torch.randn(2).round(decimals=2).abs()
            optimizer.zero_grad()
            # TODO 3) Compute the forward pass
            y = net(x)
            # TODO 4) Compute the loss and compute a backward step
            loss = torch.pow(x.sum() - y, 2)
            loss.backward()
            losses.append(loss.item())
            # TODO 5) Let the optimizer update the network parameters
            optimizer.step()
            num_episodes.set_description(f"EP({episode}:L={round(loss.item(), 3)})")
        plt.plot(range(len(losses)), losses, label=f"alpha={alpha}")
        plt.xlabel("Episodes")
        plt.ylabel("SSE Loss")
    plt.legend()
    plt.show()