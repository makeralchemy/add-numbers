# written for python 2.7.x
# overlay a number onto an image
# used for number images for instructables

# import required libraries
from PIL import Image
import argparse
import os
import sys

SUCCESS = 0						# return code for successful processing
FAILURE = 1						# return code when errors have occurred

HEIGHT_OFFSET = 35				# default offset from top for overlaying number image
WIDTH_OFFSET = 35				# default offset from right for overlaying number image

MIN_IMAGE_NUMBER = 1			# minimum number that can be added to the source image
MAX_IMAGE_NUMBER = 40			# maximum number that can be added to the source image

OUTPUT_FILETYPE = '.png'		# file type for the output image file
OUTPUT_NUM_SEPARATOR = '-'		# separate to be used in the output file name (e.g., "foo-025")

NUMBER_FILE_TYPE = '.png'		# file type for the number image files
NUMBER_FILES_PATH = ''  		# default path for the number image files (default is current directory)

# if the debug flag is on, display debug messages
def debug(programName, displayText):
	if printDebugMessages:
		print programName + ':', displayText
	return

# create a new image by overlaying an image with a number onto a source image
#
# inputs:
#     sourceFile is the image to be numbered
#     imageNumber is the number to overlayed on to the source image
#     numberFilesPath is the path name where the number image files are located
#     heightOffset is the number of pixels from the top to indent the number image
#     widthOffset is the number of pixels from the right to indent the number image
#
# returns a tuple containing:
#     error number (0 = success, non-zero = failure)
#     message corresponding with error number
#
def addNumberToImage(sourceFile, imageNumber, numberFilesPath, heightOffset, widthOffset):

	# if debugging is turned on, display the input parameters
	debug(progName, 'image file: ' + str(sourceFile))
	debug(progName, 'image number: ' + str(imageNumber))
	debug(progName, 'path to number image files: ' + numberFilesPath)
	debug(progName, 'height offset: ' + str(heightOffset))
	debug(progName, 'width offset: ' + str(widthOffset))

	# make sure the source image file exists before proceeding
	if not os.path.exists(sourceFile):
		errorMessage = 'source file ' + sourceFile + ' does not exist'
		return FAILURE, errorMessage

	# make sure the number file exists before proceeding
	numberFile = numberFilesPath + str(imageNumber) + NUMBER_FILE_TYPE
	debug(progName, 'number file: ' + numberFile)
	if not os.path.exists(numberFile):
		errorMessage = 'number file ' + numberFile + ' does not exist'
		return FAILURE, errorMessage

	# construct the output file name:  the file will be stored in the same path as the source file
	outputFile = os.path.join(os.path.dirname(sourceFile), os.path.basename(sourceFile).rsplit('.', 1)[ 0 ])
	
	# add a separator and the number to the file name
	outputFile = outputFile + OUTPUT_NUM_SEPARATOR + str(imageNumber).zfill(3)
	
	# add the file type to file name
	outputFile = outputFile + OUTPUT_FILETYPE 
	debug(progName, 'output file: ' + outputFile)

	# open the source image file
	debug(progName, 'opening source file: ' + sourceFile)
	sourceImage = Image.open(sourceFile)

	# extract the size of source file
	sourceWidth, sourceHeight = sourceImage.size
	debug(progName, 'source file size is ' + str(sourceWidth) + ' x ' + str(sourceHeight))

	# open the file containing the number to overlay on the source file
	debug(progName, 'opening number file: ' + numberFile)
	numberImage = Image.open(numberFile)
	numberWidth, numberHeight = numberImage.size
	debug(progName, 'number file size is ' + str(numberWidth) + ' x ' + str(numberHeight))

	# calculate the coordinates where the number will be pasted on the source file
	pasteWidth = sourceWidth - numberWidth
	pasteHeight = 0
	pasteLocation = (pasteWidth - widthOffset, heightOffset)
	debug(progName, 'paste location for number on source image is ' + str(pasteLocation))

	# make a copy of the source image
	debug(progName, 'making copy of source image')
	outputImage = sourceImage.copy()
	debug(progName, 'source image copied')

	# paste the number on top of the copy of the source image
	outputImage.paste(numberImage, pasteLocation, numberImage)
	debug(progName, 'number pasted on image')

	# save a copy to disk of the image with the number
	debug(progName, 'saving ' + outputFile)
	outputImage.save(outputFile)
	debug(progName, 'new image saved')

	# return a success return code and message
	errorMessage = outputFile + ' created'
	return SUCCESS, errorMessage

# if the program was called on the command line, the program will start here
if __name__ == "__main__":

	# process the command line input
	widthHelp = 'number of pixels from the top to offset the number; default is ' + str(HEIGHT_OFFSET)
	heightHelp = 'number of pixels from the right to offset the number; default is ' + str(WIDTH_OFFSET)	

	# parse the arguments to the addnumber command
	parser = argparse.ArgumentParser(description='Image Numbering Program')
	parser.add_argument('imagefile',  help='name of file to be numbered')
	parser.add_argument('-n', '--number', dest='imageNumber', type=int, required=True, choices=range(MIN_IMAGE_NUMBER, MAX_IMAGE_NUMBER+1), help='number to add to the image')
	parser.add_argument('-y', '--heightoffset', dest='heightOffset', default=HEIGHT_OFFSET, type=int, help=widthHelp)
	parser.add_argument('-x', '--widthoffset', dest='widthOffset', default=WIDTH_OFFSET, type=int, help=heightHelp)
	parser.add_argument('-d', '--debug', dest='debugSwitch', action='store_true', help='if specified, display debugging messages')
	parser.add_argument('-s', '--silent', dest='silentMode', action='store_true', help='if specified, do not display normal messages')
	parser.add_argument('-p', '--path', dest='numberFilesPath', default=NUMBER_FILES_PATH, help='path to the number image files; defaults to current directory')
	args = parser.parse_args()

	# extract the parameters from the parser
	progName = parser.prog.rsplit( ".", 1 )[ 0 ]	# name of this program without the .py
	sFile = args.imagefile							# file name of the source file
	iNumber = args.imageNumber 						# number to overlay on the source image
	hOffset = args.heightOffset 					# offset in pixels from top to overlay number
	wOffset = args.widthOffset 						# offset from right side to overlay number
	nFilesPath = args.numberFilesPath 				# path where number images are stored
	printDebugMessages = args.debugSwitch 			# if true debug messages will be displayed
	silentMode = args.silentMode 					# do not display normal messages if true

	# overlay the number on the source file image and save the resulting file
	errCode, errMessage = addNumberToImage(sFile, iNumber, nFilesPath, hOffset, wOffset)

	# print messages and exit with the return code
	if not silentMode:
		print errMessage
	sys.exit(errCode)



