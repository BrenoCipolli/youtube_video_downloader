import pytube
import PySimpleGUI as sg

tema = sg.theme('Reddit')
layout = [
    [sg.Text('youtube video downloader',font='Roboto',size=(15,0),justification='right')],
    [sg.Text('o',text_color='white')],
    [sg.Text('Digite o link abaixo:')],
    [sg.Input(key='url')],
    [sg.Button('Download',key='btn')],
]
janela = sg.Window('youtube',layout,size=(250,350))
while True:
    event,values = janela.Read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'btn':
        yt = pytube.YouTube(values['url'])
        video = yt.streams.first()
        video.download()



janela.close()