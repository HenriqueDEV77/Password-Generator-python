import random 
import PySimpleGUI as sg
import os

class GeSen:
    def __init__(self):
        sg.theme('Black')
        layout = [
            [sg.Text('Site/Software', size=(10,1)),
            sg.Input(key='site'=(20,1))],
            [sg.Text('E-mail/Usuário', size=(10,1), 
            sg.Input(key='usuario', size=(20, 1)))],
        ]
        
    def Iniciar(self):
        pass

    def Salvar_senha(self):
        pass


    gen = GeSen()
    gen.Iniciar()


