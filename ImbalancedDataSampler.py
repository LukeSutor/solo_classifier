import torch
import torch.utils.data
from collections import Counter


class ImbalancedDatasetSampler(torch.utils.data.sampler.Sampler):

    def __init__(self, dataset):
        self.indices = list(range(len(dataset)))

        self.num_samples = len(self.indices)

        # Get the number of samples for each guitarist
        trainclasses = [label for _, label in dataset]
        counter = Counter(trainclasses)

        weights = [0, 0, 0, 0]

        for i in range(len(counter)):
            weights[i] = 1 / counter.pop(i)

        self.weights = torch.DoubleTensor(weights)

    def __iter__(self):
        return (self.indices[i] for i in torch.multinomial(self.weights, self.num_samples, replacement=True))

    def __len__(self):
        return self.num_samples
