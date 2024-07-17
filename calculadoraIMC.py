import PySimpleGUI as sg

# Calcular IMC
def calcular_imc(window, values):
    
    while True:
        
        try:
            
            peso = float(values['peso'])
            
            altura = float(values['altura'])
            
            imc = round(peso / (altura**2), 2)
            
            return imc
            
        except:
            
            mostrar_erro()
            
            window['peso'].update('')
            
            window['altura'].update('')
            
            break

# Mostrar popup de erro
def mostrar_erro():
    
    sg.popup('''
        Digite apenas números
        Coloque o ponto(.)
        no lugar da vírgula(,)
    ''')

# Obter diagnóstico e cor do texto
def obter_diagnostico_e_cor(imc):
    
    if imc < 17:
        
        return 'Muito abaixo do peso', 'white'
        
    elif 18.5 > imc >= 17:
        
        return 'Abaixo do peso', 'lightblue'
        
    elif 25 > imc >= 18.5:
        
        return 'Normal', 'green'
        
    elif 30 > imc >= 25:
        
        return 'Acima do peso', 'yellow'
        
    elif 35 > imc >= 30:
        
        return 'Obesidade I', 'orange'
        
    elif 40 > imc >= 35:
        
        return 'Obesidade II (Severa)', 'red'
        
    else:
        
        return 'Obesidade III (Mórbida)', 'darkred'

# Criar janela
def criar_janela():
    
    sg.theme('Black')
    
    layout = [
        [sg.Text('Digite seu peso (Kg)')],
        [sg.Input(key='peso')],
        [sg.Text('Digite sua altura (m)')],
        [sg.Input(key='altura')],
        [sg.Button(button_text='Calcular')],
        [sg.Text(key='imc')],
        [sg.Text(key='diagnostico')]
    ]
    
    return sg.Window('Calculadora de IMC', layout=layout)

# Executar código
def main():
    window = criar_janela()

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
            
        elif event == 'Calcular':
            
            imc = calcular_imc(window, values)
            
            if imc:
                
                diagnostico, text_color = obter_diagnostico_e_cor(imc)
                
                window['imc'].update(imc)
                
                window['imc'].update(text_color=text_color)
                
                window['diagnostico'].update(diagnostico)
                
                window['diagnostico'].update(text_color=text_color)

if __name__ == '__main__':
    
    main()

            
