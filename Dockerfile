FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y tesseract-ocr
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y python3-requests
RUN pip3 install pillow 
RUN pip3 install pytesseract

#ENTRYPOINT ["tesseract"]
