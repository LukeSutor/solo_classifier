# Solo Classifier
## Goal:
Classify which guitarist is playing based on input song audio or tell user which guitarist their tone is most similar to.


## Guitarists:
* Jimmy Page
* Eddie Van Halen
* David Gilmour
* Eric Clapton


## Technologies:
Torchaudio for audio preprocessing and transformations (mel spectrogram) with PyTorch and [timm](https://github.com/rwightman/pytorch-image-models), using Google's efficientnetv2 small model for training.


## Model Hyperparameters:
* Epochs: 300
* Batch Size: 32
* Learning rate: 0.0001
* Using Autocast
* Gradient Accumulation of 4


