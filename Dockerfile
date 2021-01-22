FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y tesseract-ocr
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y python3-requests
RUN pip3 install pytesseract #V0.3

#ENTRYPOINT ["tesseract"]
