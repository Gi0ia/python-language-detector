import sys
from PyQt6.QtWidgets import QApplication

from restClient import RESTClient
import restView

class Controller:
    """
    Controller Klasse für das Language Programm
    """
    def __init__(self):
        super().__init__()
        self.view = restView.View(self)
        self.model = RESTClient()


    def check(self):
        """
        Sendet den Text an den Server und Zeigt das Ergebnis an
        """
        input_text = self.view.get_intput()
        if input_text:
            try:
                result = self.model.detect_language(input_text)
                self.view.set_result(result)
            except ValueError as e:
                self.view.set_result({"error": str(e)})
        else:
            self.view.set_result({"error": "No text provided"}) 

    def reset(self):
        """
        Resetet die Felder
        """
        self.view.reset_all()

    def close(self):
        """
        Beendet den Language Detector
        """
        sys.exit()


if __name__=="__main__":
    app = QApplication([])
    c = Controller()
    c.view.show()
    sys.exit(app.exec())