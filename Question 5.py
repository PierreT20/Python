from cImage import *

def SmoothPixel(oldPixel):
    newRed = (int(oldPixel.getRed()/2))*1
    newGreen = (int(oldPixel.getGreen()/2))*1
    newBlue = (int(oldPixel.getBlue()/2))*1
    newPixel = Pixel(newRed, newGreen, newBlue)
    return newPixel

def MakeSmooth(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    Win = ImageWin('Smooth Image', width *2, height)
    oldImage.draw(Win)
    newImage = EmptyImage(width, height)

    for row in range(height):
        for col in range(width):
            oldPixel = oldImage.getPixel(col, row)
            newPixel = SmoothPixel(oldPixel)
            newImage.setPixel(col, row, newPixel)
    newImage.setPosition(width + 1, 0)
    newImage.draw(Win)
    
MakeSmooth("pic.gif")
                         
