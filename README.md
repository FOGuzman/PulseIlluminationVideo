Official implementation for "[Compressive video via IR-pulsed illumination](https://doi.org/10.1364/OE.506011)"

# Requirements

* Python 3.9
* Pytorch >=1.10+
* Numpy
* Scikit-image
* Scikit-learn
* tqdm
* scipy
* mpmath
* tensorboard

# Installation
- install anaconda (https://www.anaconda.com/products/distribution)
- on anaconda prompt (windows) or terminal (linux) create enviroment:
```
conda create -n dpwfs python=3.9
conda activate dpwfs
```
- Install pytorch + cuda:
```
conda install pytorch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1 cudatoolkit=10.2 -c pytorch
```

# Description
This repository contains two main codes. The MATLAB code includes the basic functions extracted from [OOMAO](https://github.com/rconan/OOMAO), which are used for the analysis of results.
To train a diffractive element, we have also provided an implementation of the same equations in PyTorch.

## HowTo
