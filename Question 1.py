from cImage import Pixel
from cImage import EmptyImage
from cImage import ImageWin
import math


def Circle():

    win = ImageWin(700,700)
    img = EmptyImage(700,700)
    RadValue=[math.radians(i) for i in range(361)]
    x_list=[int(math.cos(i)*100) for i in RadValue]
    y_list=[int(math.sin(i)*100) for i in RadValue]
    pixel = Pixel(0,0,255)
    for i in range(len(x_list)):
        x = x_list[i]+ 340
        y = y_list[i]+ 340
        img.setPixel(x,y,pixel)
    img.draw(win)
    
Circle()
