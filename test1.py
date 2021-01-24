import os
import glob
import time
import requests
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
import pytesseract

path = 'images'

def get_file_age(path):
    ctime = os.stat(path).st_ctime
    return ctime

def download():
    # STEP 1: Download image

    #image_url = "https://dataweb.bmkg.go.id/MEWS/Radar/TANG_SingleLayerCRefQC.png"
    image_url = "https://inderaja.bmkg.go.id/Radar/TANG_SingleLayerCRefQC.png"
    filename = image_url.split("/")[-1]

    r = requests.get(image_url, stream = True)

    if r.status_code == 200:
        r.raw.decode_content = True

        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        # print('Image successfully downloaded: ', filename)

    else:
        pass
        # print('Image couldn\'t be retreived')

    # STEP 2: Read image and OCR

    text_from_image = pytesseract.image_to_string(Image.open(filename))
    # print("Text = " + text_from_image)

    import re

    pattern = re.compile(r"\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}")
    try:
        mytimestamp = pattern.findall(text_from_image)[0]
    except:
        # print("ERROR regex")
        mytimestamp = time.strftime("%Y-%m-%d-%H-%M")
    finally:
        mytimestamp = mytimestamp.replace(':','-')
        mytimestamp = mytimestamp.replace(' ','-')
    
    # mytimestamp = pattern.findall(text_from_image)[0]
    # mytimestamp = mytimestamp.replace(':','-')
    # mytimestamp = mytimestamp.replace(' ','-')
    # print(mytimestamp)

    # STEP 3: Rename and move the file

    shutil.move(filename, 'images/' + mytimestamp + '.png')

    # STEP 4: Delete old files

    seconds = time.time() - (2 * 60 * 60) # 2 hours

    for root_files, folders, files in os.walk(path):
        for filename in files:
            time_long = get_file_age(path + "/" + filename)
            #print("seconds = {0:5.2f} : time_long = {1:5.2f}".format(seconds, time_long))
            if seconds <= time_long:
                pass
            else:
                os.remove(path + "/" + filename)

    # STEP 5: Create gif animation
    # Create the frames
    frames = []
    new_frame = None
    imgs = glob.glob("images/*.png")
    imgs.sort(key=os.path.getctime, reverse=False)
    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)

    frames.append(new_frame)
    frames.append(new_frame)

    # Save into a GIF file that loops forever
    frames[0].save('public-html/images/weather_animation.gif', format='GIF', append_images=frames[1:], save_all=True, duration=300, loop=0)


while True: 
    download() 
    time.sleep(8*60) 