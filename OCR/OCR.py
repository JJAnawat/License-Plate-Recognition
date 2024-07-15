import easyocr

class EasyOCR():
    def __init__(self):
        self.reader = easyocr.Reader(["th","en"])
    def readText(self,path):
        result = self.reader.readtext(path,)
        return result