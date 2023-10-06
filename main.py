# COMANDOS
# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar uma tecla
# pyautogui.hotkey -> atalho (combinação de teclas)

import pyautogui
import time
import pandas as pd

# PASSO 1: ENTRANDO NO SITE DA EMPRESA
# EX: https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.PAUSE = 0.4

#abrindo o chrome    
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#entrando no link/sistema
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)  
pyautogui.press("enter")
    
#esperando o site carregar
time.sleep(3)

# PASSO 2: FAZER LOGIN

pyautogui.click(x=542, y=395)
pyautogui.write("automacao@gmail.com")

pyautogui.press("tab") #passei para o campo senha
pyautogui.write("automacao1234")

pyautogui.press("tab") #passei para o campo logar
pyautogui.press("enter")

time.sleep(3)

# PASSO 3: IMPORTAR A BASE DE DADOS DOS PRODUTOS

tabela = pd.read_csv("produtos.csv")

# PASSO 4: CADASTRANDO PRODUTOS

for linha in tabela.index:

    pyautogui.click(x=478, y=286)
        
    #preenchendo cadastro
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
        
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
        
    #enviando cadastro do produto
    pyautogui.press("tab")
    pyautogui.press("enter") 
        
    #voltando ao topo da página
    pyautogui.scroll(50000)