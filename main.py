import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract'
from PIL import Image
import re


## Check and change current working directory
print( "Current working directory = " + os.getcwd() )
path = 'E:\Personal projects\Image differ\All samples'
os.listdir( path )
os.chdir( path )
print( "Current working directory = " + os.getcwd() )


## For all image in current working directory

## Regex area name and timedate from the extracted text
## Create a folder with the area name
## Create a folder with time slots (6am - 12pm, 12pm - 6pm, 6pm - 12am, 12am - 6am)
# If folder with area name found, move the image into the sub folder corresponding to time slot











