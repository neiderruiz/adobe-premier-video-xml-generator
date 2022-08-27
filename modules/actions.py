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


def fillTemplate(template: str,newTemplate: str, values: tuple):
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
        elif '{{endCorte}}' in line:
            name = line.replace('{{endCorte}}', values.get('endCorte'))
            newTemplate.write(name)
        else:
            newTemplate.write(line)
    return True