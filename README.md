# adobe-premier-video-xml-generator

## Description

- convert a video recorded with the following dimensions 3840 × 1080 and convert it into an xml configured for adobe premier

- add a thumbnail layer to the right side of your video

<img width="1425" alt="image" src="https://github.com/neiderruiz/adobe-premier-video-xml-generator/assets/57574910/e1854882-806d-4482-af66-5de99ceac21c">


- adds a layer with the 1920 x 1080 screen display

<img width="1425" alt="image" src="https://github.com/neiderruiz/adobe-premier-video-xml-generator/assets/57574910/1515e765-c887-4ea5-85f0-6418bd229dc2">


- Add another layer in which you see yourself in full screen

<img width="1425" alt="image" src="https://github.com/neiderruiz/adobe-premier-video-xml-generator/assets/57574910/0eac4c5f-a9ad-440f-91ba-fceb7557cbbe">


## View start

![image](https://github.com/neiderruiz/adobe-premier-video-xml-generator/assets/57574910/65687eac-e32f-42b9-98e3-ffb774cd49ab)

## Config miniature

![image](https://github.com/neiderruiz/adobe-premier-video-xml-generator/assets/57574910/042ad506-f10e-4485-ae6d-f39e046abf3b)

## Result adobe premier

![image](https://github.com/neiderruiz/adobe-premier-video-xml-generator/assets/57574910/bb579cc6-0922-4563-bf56-5f95fc0b246f)

## instalación

* ### Clonar repositiorio
```
git clone https://github.com/neiderruiz/adobe-premier-video-xml-generator.git
```
* ### Crear entorno para el proyecto

```
// python menor que 3.10
python -m venv env

// python 3.10
py -m ven env

// activar entorno 

env\Scripts\activate

```

* ### instalar requerimientos

``
pip install -r requirements.txt
``

* ### ejecucion del proyecto

```
py main.py
```
# Generar ejecutable .exe

- ejecutamos el comando

```
 pyinstaller main.spec
```

- se creara una carpeta **dist** y otra **build**

- ingresas a **dist/main** y encontraras un archivo main.exe el cual puedes ejecutar pulsando en el



# run project in macOs

```bash
brew uninstall tcl-tk
```

```bash
brew install tcl-tk
```

```bash
brew install pyenv
```

```bash
pyenv install 3.10.6
```


```bash
pip install virtualenv
```

```bash
virtualenv env --system-site-packages
```

```bash
source env/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
pyinstaller main.py
```

