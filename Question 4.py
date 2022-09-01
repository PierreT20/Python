from cImage import*

def black(oldP):
    blackPixel = Pixel(255,255,255)
    whitePixel = Pixel(0,0,0)
    intensitySum = oldP.getRed() + oldP.getGreen() + oldP.getBlue()
    aveRGB = intensitySum//3
    if aveRGB > 128:
        newPixel = blackPixel
    else:
        newPixel = whitePixel

    return newPixel

def white(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    Win = ImageWin("bw",width*2,height)
    oldImage.draw(Win)
    newIm = EmptyImage(width,height)

    for row in range(height):
        for col in range(width):
            oldP = oldImage.getPixel(col,row)
            newPixel = black(oldP)
            newIm.setPixel(col,row,newPixel)
    newIm.setPosition(width + 1,0)
    newIm.draw(Win)

white("butterfly.gif")
