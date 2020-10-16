import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract'
from PIL import Image
import re


def extract_text(path, logFile):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                print(entry.name)
                sourceImage =  Image.open(entry.name)
                extractedText = pytesseract.image_to_string(sourceImage)
                prettyText = [] 
                prettyText.append(re.sub('\n', ',', extractedText)) 
                f.write(str(prettyText))
                f.write("\n")
    

## Check and change current working directory
print( "Current working directory = " + os.getcwd() )

path = 'E:\Personal projects\Image differ\All samples'
os.listdir( path )
os.chdir( path )

print( "Current working directory = " + os.getcwd() )

logFile = "E:\Personal projects\Image differ\logs\log.txt"
if os.path.exists(logFile):
    os.remove(logFile)
f = open(logFile,"w+")


## Printing out text in a image
print("\n\n++++++++++++++++ Text in Image ++++++++++++++++++++ \n\n")
# extract_text(path,logFile)
print("\n\n++++++++++++++++ End Text ++++++++++++++++++++ \n\n")


image_file =  Image.open('WhatsApp Image 2020-09-29 at 18.03.21 (1).jpeg')

text = pytesseract.image_to_string(image_file)
print(text)

image_file = image_file.convert('L') # convert image to black and white
image_file.save('question.png')
text = pytesseract.image_to_string(image_file)
print(text)

image_file.convert('L')




