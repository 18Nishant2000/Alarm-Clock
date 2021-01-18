from datetime import datetime
from playsound import playsound


def form(mode):
    
    if mode == '12':
        h_form = '%I'
        mess = 'Enter time of alerting in (HH:MM:SS AM/PM) format: '
    else:
        h_form = '%H'
        mess = 'Enter time of alerting in (HH:MM:SS) format: '
    
    return (mess, h_form)
    

def cal(text, mode):    
    
    text = text.split(':')
    
    if mode == '%I':
        hours = text[0]
        mins = text[1]
        secs = text[2].split(' ')[0]
        per = text[2].split(' ')[1].upper()
        return (hours, mins, secs, per)
    
    hours = text[0]
    mins = text[1]
    secs = text[2]
    return (hours, mins, secs)

try:
    mode = input('Enter time format in which you want to enter time (12 or 24): ')
    result = form(mode)
    text = input(result[0])
    cal_result = cal(text, result[1])
except:
    print('Enter the time format correctly...')


while True:
    current = datetime.now()
    c_hours = current.strftime(result[1])
    c_mins = current.strftime('%M')
    c_secs = current.strftime('%S')

    if cal_result[0] == c_hours and cal_result[1] == c_mins and cal_result[2] == c_secs:
        if len(cal_result) == 4:
            if cal_result[3] == current.strftime('%p'):
                playsound('Assets/audio.wav')
                break
            else:
                continue
        playsound('Assets/audio.wav')
        break

