import torch.nn as nn
import torch
import matplotlib.pyplot as plt


class Self_Attention(nn.Module):
    def __init__(self, dim, dk, dv):
        super(Self_Attention, self).__init__()
        self.scale = dk ** -0.5
        self.q = nn.Linear(dim, dk)
        self.k = nn.Linear(dim, dk)
        self.v = nn.Linear(dim, dv)


    def forward(self, x):
        q = self.q(x)
        k = self.k(x)
        v = self.v(x)

        attn = (q @ k.transpose(-2, -1)) * self.scale
        attn = attn.softmax(dim=-1)

        x = attn @ v
        return x


att = Self_Attention(dim=3, dk=3, dv=4)
x = torch.rand((1, 5, 3))

# x = torch.randint(1, 10, [5, 3])
print(x)
output = att(x)
print(output)
