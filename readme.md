# Download Weather image and create GIF Animation file user Tesseract


## Description:
This service will do the following:
1. grab current radar image from BMKG at this address: 
    >```https://inderaja.bmkg.go.id/Radar/TANG_SingleLayerCRefQC.png```
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