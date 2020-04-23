# Crowd 
(Image Clustering package)

(Note: Currently working on bettering Image clustering and creating a pypi package for quick installation)

### Installing Steps for requirements python package
#### Installing dlib on Ubuntu
The following instructions were gathered on Ubuntu 16.04 but should work on newer versions of Ubuntu as well.

To get started, let’s install our required dependencies:

```
sudo apt-get update
sudo apt-get -y install build-essential \
                        cmake \
                        libopenblas-dev \
                        liblapack-dev \
                        libx11-dev \
                        libgtk-3-dev
```
after
```
pip install dlib
```
#### Installing pyfacy models on Ubuntu

```
pip install pyfacy_dlib_models \
            imutils \
            numpy \
            scipy \
            scikit-learn
```

#### Installing pyfacy
(in progress)
```
pip install git+https://github.com/Dotmole/image-clustering.git
```
