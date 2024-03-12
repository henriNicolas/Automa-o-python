# passo a passo do projeto
# passo 1: entrar no sistema da empresa
# passo 2 : fazer login:
# passo 3 : importar a base de dados
# passo 4 : cadastrar 1 produto
# passo 5 : repetir o processo de cadastro até acabar

# https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pyautogui (biblioteca de automação )

# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.write -> escrever um texto
# pyautogui.press -> precionar 1 tecla do teclado
# pyautogui.hotkey('ctrl' , 'v')
# abrir o navegador

import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# dar uma pausa um pouco maior no codigo (3 segundos)

time.sleep(3)

# passo 2: fazer login

pyautogui.click(x=779, y=408)
pyautogui.write("nicolasdailha@gmail.com")

# escrever senha

pyautogui.press("tab")
pyautogui.write("sexo")

# clicar no botao de logar

pyautogui.click(x=945, y=569)
time.sleep(3)

# clicar na primeira barra do formulário
pyautogui.click(x=813, y=284)

# passo 3: importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# PASSO 4 : CADASTRAR 1 PRODUTO
# para cada linha da minha tabela
for linha in tabela.index:
    # codigo do produto
    pyautogui.click(x=813, y=280)
    codigo = tabela.loc[linha, "codigo"]
    # codigo do produto
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # marca do produto
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    # tipo do produto
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # categoria
    # str() string -> texto
    # str(1) -> 1 -> '1'
    # categoria do produto
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # preço unitario do produto
    pyautogui.write(str(tabela.loc[linha, "preco"]))
    pyautogui.press("tab")

    # custo do produto
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    # OBS
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    # enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)

# passo 5 repetir o processo todo
