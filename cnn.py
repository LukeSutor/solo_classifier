from torch import nn
import torch.nn.functional as F


class CNNNetwork(nn.Module):

    def __init__(self):
        super().__init__()
        # 4 convolutional blocks / flatten / linear / softmax
        self.conv1 = nn.Sequential(
            nn.Conv2d(
                in_channels=1,
                out_channels=16,
                kernel_size=3,
                stride=1,
                padding=2
            ),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(
                in_channels=16,
                out_channels=32,
                kernel_size=3,
                stride=1,
                padding=2
            ),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )
        self.conv3 = nn.Sequential(
            nn.Conv2d(
                in_channels=32,
                out_channels=64,
                kernel_size=3,
                stride=1,
                padding=2
            ),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )
        self.conv4 = nn.Sequential(
            nn.Conv2d(
                in_channels=64,
                out_channels=128,
                kernel_size=3,
                stride=1,
                padding=2
            ),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )
        self.flatten = nn.Flatten()
        print(self.flatten)
        self.linear = nn.Linear(17920, 4)  # Output is set to 3 for now,
        # this value is the number of guitarists, edit later
        self.softmax = nn.Softmax(dim=1)
        # super(CNNNetwork, self).__init__()
        # self.conv1 = nn.Conv2d(1, 128, 3, 1, 2)
        # self.bn1 = nn.BatchNorm2d(128)
        # self.pool1 = nn.MaxPool2d(4)
        # self.conv2 = nn.Conv2d(128, 128, 3)
        # self.bn2 = nn.BatchNorm2d(128)
        # self.pool2 = nn.MaxPool2d(4)
        # self.conv3 = nn.Conv2d(128, 256, 3)
        # self.bn3 = nn.BatchNorm2d(256)
        # self.pool3 = nn.MaxPool2d(4)
        # self.conv4 = nn.Conv2d(256, 512, 3)
        # self.bn4 = nn.BatchNorm2d(512)
        # self.pool4 = nn.MaxPool2d(4)
        # # input should be 512x30 so this outputs a 512x1
        # self.avgPool = nn.AvgPool1d(30)
        # self.fc1 = nn.Linear(512, 4)

    def forward(self, input_data):
        x = self.conv1(input_data)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        x = self.flatten(x)
        logits = self.linear(x)
        predictions = self.softmax(logits)
        return predictions
        x = self.conv1(input_data)
        x = F.relu(self.bn1(x))
        x = self.pool1(x)
        x = self.conv2(x)
        x = F.relu(self.bn2(x))
        x = self.pool2(x)
        x = self.conv3(x)
        x = F.relu(self.bn3(x))
        x = self.pool3(x)
        x = self.conv4(x)
        x = F.relu(self.bn4(x))
        x = self.pool4(x)
        x = self.avgPool(x)
        x = x.permute(0, 2, 1)  # change the 512x1 to 1x512
        x = self.fc1(x)
        return F.log_softmax(x, dim=2)


if __name__ == "__main__":
    cnn = CNNNetwork()
    print(cnn)
