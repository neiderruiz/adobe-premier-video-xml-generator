# adobe-premier-video-xml-generator

## Description

- convert a video recorded with the following dimensions 3840 × 1080 and convert it into an xml configured for adobe premier

- add a thumbnail layer to the right side of your video

<img width="500" alt="image" src="https://github.com/neiderruiz/adobe-premier-video-xml-generator/assets/57574910/e1854882-806d-4482-af66-5de99ceac21c">

- adds a layer with the 1920 x 1080 screen display

<img width="500" alt="image" src="https://github.com/neiderruiz/adobe-premier-video-xml-generator/assets/57574910/1515e765-c887-4ea5-85f0-6418bd229dc2">

- Add another layer in which you see yourself in full screen

<img width="500" alt="image" src="https://github.com/neiderruiz/adobe-premier-video-xml-generator/assets/57574910/0eac4c5f-a9ad-440f-91ba-fceb7557cbbe">

# Windows | MacOs

## View start Windows

<img width="400" src="https://github.com/neiderruiz/adobe-premier-video-xml-generator/assets/57574910/65687eac-e32f-42b9-98e3-ffb774cd49ab">

## Config miniature

<img width="400" src="https://github.com/neiderruiz/adobe-premier-video-xml-generator/assets/57574910/042ad506-f10e-4485-ae6d-f39e046abf3b">


## Result adobe premier

<img width="500" src="https://github.com/neiderruiz/adobe-premier-video-xml-generator/assets/57574910/bb579cc6-0922-4563-bf56-5f95fc0b246f" />

## how install Windows

*  clone project

```bash
git clone https://github.com/neiderruiz/adobe-premier-video-xml-generator.git
```

```bash
cd adobe-premier-video-xml-generator
```

- make environment

```bash
python -m venv env
```

- activate environment
```bash
env\Scripts\activate
```

* Install requirements

```bash
pip install -r requirements.txt
```

- run project

```
python main.py
```

## make executable .exe

- run command

```bash
 pyinstaller main.spec
```

- A **dist** folder and another **build** folder will be created

- Enter **dist/main** and you will find a main.exe file which you can run by clicking on the



# how install MacOs

```bash
git clone https://github.com/neiderruiz/adobe-premier-video-xml-generator.git
```

```bash
cd adobe-premier-video-xml-generator
```

- Mac chip m1 | m2

```bash
brew uninstall tcl-tk
```

```bash
brew install tcl-tk
```

- admin versions python

```bash
brew install pyenv
```
- we will use python 3.10.6
```bash
pyenv install 3.10.6
```

- create enviroment

```bash
python -m venv env
```

```bash
source env/bin/activate
```

- install requirements

```bash
pip install -r requirements.txt
```


- run project

```bash
python main.py
```

- make executable

```bash
pyinstaller main.py
```

