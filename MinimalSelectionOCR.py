import sys
import pytesseract
from PIL import ImageGrab
import pyperclip

from MainWindow import Ui_MainWindow
from AreaSelectTool import AreaSelectTool
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QGuiApplication

# Requires
# - Tesseract (sudo apt install tesseract-ocr)
# - Tesseract training data (from website)
# - xclip (sudo apt install xclip)

#TODO: Return to auto mode when focus is lost from textarea?
#TODO: Would be cool to make it a webapp instead
#TODO: Pause scanning loop when selecting
#TODO: Fix some text on the main window
#TODO: Write README


def get_bbox(point1, point2):
    x1 = min(point1.x(), point2.x())
    y1 = min(point1.y(), point2.y())
    x2 = max(point1.x(), point2.x())
    y2 = max(point1.y(), point2.y())
    return (x1,y1,x2,y2)

def perform_ocr(bbox, config, lang):
    image = ImageGrab.grab(bbox)
    return pytesseract.image_to_string(image, config=config, lang=lang)

class MinimalOCR(QMainWindow):
    
    screen_idx = 0
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
        
        self.splash = AreaSelectTool(self.screen_idx)
        self.splash.gotResult.connect(self.processAreaSelectResult)
        self.hide()
        self.splash.show()
        self.splash.activateWindow()
    
    def overwrite(self):
        text = self.ui.textEdit_result.toPlainText()
        pyperclip.copy(text)
    
    def begin_text_edit(self):
        if self.ui.textEdit_result.hasFocus():
            self.ui.radioButton_manu.setChecked(True)
    
    def processAreaSelectResult(self, result):
        self.splash.hide()
        self.show()
        point1 = self.splash.globalPos1
        point2 = self.splash.globalPos2
        self.splash.deleteLater()
        
        if result == 0:
            self.bbox = get_bbox(point1, point2)
            
            if self.ui.radioButton_manu.isChecked():
                self.ui.pushButton_scan.setEnabled(True)
            self.ui.label_status.setText('Scan result:')
        elif (result == -1) | (result == 1):
            n_screens = len(QGuiApplication.screens())
            self.screen_idx = (self.screen_idx + result) % n_screens
            self.select_area()
        
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
