# addnumbers

## Overview
*addnumber.py* is a program used to create photos for step by step instructions like instructables. *addnumber.py* will overlay an image containing a number on top of an photo.  *addnumber.py* will use the set of images in this repository as the numbers that will be overlayed on top of the photos. The number files have numbers inside of circles with transparent backgrounds.

*addnumber.py* is written for python 2.7.x.

## Usage Instructions

*addnumber.py* can be executed from the command line or as a function imported by another python program.

### Command Line Usage:

    usage: addnumber.py [-h] -n IMAGENUMBER [-y HEIGHTOFFSET] [-x WIDTHOFFSET]
                        [-d] [-s] [-l] [-p NUMBERFILESPATH]
                        imagefile

    Image Numbering Program

    positional arguments:
      imagefile             name of file to be numbered

    optional arguments:
      -h, --help            show this help message and exit
      -n IMAGENUMBER, --number IMAGENUMBER
                            number to add to the image
      -y HEIGHTOFFSET, --heightoffset HEIGHTOFFSET
                            number of pixels from the top to offset the number;
                            default is 35
      -x WIDTHOFFSET, --widthoffset WIDTHOFFSET
                            number of pixels from the right to offset the number;
                            default is 35
      -d, --debug           if specified, display debugging messages
      -s, --silent          if specified, do not display normal messages
      -l, --leading         if specified, put file number before file name
      -p NUMBERFILESPATH, --path NUMBERFILESPATH
                            path to the number image files; defaults to current
                            directory
     
    
#### Command Line Examples
Create a new image by adding the number 5 to *testimage.jpg*. The new file will be called *testimage-005.jpg* and will be stored in the same directory as *testimage.jpg*. Number files are in the current directory. Default offsets for placement of the number will be used.

    $ python addnumber.py -n 5 testimage.jpg

Create a new image by adding the number 5 to *testimage.jpg*. The new file will be called *005-testimage.jpg* and will be stored in the same directory as *testimage.jpg*. Number files are in the current directory. Default offsets for placement of the number will be used.

    $ python addnumber.py -n 5 -l testimage.jpg

Create a new image by adding the number 8 to *testimage.jpg*. The new file will be called *testimage-008.jpg* and will be stored in the same directory as *testimage.jpg*. Number files are in the current directory. Default offsets for placement of the number will be used.

    $ python addnumber.py -n 8 /path/to/my/project/testimage.jpg

Create a new image by adding the number 12 to *testimage.jpg*. Offset the image by 120 pixels from the top and 145 pixels from right edge.  The numbered image will be called *testimage-012.jpg* and will be stored in the same directory as *testimage.jpg*. Number files are in the current directory.

    $ python addnumber.py -n 12 -y 120 -x 145 testimage.jpg

Create a new image by adding the number 35 to *testimage.jpg*. Number files are stored in /path/to/number/files. The numbered image will be called *testimage-035.jpg* and will be stored in the same directory as *testimage.jpg*. Default offsets for placement of the number will be used.

    $ python addnumber.py -n 35 -p /path/to/number/files testimage.jpg

#### Messages
If *addnumber.py* completes successfully, *addnumber.py* will display a message like:

    testimage-023.jpg created

and return 0 for the error code.

If the input source image file is not found, *addnumber.py* will display an error message like: 

    source file testimage.jpg does not exist

and return 1 for the error code.

If the number image file is not found, *addnumber.py* will display an error message like:

    number file 5.png does not exist

and return 1 for the error code.

If the number to be added to the image is not in the proper range, *addnumber.py* will display the message:

    image number must be 1 to 40

### Python usage:
#### Syntax
    addNumberToImage(sourceFile, imageNumber, numberFilesPath, heightOffset, widthOffset, prefixFileNum)

    sourceFile             string with the name of the source file.
    imageNumber            integer of the number to be overlayed on the image.
    numberFilesPath        string containing the path to where the number files are stored. '' indicates current path.
    heightOffset           integer of the number of pixels from the top to offset the number.
    widthOffset            integer of the number of pixels from the right edge to offet the number.
    progName =             string to be used as the program name in debug messages
    printDebugMessages =   boolean indicating whether to display debug messages
    prefixFileNum          boolean if true the file name will be preceeded with the file number; if false the file name will be appended with the file number
#### Examples
Create a new image by adding the number 5 to *testimage.jpg* in the current directory. The new file will be called *testimage-005.jpg* and will be stored in the same directory as *testimage.jpg*. Offset the number by 35 pixels from the top and 35 pixels from the right. Number files are in the current directory.

    import addnumber
    errCode, errMessage = addnumber.addNumberToImage('testimage.jpg', 5, '', 35, 35)

Create a new image by adding the number 5 to *testimage.jpg* in the current directory. The new file will be called *005-testimage.jpg* and will be stored in the same directory as *testimage.jpg*. Offset the number by 35 pixels from the top and 35 pixels from the right. Number files are in the current directory.

    import addnumber
    errCode, errMessage = addnumber.addNumberToImage('testimage.jpg', 5, '', 35, 35, prefixFileNum = True)

Create a new image by adding the number 8 to *testimage.jpg* in the directory */path/to/my/project*. The new file will be called *testimage-005.jpg* and will be stored in the same directory as *testimage.jpg*. Offset the number by 35 pixels from the top and 35 pixels from the right. Number files are in the current directory.

    import addnumber
    errCode, errMessage = addnumber.addNumberToImage('/path/to/my/project/testimage.jpg', 8, '', 35, 35)

Create a new image by adding the number 12 to *testimage.jpg* in the current directory. Offset the image by 40 pixels from the top and 45 pixels from right edge.  The numbered image will be called *testimage-012.jpg* and will be stored in the same directory as *testimage.jpg*. Number files are in the current directory. Print debugging messages.

    import addnumber
    errCode, errMessage = addnumber.addNumberToImage('testimage.jpg', 12, '', 40, 45, printDebugMessages = True)

Create a new image by adding the number 35 to *testimage.jpg*. Number files are stored in /path/to/number/files. The numbered image will be called *testimage-035.jpg* and will be stored in the same directory as *testimage.jpg*. 
  
    import addnumber
    errCode, errMessage = addnumber.addNumberToImage('testimage.jpg', 35, '/path/to/number/files', 35, 35)

## Installation Instructions
*addnumber.py* requires the Pillow imaging library to be installed. The procedure to install Pillow can be found [here](https://python-pillow.org/).

Change to the directory where you want the files to be installed.

Install *addnumber.py* and the associated files by cloning this repository with this command:

    git clone https://github.com/makeralchemy/addnumbers

Verify everything has installed properly using the provided test image. Use the debug option in the command to see what *addnumber.py* is doing:

    python addnumber.py testimage.jpg --number 4 --debug

or

    python addnumber.py testimage.jpg -n 4 -d 

If everything has been installed properly, a new file *testimage-004.jpg* should have been created in the directory with the number 4 in a circle overlayed on the upper right corner of the image.

## License
This project is licensed under the MIT license.

