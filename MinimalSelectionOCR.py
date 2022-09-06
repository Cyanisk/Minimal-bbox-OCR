import pytesseract
from PIL import ImageGrab
from pynput import mouse
import time

# Requires
# - Tesseract (sudo apt install tesseract-ocr)
# - Tesseract training data (from website)


def get_bbox(point1, point2):
    x1 = min(point1[0], point2[0])
    y1 = min(point1[1], point2[1])
    x2 = max(point1[0], point2[0])
    y2 = max(point1[1], point2[1])
    return (x1,y1,x2,y2)

def perform_ocr(bbox, config, lang):
    image = ImageGrab.grab(bbox)
    return pytesseract.image_to_string(image, config=config, lang=lang)

class MinimalOCR():
    
    point1 = (0,0)
    point2 = (0,0)
    bbox = (0,0,0,0)
    current_text = ''
    config = r'-c preserve_interword_spaces=1 --psm 4'
    lang = 'jpn'
    
    def __init__(self):
        print('Select an area to scan for text')
        with mouse.Listener(on_click = self.on_click) as listener:
            listener.join()
        
        self.bbox = get_bbox(self.point1, self.point2)
        
        for i in range(60):
            self.update()
            time.sleep(1)
    
    def on_click(self, x, y, button, pressed):
        if pressed:
            self.point1 = (x,y)
        else:
            self.point2 = (x,y)
            return False
        
    def update(self):
        text = perform_ocr(self.bbox, self.config, self.lang)
        if text != self.current_text:
            print(text)
            self.current_text = text



MinimalOCR()
