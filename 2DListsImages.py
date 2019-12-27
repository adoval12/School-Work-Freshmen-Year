#
# Images as 2-D lists  
#
# 

from hmcpng import *

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []

    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels

def blank_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are green.
        inputs: height and width are non-negative integers
    """
    all_green = create_uniform_image(height, width, [0, 255, 0])
    return all_green

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100

## put your functions below
def grayscale(pixels):
    """ This function takes the 2-D list pixels containing pixels for an image
        and the function creates and returns a new 2-D list of pixels for an
        image that is a grayscale version of the original image."""
    gray_scale = pixels[:][:][:]
    for n in range(len(pixels)):
        gray_scale[n] = [x[:] for x in pixels[n]]
    for i in range(len(gray_scale)):
        for j in range(len(gray_scale[0])):
            for k in range(len(gray_scale[0][0])):
                gray_scale[i][j][k] = brightness(pixels[i][j])
    return gray_scale

def fold_diag(pixels):
    """ This function takes the 2-D list pixels containing pixels for an image
        This function then creates and returns a new 2-D list of pixels for an
        image in which the original image is “folded” along its diagonal. """
    fold_diag = pixels[:][:][:]
    for n in range(len(pixels)):
        fold_diag[n] = [x[:] for x in pixels[n]]
    for i in range(len(pixels)):
        for j in range(len(pixels[0])):
            for k in range(len(pixels[0][0])):
                if range(len(pixels))[i] > range(len(pixels[i]))[j]:
                         fold_diag[i][j][k] = 255
                else:
                        fold_diag[i][j][k] = pixels[i][j][k]
    return fold_diag

def mirror_horiz(pixels):
    """This function takes the 2-D list pixels containing pixels for an image.
       This function creates and returns a new 2-D list of pixels for an image 
       in which the original image is “mirrored". """
    mirror_horiz = pixels[:][:][:]
    for n in range(len(pixels)):
        mirror_horiz[n] = [x[:] for x in pixels[n]]
    mirror_width = (len(pixels[0]) - 1) / 2
    full_mirror_width = (len(pixels[0]) - 1)
    mirror_height = (len(pixels) - 1) / 2
    full_mirror_height = (len(pixels) - 1)
    for i in range(len(pixels)):
        for j in range(len(pixels[0])):
            if range(len(pixels[0]))[j] > mirror_width and range(len(pixels[0]))[j] < full_mirror_width  :
                mirror_horiz[i][j] = pixels[i][-j]
            if range(len(pixels))[i] < mirror_height and range(len(pixels))[i] > full_mirror_height:
                mirror_horiz[i][j] = pixels[i][j]  
    return mirror_horiz


def extract(pixels, rmin, rmax, cmin, cmax):
    """This function takes the 2-D list pixels containing pixels for an image, then it
       creates and returns a new 2-D list that represents the portion of the original
       image that is specified by the other four parameters."""
    extract_image = blank_image(((rmax) - rmin), ((cmax) - cmin))
    for i in range(len(pixels)):
        for j in range(len(pixels[0])):
            if (rmin <= range(len(pixels))[i] < rmax) and (cmin <= range(len(pixels[0]))[j] < cmax):
                extract_image[(i - rmin)][(j - cmin)] = pixels[i][j]
    return extract_image


    
    
    
       
    
        

    
