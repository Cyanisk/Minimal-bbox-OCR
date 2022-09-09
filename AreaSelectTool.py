from PyQt5.QtWidgets import QSplashScreen, QRubberBand
from PyQt5.QtCore import Qt, QRect, QSize, pyqtSignal, QPoint
from PyQt5.QtGui import QPixmap, QGuiApplication

class AreaSelectTool(QSplashScreen):
    
    gotResult = pyqtSignal(int)
    screen_idx = None
    localPos = None
    globalPos1 = None
    globalPos2 = None
    selection_started = False
    
    def __init__(self, screen_idx):
        # Paint the splash screen so it fits the selected screen
        self.screen_idx = screen_idx
        screen = QGuiApplication.screens()[self.screen_idx]
        size = screen.size()
        pixmap = QPixmap(size)
        pixmap.fill(Qt.black)
        
        # Apply the splash screen
        super().__init__(screen, pixmap)
        self.setWindowState(Qt.WindowFullScreen)
        self.setWindowOpacity(0.5)
        message = 'Drag with left mouse button to select an area\n' +\
            'Press Right or Left key to change screen\n' +\
            'Press Esc key to return'
        self.showMessage(message, alignment=Qt.AlignCenter, color=Qt.white)
        
        # Define the selection box
        self.rubberband = QRubberBand(QRubberBand.Rectangle, self)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.selection_started = True
            self.globalPos1 = event.globalPos()
            self.localPos = event.pos()
            
            self.rubberband.setGeometry(QRect(self.localPos, QSize()))
            self.rubberband.show()
    
    def mouseMoveEvent(self, event):
        if self.selection_started:
            upper_left = QPoint(min(self.localPos.x(), event.pos().x()),
                                min(self.localPos.y(), event.pos().y()))
            lower_right = QPoint(max(self.localPos.x(), event.pos().x()),
                                 max(self.localPos.y(), event.pos().y()))
            self.rubberband.setGeometry(QRect(upper_left, lower_right))
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.globalPos2 = event.globalPos()
            self.gotResult.emit(0)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.gotResult.emit(None)
            
        if not self.selection_started:
            if event.key() == Qt.Key_Left:
                self.gotResult.emit(-1)
            elif event.key() == Qt.Key_Right:
                self.gotResult.emit(1)