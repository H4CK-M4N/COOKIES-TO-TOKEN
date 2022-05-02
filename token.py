#!/usr/bin/env python3
import requests, time, os, re
# Warna
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
P = ('\x1b[1;97m')
def xoshnaw():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  print("\x1b[37;1mYOUR ID : "+id)
  try:
    httpCaht = requests.get("https://pastebin.com/n08Tdjg5").text
    if id in httpCaht:
      print("\033[1;92mYOUR ID IS ACTIVE...!")
      msg = str(os.geteuid())
      time.sleep(0.3)
      pass
    else:
      print("\x1b[1;91mID ACTIVATE (WhatsApp) INBOX  ")
      os.system('xdg-open https://wa.me/+2349150557103')
      time.sleep(1)
      sys.exit()
  except:
    sys.exit()
    if name == '__main__':
    	print(logo)
    	xoshnaw()
xoshnaw()
# Logo
__logo__ = (f'''
{H}.##.....##.########.##..........###....##....##.####.##....##.{H}
{P}.###...###.##.......##.........##.##...###...##..##..###...##.{P}
{H}.####.####.##.......##........##...##..####..##..##..####..##.{H}
{P}.##.###.##.######...##.......##.....##.##.##.##..##..##.##.##.{P}
{H}.##.....##.##.......##.......#########.##..####..##..##..####.{H}
{P}.##.....##.##.......##.......##.....##.##...###..##..##...###.{P}
{H}.##.....##.########.########.##.....##.##....##.####.##....##.{H}
{H}[ {P}CONVERT COOKIE TO TOKEN {H}]{H}
{H}_________________________{H}     

{P} ®️ Script By Melanin{P} ®️                                  
{H}_________________________{H}
{H}[{P}Baddest  Nigerian Coder✓{H}]{H}

 
{H}Version{H}:{P}2.0{P}     
      
      
...................{P}[ {H} Cookies To Token ( EAAB ) {P} ]{P}...................
''')
# Menu Convert Token
def __main__():
  try:
    os.system('clear')
    print(f"""{__logo__}
{P}1{M}.{H} Convert Cookie To EAAB Token
{H}2{H}.{P} Contact Melanin
{P}3{M}.{H} Log Out (exit)
    """)
    
    masuk = input(f"{P} Select :{P} ")
    if masuk in ['1','01']:
      cookie = input(f"{P}[•]{H}.{P}Enter Cookies  :{H} ")
      if len(cookie) == 0:
        exit(f"{M}!{P}.{M} Don't be empty")
      else:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0',
            'Cookie': cookie
        }
        with requests.Session() as r:
          req = r.get('https://web.facebook.com/adsmanager?_rdc=1&_rdr', headers = headers)
          cari_id = re.findall('act=(.*?)&nav_source', req.text)
          for z in cari_id:
            rex = r.get(f'https://web.facebook.com/adsmanager/manage/campaigns?act={z}&nav_source=no_referrer', headers = headers)
            token = re.search('(EAAB\w+)', rex.text).group(1)
            print(f"\n{P}[•]{H}.{P}Your EAAB Token :{H} {token}")
    elif masuk in ['2','02']:
      print(f"{P}!{K}.{P} You will be redirected to WhatsApp...");time.sleep(2);os.system('xdg-open https://wa.me/+2349150557103');exit()
    elif masuk in ['3','03']:
      exit()
    else:
      exit(f"{M}!{P}.{M} Wrong input")
  except Exception as e:
    exit(f"{M}!{P}.{M} {e}")

if __name__=='__main__':
  os.system('git pull');__main__()