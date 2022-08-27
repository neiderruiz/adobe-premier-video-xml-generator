from logging import PlaceHolder
import os
from itertools import count
import librosa
import librosa.display
import matplotlib.pyplot as plt
from moviepy.editor import VideoFileClip
import tkinter
from tkinter import StringVar, ttk, filedialog as fd, simpledialog, messagebox
from modules import actions
# filename = librosa.util.example('brahms')
import threading

import time

root = tkinter.Tk()
nameFile = StringVar()
loading = StringVar()
routeProject = StringVar()

def editVideo(newVideo: str, nameProject: str,loading):
    if newVideo == '':
        messagebox.showerror('Error', 'Selecciona un archivo')
        return
    if nameProject == '':
        messagebox.showerror('Error', 'Ingresar nombre de proyecto')
        return
    nameProject = nameProject.lower().replace(' ','-')
    nameFolder = f"projects/{nameProject}"
    if os.path.isdir(nameFolder) is not True:
        os.makedirs(nameFolder.lower())


    loading.set('procesando...')
    

    templateAdobe = open('./base.xml')
    nameFileXml =f"./{nameFolder}/{nameProject}.xml"
    ourputAdobe = open(nameFileXml, 'w')
    video = VideoFileClip(newVideo)
    nameAudio = f"./{nameFolder}/{nameProject}.mp3"
    video.audio.write_audiofile(nameAudio)

    duration = video.duration * 60
    videoName = video.filename
    baseVideo = os.path.realpath(videoName).replace('\\', '/').split(':')
    routeVideo = f"file://localhost/{baseVideo[0]}%3a{baseVideo[1]}"
    baseAudio = os.path.realpath(nameAudio).replace('\\', '/').split(':')
    routeAudio = f"file://localhost/{baseAudio[0]}%3a{baseAudio[1]}"
    routeProject.set(os.path.realpath(nameFolder))

    y, sr = librosa.load(nameAudio)

    tik = 254016000000
    corteArrStart, startCorte = actions.getTimeStart(y, sr)
    corteArrEnd, endCorte = actions.getTimeEnd(y, sr)

    startFrame = float(len(corteArrStart) / sr) * 60
    tiksStart = float(startCorte * tik)
    tiksAudioEnd = float(endCorte * tik) - tiksStart
    endCorte = ((len(y) - (len(corteArrEnd) + len(corteArrStart))) / sr) * 60

    values = {"videoName": videoName, "routeVideo": routeVideo, "routeAudio": routeAudio,
              "startFrame": f"{startFrame}", "tiksStart": f"{tiksStart}", "endCorte": f"{endCorte}"}
    finish = actions.fillTemplate(templateAdobe, ourputAdobe, values)
    if finish:
        print('terminate')
        loading.set('terminado')
        messagebox.showinfo('Correcto', 'Configuracion de proyecto terminada')
        # time.sleep(5)
        # loading.set('')



frm = ttk.Frame(root, padding=10, width=300, height=400)
frm.grid()
root.title('Convert Premier')
style = ttk.Style()

style.configure('TButton', font=('calibri', 10, 'bold', ),
                )

style.map('TButton', foreground=[('active', '!disabled', 'green')],
          background=[('active', 'black')])


def SelectFile():
    filename = fd.askopenfilename(filetypes=filetypes)
    nameFile.set(filename)


nameProject = ttk.Entry(frm, width=80)
nameProject.grid(column=0, row=1)
urlProject = ttk.Entry(frm, width=80, textvariable=routeProject)
urlProject.grid(column=0, row=8)

ttk.Label(frm, text='Nombre del proyecto').grid(column=0, row=0)
ttk.Button(frm, text="Select File", command=SelectFile).grid(column=0, row=2)
label = ttk.Label(root, textvariable=nameFile).grid(column=0, row=3)
ttk.Button(frm, text="Procesar Video",  command=lambda: editVideo(
    nameFile.get(), nameProject.get(), loading),   style='TButton').grid(column=0, row=4)
filetypes = (
    ('videos', '*.mp4'),
    ('All files', '*.*')
)

root.mainloop()
