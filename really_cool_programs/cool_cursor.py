import sys
from PyQt6.QtCore import Qt, QSize, QTimer
from PyQt6.QtGui import QBrush, QColor, QPixmap, QPainter, QPen, QScreen, QPainterPath
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QLabel
from pynput.mouse import Listener
from threading import Thread, Event
from time import sleep, time

#Implementation of https://dev.to/uuuuuulala/coding-an-interactive-and-damn-satisfying-cursor-7-simple-steps-2kb-of-code-1c8b
#https://codepen.io/ksenia-k/pen/rNoBgbV
#In python

def start_mousetrigger(stopevent): #Dont try to move the main window around, moving it to different display that it hasnt been started in Causes Segmentation Fault
    def on_move(x, y):
        maxh = main.overlay.geom.height()+main.overlay.geom.top()
        maxw = main.overlay.geom.width()+main.overlay.geom.left()
        if (x in range(0,maxw)) and (y in range (0,maxh)):
            #print(f'x={x} and y={y}')
            main.overlay.cursor_pos["x"] = x-(main.overlay.geom.left()//2)
            main.overlay.cursor_pos["y"] = y-(main.overlay.geom.top()//2)
            main.overlay.mouse_moved_at = time()

            #main.overlay.render()

        if stopevent.is_set():
            mouse_listener.stop()

    mouse_listener = Listener(on_move=on_move)
    mouse_listener.start()


def exitfunc():
    stopevent.set()

class OverlayScreen(QMainWindow):
    def __init__(self, parent=None):
        global stopevent
        super().__init__()
        self.monitors = QScreen.virtualSiblings(self.screen())
        self.geom = QScreen.availableGeometry(self.screen())
        #self.setFixedHeight(self.geom.height())
        #self.setFixedWidth(self.geom.width())
        self.setObjectName("overlay")
        self.setStyleSheet("QMainWindow#overlay {background-color: transparent}") #Slightly visible rgba(0, 0, 0, 125)


        ##############
        ###Settings###
        ##############
        # Base
        self.interval = 10 #Controls how quickly it updates, higher values are less heavy on the device but it looks laggy and lower values are smoother but heavier on the device
        self.spring = 0.4 #Controls Movement
        self.pointsNumber = 40 #Length of the line
        self.friction = 0.5 #Controls Movement
        self.baseWidth = 0.5 #Size of the line

        #Coloring - Control the color of the line with rgb coloring   0 is Min   255 is Max
        self.red = 0
        self.green = 0
        self.blue = 0
        self.transparency = 255 #Lower is more transparent , Higher is less transparent   0 Is Invisible   255 Is No Transparency

        #Downsizing - transparency doesnt work very well with this
        self.downsize = True #The line gets gradually smaller
        self.colorchange = False #Subtracts or adds color per draw , this can result in some cool looking lines
        self.colorchange_settings = {"red":"+", "green":"", "blue":"-"} #+ is add   - is subtract   Empty is dont change at all
        self.colorchange_multiplier = 20 #By how much does it increase/decrease the colors


        self.draw_pos = {"x":0, "y":0}
        self.cursor_pos = {"x":0, "y":0}
        self.mouse_moved_at = None
        self.trails = [{"x": self.cursor_pos["x"], "y": self.cursor_pos["y"], "dx": 0, "dy": 0} for point in range(self.pointsNumber)]


        self.label = QLabel()

        self.canvas = QPixmap(QSize(self.geom.width(),self.geom.height()))
        self.canvas.fill(QColor("#1c460001"))

        self.pen = QPen()
        self.pen.setStyle(Qt.PenStyle.SolidLine)
        self.pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        self.pen.setJoinStyle(Qt.PenJoinStyle.RoundJoin)

        self.brush = QBrush()
        self.brush.setColor(QColor("transparent"))
        self.brush.setStyle(Qt.BrushStyle.SolidPattern)

        self.setCentralWidget(self.label)


        self.render_timer = QTimer()
        self.render_timer.timeout.connect(self.render)
        self.render_timer.setInterval(self.interval)
        self.render_timer.start()
        Thread(target = start_mousetrigger, args=(stopevent,)).start()

    def render(self):
        if self.mouse_moved_at != None:
            if time() - self.mouse_moved_at < 0.2*self.interval:
                self.canvas.fill(QColor("transparent"))
                painter = QPainter(self.canvas)
                painter.setPen(self.pen)
                painter.setBrush(self.brush)

                self.pen.setWidth(int(15* self.baseWidth))
                self.pen.setColor(QColor(self.red, self.green, self.blue, self.transparency))
                for i,trail in enumerate(self.trails):
                    prev = self.cursor_pos if i == 0 else self.trails[i-1]
                    spring = 0.4 * self.spring if i == 0 else self.spring

                    trail["dx"] += (prev["x"] - trail["x"]) * spring
                    trail["dy"] += (prev["y"] - trail["y"]) * spring
                    trail["dx"] *= self.friction
                    trail["dy"] *= self.friction

                    trail["x"] += trail["dx"]
                    trail["y"] += trail["dy"]

                    if i == 0:
                        line_path = QPainterPath()
                        line_path.fillRule()
                        line_path.moveTo(trail["x"], trail["y"])
                    #else:
                    #    line_path.lineTo(int(trail["x"]), int(trail["y"]))
                for i,trail in enumerate(self.trails[:-1]):
                    xc = 0.5 * (trail["x"] + self.trails[i+1]["x"])
                    yc = 0.5 * (trail["y"] + self.trails[i+1]["y"])
                    line_path.quadTo(trail["x"], trail["y"], xc, yc)

                    if self.downsize:
                        self.pen.setWidth(int(self.baseWidth * (self.pointsNumber - i)))

                        if self.colorchange:
                            color_range = [col for col in range(0,256)]
                            color_value = int(self.colorchange_multiplier * (self.pointsNumber - i))

                            custom_red = color_range[(self.red + color_value) % len(color_range)] if self.colorchange_settings["red"] == "+" else color_range[(self.red - color_value) % len(color_range)] if self.colorchange_settings["red"] == "-" else self.red
                            custom_green = color_range[(self.green + color_value) % len(color_range)] if self.colorchange_settings["green"] == "+" else color_range[(self.green - color_value) % len(color_range)] if self.colorchange_settings["green"] == "-" else self.green
                            custom_blue = color_range[(self.blue + color_value) % len(color_range)] if self.colorchange_settings["blue"] == "+" else color_range[(self.blue - color_value) % len(color_range)]  if self.colorchange_settings["blue"] == "-" else self.blue
                            self.pen.setColor(QColor(custom_red, custom_green, custom_blue, self.transparency))

                        painter.setPen(self.pen)
                        painter.drawPath(line_path)

                line_path.lineTo(self.trails[-1]["x"], self.trails[-1]["y"])
                painter.drawPath(line_path)

                painter.drawPath(line_path)
                painter.end()
                self.label.setPixmap(self.canvas)

class Mainwindow(QStackedWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setFixedHeight(500)
        self.setFixedWidth(600)
        self.setStyleSheet("QMainWindow#overlay {background-color: rgba(0, 0, 0, 125)}")
        self.move(0, 0)
        self.overlay = OverlayScreen()
        self.addWidget(self.overlay)
        #self.show()
        self.showFullScreen()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(exitfunc)

    stopevent = Event()
    main = Mainwindow()

    sys.exit(app.exec())


