# adobe-premier-video-xml-generator
![image](https://user-images.githubusercontent.com/57574910/187046129-21fef922-1c65-475a-af55-c595021e6840.png)
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
pyinstaller --noconsole '.\main.py'
```

- se creara una carpeta **dist** y otra **build**

- ingresas a **dist/main** y encontraras un archivo main.exe el cual puedes ejecutar pulsando en el


