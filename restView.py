import sys
import requests
from PyQt6 import QtWidgets, uic

from PyQt6.QtWidgets import QMainWindow


import restController

class View(QMainWindow):
    """
    View Klasse für das Language Programm
    """
    def __init__(self, c: restController):
        """
        Konstruktor der View Klasse, lädt das ui file & initialisiert die Buttons
        """
        super().__init__()

        # Lädt das ui file
        uic.loadUi("gui.ui", self)
        self.setWindowTitle("Language Detection - Gioia Frolik")


        self.resultTxt.setReadOnly(True)      # Ergebnisfeld soll nicht editierbar sein
        self.inputTxt.setReadOnly(False)      # Eingabe soll editierbar sein
            

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
        #text = self.inputTxt.toPlainText().strip()
        # print(f"DEBUG: Eingabetext = '{text}'")  # <-- Debugging
        #return text
        return self.inputTxt.toPlainText().strip() # stripe entfernt alle Zeilenumbrüche & Leerzeichen am Anfang / Ende

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
                f"Language: <b>{result['language']}</b><br>"
                f"Short Code: <b>{result['short']}</b><br>"
                f"Propability: <b>{result['prob']}%</b><br>"
                f"Reliable: <b>{reliable}</b>"
            )
            self.resultTxt.setHtml(text)

    def reset_all(self):
        """
        Resetet alle Felder
        """
        self.inputTxt.clear()
        self.resultTxt.clear()

