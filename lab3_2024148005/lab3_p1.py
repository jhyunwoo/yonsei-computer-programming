#
# This code get usb size from user and calculate how much files can be stored.
# In this program, we assume that image size is 800 x 600
#

# import math module for floor function
import math

# Get USB Size
size = int(input("Enter USB size (GB): "))  # get user input and convert str to int type

usb_size_bytes = size * 1_000_000_000  # convert user input (GB) to byte

# Set Default Image Size (byte)
image_size = 800*600  # default image size

# Set Image Size by Format (byte)
gif = image_size * 1 / 5  # gif image size
jpeg = image_size * 3 / 25  # jpeg image size
png = image_size * 3 / 8  # png image size
tiff = image_size * 6  # tiff image size

# Calculate number of images by format
capable_gif = math.floor(usb_size_bytes / gif)  # gif images
capable_jpeg = math.floor(usb_size_bytes/jpeg)  # jpeg images
capable_png = math.floor(usb_size_bytes/png)  # png images
capable_tiff = math.floor(usb_size_bytes/tiff)  # tiff images

# Print result
print(format(str(capable_gif), ">5"), "images in GIF format can be stored")  # print gif result
print(format(str(capable_jpeg), ">5"), "images in JPEG format can be stored")  # print jpeg result
print(format(str(capable_png), ">5"), "images in PNG format can be stored")  # print png result
print(format(str(capable_tiff), ">5"), "images in TIFF format can be stored")  # print tiff result

