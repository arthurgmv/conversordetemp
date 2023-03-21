# Por Arthur Gabriel https://github.com/arthurgmv
import PySimpleGUI as sg
from PySimpleGUI import tkinter
sg.theme('DarkBlue3')


layout = [
    [sg.Text('Conversor de Temperatura', font=('Helvetica', 20), justification='center')],
    [sg.Text('Informe a temperatura em ºC:'), sg.InputText(key='temp_celsius')],
    [sg.Text('Informe a temperatura em ºF:'), sg.InputText(key='temp_fahrenheit')],
    [sg.Button('Converter'), sg.Button('Sair')],
    [sg.Text(size=(50,1), key='output', font=('Helvetica', 16), justification='center')]
]


window = sg.Window('Conversor de Temperatura', layout)


while True:
    event, values = window.read() 

    if event == sg.WINDOW_CLOSED or event == 'Sair': 
        break

 
    if event == 'Converter':
        try:
            if values['temp_celsius']:
                temp_celsius = float(values['temp_celsius']) 
                temp_fahrenheit = ((9 * temp_celsius) / 5) + 32 
                window['output'].update(f'{temp_celsius}ºC em Fahrenheit é {temp_fahrenheit:.2f}') 
            elif values['temp_fahrenheit']:
                temp_fahrenheit = float(values['temp_fahrenheit'])
                temp_celsius = (temp_fahrenheit - 32) * 5 / 9
                window['output'].update(f'{temp_fahrenheit}ºF em Celsius é {temp_celsius:.2f}')
            else:
                raise ValueError
        except ValueError:
            sg.popup('Erro: insira uma temperatura válida!') 


window.close()
