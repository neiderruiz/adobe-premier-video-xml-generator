import os
import time
from moviepy.editor import VideoFileClip
import librosa
import librosa.display
from modules import actions
from tkinter import messagebox
import urllib.parse

def getTimeEnd(y, sr)-> tuple[tuple,int]:
    inner = 0
    corteArr = []
    for time in y[::-1]:
        corteArr.append(time)
        if time != 0.0 and inner == 0:
            inner = inner + 1
            endCorte = float(len(corteArr) / sr)
            return [corteArr, endCorte]


def getTimeStart(y, sr) ->  tuple[list, int]:
    l = 0
    inner = 0
    corteArrStart = []
    startCorte = 0
    tik = 254016000000

    for time in y:
        l = l + 1
        corteArrStart.append(time)
        if time != 0.0 and inner == 0:
            inner = inner + 1
            startCorte = float(len(corteArrStart) / sr)
            return [corteArrStart,startCorte]


def fill_template(template: str,newTemplate: str, values: tuple):
    for line in template.readlines():
        if '{{name-video}}' in line:
            name = line.replace('{{name-video}}', values.get('videoName'))
            newTemplate.write(name)
        elif '{{pathVideo}}' in line:
            name = line.replace('{{pathVideo}}', values.get('routeVideo'))
            newTemplate.write(name)
        elif '{{pathAudio}}' in line:
            name = line.replace('{{pathAudio}}', values.get('routeAudio'))
            newTemplate.write(name)
        elif '{{tickStart}}' in line:
            name = line.replace('{{tickStart}}', values.get('startFrame'))
            newTemplate.write(f"{name}")
        elif '{{tickStartAudio}}' in line:
            name = line.replace('{{tickStartAudio}}', values.get('tiksStart'))
            newTemplate.write(f"{name}")
        elif '{{miniatureScale}}' in line:
            name = line.replace('{{miniatureScale}}', values.get('miniatureScale'))
            newTemplate.write(name)
        elif '{{miniatureHorizontalPosition}}' in line:
            name = line.replace('{{miniatureHorizontalPosition}}', values.get('miniatureHorizontalPosition'))
            newTemplate.write(name)
        elif '{{miniatureVerticalPosition}}' in line:
            name = line.replace('{{miniatureVerticalPosition}}', values.get('miniatureVerticalPosition'))
            newTemplate.write(name)
        elif '{{miniatureLeftCutPercentage}}' in line:
            name = line.replace('{{miniatureLeftCutPercentage}}', values.get('miniatureLeftCutPercentage'))
            newTemplate.write(name)
        elif '{{miniarureRightCutPercentage}}' in line:
            name = line.replace('{{miniarureRightCutPercentage}}', values.get('miniarureRightCutPercentage'))
            newTemplate.write(name)
        elif '{{endCorte}}' in line:
            name = line.replace('{{endCorte}}', values.get('endCorte'))
            newTemplate.write(name)
        else:
            newTemplate.write(line)
    return True

def edit_video(newVideo: str, nameProject: str, loading,  miniature: dict = None):
    if newVideo == '':
        messagebox.showerror('Error', 'Selecciona un archivo')
        return
    if nameProject == '':
        messagebox.showerror('Error', 'Ingresar nombre de proyecto')
        return
    nameProject = nameProject.lower().replace(' ', '-')
    nameFolder = f"projects/{nameProject}"
    if os.path.isdir(nameFolder) is not True:
        os.makedirs(nameFolder.lower())

    loading.set('procesando...')

    templateAdobe = open('./base.xml')
    nameFileXml = f"./{nameFolder}/{nameProject}.xml"
    ourputAdobe = open(nameFileXml, 'w')
    video = VideoFileClip(newVideo)
    nameAudio = f"./{nameFolder}/{nameProject}.mp3"
    video.audio.write_audiofile(nameAudio)

    duration = video.duration * 60
    videoName = video.filename
    routeVideo = "file://localhost" + urllib.parse.quote(os.path.abspath(videoName))
        
    nameAudio = f"./{nameFolder}/{nameProject}.mp3"
    video.audio.write_audiofile(nameAudio)
    routeAudio = "file://localhost" + urllib.parse.quote(os.path.abspath(nameAudio))


    # routeProject.set(os.path.realpath(nameFolder))

    y, sr = librosa.load(nameAudio)

    tik = 254016000000
    corteArrStart, startCorte = actions.getTimeStart(y, sr)
    corteArrEnd, endCorte = actions.getTimeEnd(y, sr)

    startFrame = float(len(corteArrStart) / sr) * 60
    tiksStart = float(startCorte * tik)
    tiksAudioEnd = float(endCorte * tik) - tiksStart
    endCorte = ((len(y) - (len(corteArrEnd) + len(corteArrStart))) / sr) * 60

    values = {
        "videoName": videoName,
        "routeVideo": routeVideo,
        "routeAudio": routeAudio,
        "startFrame": f"{startFrame}",
        "tiksStart": f"{tiksStart}",
        "endCorte": f"{endCorte}",
        "miniatureScale": miniature.get('scale'),
        "miniarureRightCutPercentage": miniature.get('right_cut_percentage'),
        "miniatureLeftCutPercentage": miniature.get('left_cut_percentage'),
        "miniatureVerticalPosition": miniature.get('vertical_position'),
        "miniatureHorizontalPosition": miniature.get('horizontal_position'),
    }
    finish = actions.fill_template(templateAdobe, ourputAdobe, values)
    if finish:
        loading.set('terminado')
        messagebox.showinfo('Correcto', 'Configuracion de proyecto terminada')