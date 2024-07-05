import random
import PySimpleGUI as sg
import os

class GeSen:
    def __init__(self):
        # Layout
        sg.theme('Black')
        layout = [
            [sg.Text('Site/Software', size=(10, 1)), sg.Input(key='site', size=(20, 1))],
            [sg.Text('E-mail/Usuario', size=(10, 1)), sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(range(1, 31)), key='total_chars', default_value=1, size=(3, 1))],
            [sg.Button('Gerar Senha', key='gerar_senha')],
            [sg.Output(size=(32, 5))]
        ]
        # Janela
        self.janela = sg.Window('Password Generator', layout)
    
    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'gerar_senha':
                nova_senha = self.gerar_senha(int(valores['total_chars']))
                print(nova_senha)
                self.Salvar_senha(nova_senha, valores)
    
    def gerar_senha(self, total_chars):
        char_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
        chars = random.choices(char_list, k=total_chars)
        new_pass = ''.join(chars)
        return new_pass

    def Salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a') as arquivo:
            arquivo.write(f"site: {valores['site']}, usuario: {valores['usuario']}, nova senha: {nova_senha}\n")
        print('Senha Gerada.')

if __name__ == "__main__":
    gen = GeSen()
    gen.Iniciar()
