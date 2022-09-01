from cImage import *

def redintensity(oldPixel):
    red = 0
    if oldPixel.getRed()<= 200:
        red = oldPixel.getRed()+50
    elif oldPixel.getRed()<240:
        red = oldPixel.getRed()+10

    green = oldPixel.getGreen() 
    blue = oldPixel.getBlue() 
    newPixel = Pixel(red,green//4,blue//4)

    return newPixel

def newImage(imageFile):
    oldImage = FileImage(imageFile)
    Width = oldImage.getWidth()
    Height = oldImage.getHeight()

    win = ImageWin("Red Intensity Image",Width,Height)
    
    newImage = EmptyImage(Width,Height)
    for r in range(Height):
        for c in range(Width):
            oldPixel = oldImage.getPixel(c,r)
            newPixel = redintensity(oldPixel)
            newImage.setPixel(c,r,newPixel)

    newImage.draw(win)
    

newImage("butterfly.gif")
