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

def DoActions(typ = select1):
  if typ == "1":
    DoOpenFile()
  elif typ == "2":
    DoNewFile()
  elif typ == "3":
    DoQuickDefault()
  elif typ == "4":
    DoSettings()
  elif typ == "5":
    DoHelp()
  elif typ == "6":
    DoGitHub()
  else:
    print("Daum asi jsem udělal bug nebo jsi blbě zadal info!!! Pokus se restartovat program a pokud problém přetrvává udělej mi report na GitHub!!!")
  op = ShowMenu()
kex = input("LOL\n")
select1 = ShowMenu(kex)
DoActions(select1)
