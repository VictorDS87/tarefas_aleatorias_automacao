# Abrir o site 
import webbrowser
import pyautogui
from time import sleep

webbrowser.open_new_tab('https://cursoautomacao.netlify.app/')
# Clicar na pagina para ela ganhar o foco
pyautogui.click(1081,459, duration=1)
# Dar scroll para baixo e clicar no input de name
pyautogui.scroll(-700)
pyautogui.click(1482,547, duration=1)
# Digitar o meu nome e clicar no botão "alert", após isso clicar em "OK" no alert que abrir
pyautogui.typewrite('Victor')
pyautogui.click(1484,579, duration=1)
pyautogui.click(1157,151, duration=1)
# Descer a pagina e clicar para baixar dois arquivos
pyautogui.scroll(-1400)
pyautogui.click(514,243, duration=1)
pyautogui.click(703,256, duration=1)
sleep(1)
# Informar que a tarefa terminou
pyautogui.alert('Terminou')
