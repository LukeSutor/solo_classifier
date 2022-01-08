# Solo Classifier
## Goal:
Classify which guitarist is playing based on input song audio or tell user which guitarist their tone is most similar to.


## Guitarists:
* Jimmy Page
* Eddie Van Halen
* David Gilmour
* Eric Clapton


## Data Collection
Data for this model was collected from youtube, from the respective artist's channels and stored in the audio directory. After this, the songs were reduced down into one or more files of just the guitar solos. Finally, the solos were passed into the MinimizeSolo.py function, which chopped them down further into ten second snippets, which could be turned into mel spectrograms and passed into the network.


## Technologies:
Torchaudio for audio preprocessing and transformations (mel spectrogram) with PyTorch and [timm](https://github.com/rwightman/pytorch-image-models), using Google's efficientnetv2 small model for training.


## Model Hyperparameters:
* Epochs: 300
* Batch Size: 32
* Learning rate: 0.0001
* Using Autocast
* Gradient Accumulation of 4