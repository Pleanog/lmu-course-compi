import torch
from torch.nn import Module, Sequential, Linear, ReLU
from torch.optim import SGD, Adam, Adagrad
from tqdm import trange
import matplotlib.pyplot as plt

# Setup:
#(venv)> pip install torch, numpy, tqdm, matplotlib

class Net(Module):
    '''The simple net as shown in the exercise.'''
    def __init__(self) -> None:
        super().__init__()
        self.model = Sequential(
            # TODO 1) Replicate the simple addition network architecture
            # your code here
        )

    def forward(self, x):
        # TODO 3) Compute the forward pass
        pass # your code here

if __name__ == "__main__":
    torch.manual_seed(42)
    net = Net()
    alpha = 0.3

    # TODO 2) Intitialize the SDG optimizer for the network's parameters with the given learning rate
    optimizer = None # your code here
    num_episodes = trange(100) 
    for episode in num_episodes:
        # sample two random, positive input floats
        x = torch.randn(2).round(decimals=2).abs()
        optimizer.zero_grad()

        # TODO 3) Compute the forward pass
        y = None # your code here
        
        # TODO 4) Compute the SSE loss and compute a backward step
        loss = None # your code here
        
        # TODO 5) Let the optimizer update the network parameters
        # your code here
        
        # some information for the progress bar
        num_episodes.set_description(f"EP({episode}:L={round(loss.item(), 3)})")