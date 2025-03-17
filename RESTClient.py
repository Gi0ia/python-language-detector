import requests

class RESTClient:
    BASE_URL = "http://127.0.0.1:5000/lg"

    @staticmethod
    def detect_language(text):
        """
        Sendet den Text zur Spracherkennung an den Server

        Args:
            text (str): der zu überprüfende Text

        Returns:
            JSON | str: The Response as JSON or the error as String
        """

        try:
            response = requests.get(RESTClient.BASE_URL, params={"id": text})
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"Fehler: {response.status_code}"}

        except Exception as e:
            return {"error": strg(e)}

if __name__=="__main__":
    print(RESTClient.detect_language("Ho fame, mio marito?"))