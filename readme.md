# Download Weather image and create GIF Animation file using Tesseract


## Description:
This service will do the following:
1. grab current radar image from BMKG at this address: 
    >https://inderaja.bmkg.go.id/Radar/TANG_SingleLayerCRefQC.png
2. save the image in current directory
3. try to recognize the datetime from the image, otherwise will create self timestamp
4. rename the downloaded image and move it to `images` directory
5. create gif animation for all images under `images` directory and save it as `weather_animation.gif` in the current folder

## Build and Run:

Create Dockerfile with the following entries:
```python
FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y tesseract-ocr
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y python3-requests
RUN pip3 install pytesseract
```

To build the docker image, run the following docker command:
>```docker build --tag tesseract:v0.3 .```

Run the docker container by running (current directory will be mapped to /home in the container)
>```docker run -it -v $PWD:/home tesseract:v0.3```

Run the application inside the container by running:
>```python3 test1.py```

Then the result gif file can be opened manually using a browser or VisualCode

To do:
1. to run straight from docker: 
    >```docker run -d -v $PWD:/home -w /home tesseract:v0.3 python3 test1.py```

Update Date: 24 January 2021

## Installing Docker on Raspberry Pi

After hours of trying to install (success) and run ```docker-compose``` (many unsuccessfull), I finnaly managed to have a stable (and runnable) docker and its utilities.
I am now using Ubuntu Server 20.04.1 LTS 64-bit (https://ubuntu.com/download/raspberry-pi).
The instructions on installing docker can be found here:
> https://wiki.learnlinux.tv/index.php/Setting_up_a_Raspberry_Pi_Kubernetes_Cluster_with_Ubuntu_20.04

Information on configuring Wi-Fi on ubuntu server can be found here:
>https://www.linuxbabe.com/ubuntu/connect-to-wi-fi-from-terminal-on-ubuntu-18-04-19-04-with-wpa-supplicant


## Multi-container and multi services
Right now I am using ```docker-compose.yml``` to build 2 services:
1. ```app```:
This is the python code to download, OCR, and create gif animations
2. ```web```:
This is the web service (apache/httpd)

They both will access ```public-html``` folder (the ```app``` will put the gif animation file, and the ```web``` will serve)

## Installing on AWS
todo....