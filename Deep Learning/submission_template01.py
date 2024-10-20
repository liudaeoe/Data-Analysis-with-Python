import numpy as np
import torch
from torch import nn
 model = nn.Sequential(
        nn.Linear(784, 256), 
        nn.ReLU(),
        nn.Linear(256, 16),
        nn.ReLU(), 
        nn.Linear(16, 10) 
    )
def create_model():
    #
    # return model instance (None is just a placeholder)

    return None

def count_parameters(model):
    # def count_parameters(model):
    # your code here

    # верните количество параметров модели model
   return sum(param.numel() for param in model.parameters())
    # return integer number (None is just a placeholder)
    
    return None
