# Gaphics 9/23/21

```python
import graphics # on MuOnline
#                                w    h
myWin = grpahics.GraphicsWindow(300, 300)
myCanvas = myWin.Canvas()

#                      x   y   w   h
myCanvas.drawRectangle(10, 10, 30, 140)
# can use a RGB value too
myCanvas.setColor("Red")

myWin.wait()
```

- creates a graphic window with WxH of 300
- draws a rectangle that starts at x:10 y:10 and then draws a red 30x140 rectangle on the canvas 
    - colors could be different because all people read RGB values much differently 
        - 1 bit per pixel for 1 color display
        - modern is 24 bit per pixel 

        - 1 bit is black and white 
        - 8 bit is simple colors
        - 16 bit is shading and complex colors 