import PySimpleGUI as sg

#calcumar IMC

def calcular_Imc(window,values):
    
    while True:
        
        try:
            
            peso = float(values['peso'])
            
            altura = float(values['altura'])
            
            imc = round(peso/(altura**2),2)
            
            return imc
        
        except:
            
            sg.popup('''
                Digite apenas números
                Coloque o ponto(.)
                no lugar da vígula(,)
            ''')
            
            window['peso'].update('')

            window['altura'].update('')
            
            break
            
#Definir o diagnóstico
        
def definir_diagnostico(imc):
    
    if imc < 17:
        
        return 'Muito abaixo do peso'
    
    elif 18.5 > imc >= 17:
        
        return 'Abaixo do peso'
    
    elif  25 > imc >= 18.5 :
        
        return 'Normal'
    
    elif 30 > imc >= 25:
        
        return 'Acima do peso'
    
    elif 35 > imc >= 30:
        
        return 'Obesidade I'
    
    elif 40 > imc >= 35:
        
         return 'Obesidade II(Severa)'
        
    else:
        
        return 'Obesidade III(Mórbida)'

#Definir a cor do texto
    
def definir_cor_texto(imc):

    if imc < 18.5:
        
        return 'white'
    
    elif 25 > imc >= 18.5:
        
        return 'green'
    
    else:
        
        return 'red'

#criar_janela
    
def criar_janela():

    sg.theme('Black')

    layout =[
        [sg.Text('Digite seu peso(Kg)')],
        [sg.Input(key='peso')],
        [sg.Text('Digite sua altura(m)')],
        [sg.Input(key='altura')],
        [sg.Button(button_text='Calcular')],
        [sg.Text(key='imc')],
        [sg.Text(key='diagnostico')]
        ]

    return sg.Window('Calculadora de IMC',layout=layout)

#executar código

def main():
    
    window = criar_janela()

    while True:
        
        event,values = window.read()

        if event == sg.WIN_CLOSED:
            
            break
        
        elif event == 'Calcular':
            
            imc = calcular_Imc(window,values)
            
            if imc:
                
                diagnostico = definir_diagnostico(imc)
                
                text_color = definir_cor_texto(imc)
                
                window['imc'].update(imc)
                
                window['imc'].update(text_color=text_color)
                
                window['diagnostico'].update(diagnostico)
                
                window['diagnostico'].update(text_color=text_color)
                
                
 if __name__ == '__main__':
     main()
            
