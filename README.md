# common-language-detection-service-Gi0ia

Implementation of a simple RESTful-Webservice w/ GUI Client, to detect language.

Webservice: http://127.0.0.1:500
-> GET-Parameter

call to service
http://127.0.0.1:5000/lg?id="text to search"

*Format of the JSON Object*

```JSON
{
    reliable (boolean): reliability
    language (string): found language full name
    short (string): found language short name
    prob (float): probability in percent (xxx.xx)
}
```
usage of:
- flask
- langdetect
- iso-639


## Requirements Client
- get Languages via webservice
- make response python usable
- prepare Data for GUI

## Requirements MVC
- Model (RESTful Client) Connection to Webservice, get solution of language detection, carefully tested in main
- View (PyQt)
- Controller (function of buttons), provide View w/ Data from Model

## Requirements GUI
- Client returnd result in textfield, result is **bold**
- 3 Buttons:
    - verify
    - reset
    - close
- scaled 


## langdetect
`$ pip install langdetect`
-> https://pypi.org/project/langdetect/

```bash
sudo pacman -S python-pipx
pipx ensurepath
pipx install langdetect

pip install langdetect
```

## iso-639
`pip install iso-639`

`pip install --upgrade setuptools`

