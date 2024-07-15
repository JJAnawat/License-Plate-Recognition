import easyocr
import constants

class EasyOCR():
    def __init__(self):
        self.reader = easyocr.Reader(["th"])
    def readText(self,path):
        results = self.reader.readtext(path)

        ret = []
        for result in results:
            if(result[2] >= constants.OCR_CONF_THRESHOLD):
                ret.append(result)

        return ret