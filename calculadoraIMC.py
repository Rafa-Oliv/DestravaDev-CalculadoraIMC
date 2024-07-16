import PySimpleGUI as sg

sg.theme('Black')

layout =[
    [sg.Text('Digite seu peso(Kg)')],
    [sg.Input(key='peso')],
    [sg.Text('Digite sua altura(m)')],
    [sg.Input(key='altura')],
    [sg.Button(button_text='Calcular')],
    [sg.Text(key='resultado')]
   

    ]

window = sg.Window('Calculadora de IMC',layout=layout)

while True:
    event,values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == 'Calcular':
        print('Calculado')
        print(values)
        try:
            peso = float(values['peso'])
            altura = float(values['altura'])
            imc = round(peso/(altura**2),2)
            if imc < 17:
                resultado = f'''
    IMC = {imc}
    Muito abaixo do peso
    '''
                text_color = 'white'
                
            elif 18.5 > imc >= 17:
                resultado = f'''
    IMC = {imc}
    Abaixo do peso
    '''
                text_color = 'white'
            elif 18.5 > imc >= 17:
                resultado = f'''
    IMC = {imc}
    Abaixo do peso
    '''
                text_color = 'white'

            elif  25 > imc >= 18.5 :
                resultado = f'''
    IMC = {imc}
    Peso Normal
    '''
                text_color = 'green'

            elif 30 > imc >= 25:
                resultado = f'''
    IMC = {imc}
    Acima do peso
    '''
                text_color = 'red'

            elif 35 > imc >= 30:
                resultado = f'''
    IMC = {imc}
    Obesidade I
    '''
                text_color = 'red'
            elif 40 > imc >= 35:
                resultado = f'''
    IMC = {imc}
    Obesidade II(Severa)
    '''
                text_color = 'red'
            else:
                resultado = f'''
    IMC = {imc}
    Obesidade III(Mórbida)
    '''
                text_color='red'
                
            window['resultado'].update(resultado)
            window['resultado'].update(text_color=text_color)
            print(resultado)
        except:
            sg.popup('''
Digite apenas números
coloque o ponto(.)
no lugar da vígula
''')
