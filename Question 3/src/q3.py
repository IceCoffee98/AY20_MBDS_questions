# %%
import torch
import torch.nn.functional as F
import pandas as pd


# %%
# Read Input file
train_data = pd.read_csv('../input/train_data.txt', sep='\t').values
test_data = pd.read_csv('../input/test_data.txt', sep='\t').values
train_label = pd.read_csv('../input/train_truth.txt').values
# Make numpy data -> tensor data
train_data = torch.tensor(train_data)
test_data = torch.tensor(test_data)
train_label = torch.tensor(train_label)


# %%
# Buile multilayer perceptron for regression
class Net(torch.nn.Module):
    # Input params:
    # n_feature: the dim of x(x1, x2, x3), so n_feature = 3
    # n_hidden: 4 * 4 hidden layers in the title, so n_hidden = 4
    # n_output: regression, fo n_output = 1
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        # 4 * 4 hidden layers
        self.hidden_1 = torch.nn.Linear(n_feature, n_hidden)
        self.hidden_2 = torch.nn.Linear(n_hidden, n_hidden)
        self.hidden_3 = torch.nn.Linear(n_hidden, n_hidden)
        self.hidden_4 = torch.nn.Linear(n_hidden, n_hidden)
        # 1 output layer
        self.predict = torch.nn.Linear(n_hidden, n_output)

    def forward(self, x):
        # network forward propagation
        x = self.hidden_1(x)
        x = self.hidden_2(x)
        x = self.hidden_3(x)
        x = F.relu(self.hidden_4(x))
        x = self.predict(x)
        return x


# %%
net = Net(n_feature=3, n_hidden=4, n_output=1)

# optimizer params
optimizer = torch.optim.Adam(net.parameters())
# loss function
loss_func = torch.nn.MSELoss()

# train 500 epoch
for epoch in range(501):
    prediction = net(train_data.float())

    loss = loss_func(prediction, train_label.float())
    if epoch % 100 == 0:
        print('Epoch:', epoch, 'Loss:', loss.item())
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

y = net(test_data.float())

with open('../output/test_predicted.txt', 'w') as f:
    f.write('y\n')
    for i in y:
        f.write(str(i[0].item()) + '\n')
# %%
