import os
import ocrspace
import re
import shutil
import time

from PIL import Image, ImageEnhance

EXIT_SUCCESS = 'true'
EXIT_FAILURE = 'false'

def validateAddress( ocrOut ):
    ## Regex Area Name
    regexOut = re.split("\n", ocrOut)
    filter = "".join(regexOut[0].split())
    address = regexOut[2]
    originalAddress = address # Save address before modifying it
    # print( address )
    print( regexOut )
    # print( filter == 'Google')

    if( filter == 'Google' ):
        ## Validate area name
        #
        # if re.search("India$", address ):
        #     print('Area name is good!')
        # else:
        #     print('Area name is not good!')

        ## Adding comma after state as the original image has output after state name
        substr = "Andhra Pradesh"
        inserttxt = ","
        idx = address.index(substr)+len(substr)
        address = address[:idx] + inserttxt + address[idx:]
        # print( address )
        area = re.split(",", address)
    else:
        area = ['Unknown','','','','']
    
    return area

def changeCurrentWorkingDirectory( path ):  
    ##Change current working directory
    # print( "Current working directory = " + os.getcwd() )
    os.chdir( path )
    print( "Current working directory changed to " + os.getcwd() )

def copyFile( sourceFolder, destFolder, folderName, fileName ):
    print( "Moving files to " + destFolder )
    if not os.path.exists(folderName):
        os.mkdir(folderName)
        shutil.copyfile(sourceFolder + fileName , destFolder + fileName )
    else:
        shutil.copyfile(sourceFolder + fileName , destFolder + fileName )

def enhanceImage( image ):
    print('Enhancing Image')
    # # Read image
    # im = Image.open("E:\Personal projects\Image differ\All samples\WhatsApp Image 2020-09-29 at 18.03.21 (1).jpeg")
    # #image brightness enhancer
    # enhancer = ImageEnhance.Contrast(im)
    # factor = 1 #gives original image
    # im_output = enhancer.enhance(factor)
    # im_output.save('custom-image.png')
    
def applyOCR( file ):
    enhanceImage( file )
    api = ocrspace.API('8a214b0d6788957',ocrspace.Language.English)
    ocrOut = api.ocr_file(file)
    print('\n')
    print( '------------- OCR ouput -----------' )
    print( ocrOut )
    print('\n------------------------------------\n')
    return ocrOut

def processAllFiles( path ):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    print(entry.name)
                    processFile( path + entry.name )

    except Exception as exception:
        print( exception )
        return EXIT_FAILURE
    else:
        print('Successfully processed all files' )
        return EXIT_SUCCESS        

def processFile( file ):
    try:
        print('Processing ' + file )

        ## Applying OCR to a image
        ocrOut = applyOCR( file )

        ## Validate address
        area = validateAddress( ocrOut )

        ## Extract fields from address
        areaName = area[0]
        region = area[1]
        state = area[2]
        pincode = area[3]
        country = area[4]
        print( areaName, region )

        # Create directory if not exits and move files
        folderName = areaName + ', ' + region
        destFolder = os.getcwd() + folderName + '\\' 
        # copyFile( sourceFolder, destFolder, folderName, fileName )

    except Exception as exception:
        print( exception )
        raise Exception(exception)
    else:
        print('Successfully processed ' + file + '\n' )
        return EXIT_SUCCESS  

def main():
    startTime = time.time() #To calculate run time of the program
    # os.system('cls')  #Clear screen

    ## Change current working directory
    path = 'E:\\Personal projects\\Image differ\\All samples\\Output\\'
    changeCurrentWorkingDirectory( path )

    ## Process all files of sourceFolder
    sourceFolder = 'E:\\Personal projects\\Image differ\\All samples\\' 
    if( processAllFiles( sourceFolder )):
        print( "Finished processing all files" )
    else:
        print( "An error occurred while processing the files" )

    print("\n\n--- Finished in %s seconds ---" % (time.time() - startTime))

if __name__=="__main__":
    print('========== Executing ocr_space_main ==========\n')
    # main()
    processFile( 'E:\Personal projects\Image differ\All samples\WhatsApp Image 2020-09-29 at 17.54.58 (1).jpeg' )