print("""
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗    ██╗███╗░░██╗  
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝    ██║████╗░██║  
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░    ██║██╔██╗██║  
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░    ██║██║╚████║  
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗    ██║██║░╚███║  
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝    ╚═╝╚═╝░░╚══╝  

████████╗░█████╗░░░░░░░██████╗░░█████╗░  ██╗░░░░░██╗░██████╗████████╗
╚══██╔══╝██╔══██╗░░░░░░██╔══██╗██╔══██╗  ██║░░░░░██║██╔════╝╚══██╔══╝
░░░██║░░░██║░░██║█████╗██║░░██║██║░░██║  ██║░░░░░██║╚█████╗░░░░██║░░░
░░░██║░░░██║░░██║╚════╝██║░░██║██║░░██║  ██║░░░░░██║░╚═══██╗░░░██║░░░
░░░██║░░░╚█████╔╝░░░░░░██████╔╝╚█████╔╝  ███████╗██║██████╔╝░░░██║░░░
░░░╚═╝░░░░╚════╝░░░░░░░╚═════╝░░╚════╝░  ╚══════╝╚═╝╚═════╝░░░░╚═╝░░░

█▀▄▀█ ▄▀█ █▀▄ █▀▀   █▄▄ █▄█   █▀ ▄▀█ █▀▄▀█ █░█ █▀▀ █░░   █▀█ ▄▀█ █░░ █░█ █▄▄ ▄▀█   ▀ █▀▄   ▄▀ █▀▀ ▀▄   ▀█ █▀█ ▀█ ▀█
█░▀░█ █▀█ █▄▀ ██▄   █▄█ ░█░   ▄█ █▀█ █░▀░█ █▄█ ██▄ █▄▄   █▀▀ █▀█ █▄▄ █▄█ █▄█ █▀█   ▄ █▄▀   ▀▄ █▄▄ ▄▀   █▄ █▄█ █▄ █▄
""")
import webbrowser
import os
import sys
import time
import random

def DoOpenFile():
  print("Open File")
  print("This function is not ready yet!!!")

def DoNewFile():
  print("New File")
  print("This function is not ready yet!!!")

def DoQuickDefault():
  print("Quick Default")
  print("This function is not ready yet!!!")

def DoSettings():
  print("Settings")
  print("This function is not ready yet!!!")

def DoHelp():
  print("Help")
  
def DoGitHub():
  print("GitHub")
  webbrowser.open('https://github.com/SamuelPalubaCZ')

def ShowMenu(typ = "Full"):
  if typ in ["Full", "full", "FULL", 1]:
    print("""1.Open File 🚪
2.New File 🆕
3.Quick Default ⏩
4.Settings⚙️
5.Help 🆘
6.Show my GitHub Profile 👀""")
  elif typ in ["Lite", "lite", "LITE"]:
    print("""1.Open File 🚪
2.New File 🆕
3.Quick Default ⏩
4.Settings⚙️
""")
  else:
    print("Daum asi jsem udělal bug nebo jsi blbě zadal info!!! Pokus se restartovat program a pokud problém přetrvává udělej mi report na GitHub!!!")
  print("\n")
  select = input("Give me number of your select❗\n")
  return select
select1 = "6"

kex = input("LOL\n")
select1 = ShowMenu(kex)
DoActions(select1)

  
def DoExit():
  print("Exit")
  exit(69)

  op = ShowMenu()
  DoActions(op)