This code works for all linux oerating environments. Ubuntu particularly is very good option for programming machine learning codes and python programmes. 
If you are doing this project, you might have already installed python 2.7 or 3.5+ version with opencv installed.
There are few things which is needed to be installed and setup.
First thing is dlib library for opencv, a tool for implementing a variety of machine learning algorithms, including classification, regression, clustering, data transformation, and structured prediction.
Befor installing dlib, few other dependencies are to be installed which can be installed using the command
 sudo apt-get install
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-dev \
    libavcodec-dev \
    libavformat-dev \
    libboost-all-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    python3-pip \
    zip
    
    Then we can directly run the command : sudo apt-get install dlib , We can find related examples related to dlib usage in its installation directory, those are very interesting to see.
    dlib takes lot of time to install, hence you can get coffee for 20-25 minutes   

Second is face_recognition library which can be installed by : sudo pip3 install face_recognition 
dlib + face_recognition library give us an easy way of recognising faces using any camera.
