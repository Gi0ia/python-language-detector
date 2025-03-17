import sys
import requests
from PyQt6 import QtWidgets, uic

import restController

class View(QMainWindow):
    """
    View Klasse für das Language Programm
    """
    def __init__(self, c: controller):
        """
        Konstruktor der View Klasse, lädt das ui file & initialisiert die Buttons
        """
        super().__init__()

        # Lädt das ui file
        uic.loadUi("gui.ui", self)
        self.setWindowTitle("Language Detection - Gioia Frolik")


        self.resultTxt.setReadOnly(False)    # Eingabe soll editierbar sein
        self.inputTxt.setReadOnly(True)      # Ergebnisfeld soll nicht editierbar sein
            

        # setzten der Button Funktionen
        self.checkB.clicked.connect(c.check)
        self.resetB.clicked.connect(c.reset)
        self.closeB.clicked.connect(c.close)

    def get_intput(self):
        """
        Holt den Text aus dem Input-Feld

        Returns:
            str: der Eingegebene Text
        """
        return self.inputTxt.toPlainText().strip() # entfert Leerzeichen am Anfang/Ende
    
    def set_result(self, result):
        """
        Setzt das Result Text Feld

        Args:
            result (dict): Die Response vom Server als dict
        """
        if "error" in result:
            self.resultTxt.setPlainText(f"Error: {result['error']}")
        else:
            reliable = "Yes" if result['reliable'] else "No"
            text = (
                f"Language: <b>{result['language']}</b>\n"
                f"Short Code: <b>{result['short']}</b>\n"
                f"Propability: <b>{result['prob']}%</b>\n"
                f"Reliable: <b>{reliable}</b>"
            )
            self.resultTxt.setHtml(text)

    def reset_all(self):
        """
        Resetet alle Felder
        """
        self.inputTxt.clear()
        self.resultTxt.clear()

