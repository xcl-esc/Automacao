#Passo 1 Entrar no sistema  https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time
pyautogui.PAUSE = 1.5

pyautogui.press('Win')
pyautogui.write('opera')
pyautogui.press('Enter')

time.sleep(3)

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('Enter')

#passo 2 loggar no site 

time.sleep(3)

pyautogui.press('Tab')
pyautogui.write('cleberwagner31@gmail.com')

time.sleep(1.5)

pyautogui.press('Tab')
pyautogui.write('12345')

pyautogui.press('Enter')
time.sleep(3)

#passo 3 importar base de dados
import pandas

tabela = pandas.read_csv('produtos.csv')
print(tabela)
time.sleep(3)

#passo 4 cadastrar um produto

pyautogui.click(x=2016, y=292)


for linha in tabela.index:
    pyautogui.click(x=2016, y=292)
#codigo
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('Tab')

# marca
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('Tab')

# tipo
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('Tab')

# categoria
    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('Tab')

# preco unitario
    preco = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco))
    pyautogui.press('Tab')

# custo
    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('Tab')

    time.sleep(0.5)
 # obs
 # nan = Not a Number = vazio
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press('Tab')

# enviar
    pyautogui.press('Enter')
    time.sleep(1)
    pyautogui.scroll(5000)
    


#passo5  repetir o processo até acabarem os produtos disponíveis para cadastrar