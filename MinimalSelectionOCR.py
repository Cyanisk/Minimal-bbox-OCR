import sys
import pytesseract
from PIL import ImageGrab
from pynput import mouse
import pyperclip

from MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer, Qt

# Requires
# - Tesseract (sudo apt install tesseract-ocr)
# - Tesseract training data (from website)
# - xclip (sudo apt install xclip)

#TODO: Can we visualize the bbox?
#TODO: Would be cool to make it a webapp instead


def get_bbox(point1, point2):
    x1 = min(point1[0], point2[0])
    y1 = min(point1[1], point2[1])
    x2 = max(point1[0], point2[0])
    y2 = max(point1[1], point2[1])
    return (x1,y1,x2,y2)

def perform_ocr(bbox, config, lang):
    image = ImageGrab.grab(bbox)
    return pytesseract.image_to_string(image, config=config, lang=lang)

class MinimalOCR(QMainWindow):
    
    point1 = None
    point2 = None
    bbox = None
    is_using_clipboard = True
    config = r'-c preserve_interword_spaces=1 --psm 4'
    lang = 'jpn'
    
    def __init__(self):
        
        # Setup GUI
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Minimal-bbox-OCR')
        self.ui.textEdit_result.setAlignment(Qt.AlignVCenter)
        
        # Setup events
        self.ui.radioButton_auto.toggled.connect(self.change_scanning_mode)
        self.ui.checkBox_clipboard.stateChanged.connect(self.toggle_clipboard)
        self.ui.pushButton_selectArea.clicked.connect(self.select_area)
        self.ui.pushButton_overwrite.clicked.connect(self.overwrite)
        self.ui.pushButton_scan.clicked.connect(self.scan)
        self.ui.textEdit_result.textChanged.connect(self.begin_text_edit)
        
        # Setup QTimer
        self.timer = QTimer()
        self.timer.timeout.connect(self.scan)
    
    def change_scanning_mode(self):
        if self.ui.radioButton_auto.isChecked():
            self.ui.pushButton_scan.setEnabled(False)
            self.timer.start(1000)
        else:
            self.timer.stop()
            if self.bbox != None:
                self.ui.pushButton_scan.setEnabled(True)
    
    def toggle_clipboard(self):
        self.is_using_clipboard = self.ui.checkBox_clipboard.isChecked()
            
    def select_area(self):
        self.ui.label_status.setText('Drag the mouse to select an area to scan')
        
        QTimer.singleShot(10, self.start_mouse_listener)
    
    def overwrite(self):
        text = self.ui.textEdit_result.toPlainText()
        pyperclip.copy(text)
    
    def begin_text_edit(self):
        if self.ui.textEdit_result.hasFocus():
            self.ui.radioButton_manu.setChecked(True)
    
    def start_mouse_listener(self):
        # Listen to the mouse in order to define the bounding box
        with mouse.Listener(on_click = self.on_click) as listener:
            listener.join()
        self.bbox = get_bbox(self.point1, self.point2)
        
        if self.ui.radioButton_manu.isChecked():
            self.ui.pushButton_scan.setEnabled(True)
        self.ui.label_status.setText('Scan result:')  
    
    def on_click(self, x, y, button, pressed):
        if pressed:
            self.point1 = (x,y)
        else:
            self.point2 = (x,y)
            return False
        
    def scan(self):
        if self.bbox != None:
            text = perform_ocr(self.bbox, self.config, self.lang)
            
            if text == self.ui.textEdit_result.toPlainText():
                return
            
            self.ui.textEdit_result.setPlainText(text)
            
            if self.is_using_clipboard:
                pyperclip.copy(text)
    
    def closeEvent(self, event):
        self.timer.stop()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MinimalOCR()
    widget.show()
    app.exec_()
