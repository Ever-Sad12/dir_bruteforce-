#Don't copy my code just creat your own script be ethic
import requests

def banner():
	print('\n¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤')
	print('¤   Coder- Da4k W0lF   ¤')
	print('¤   	Happy Hacking  ¤')
	print('¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤')
	
banner()
url = input('\n[+]Enter Domain name: ')
path = input('[+]Enter path :')

file = open(path, "r")

for i in range(100):
	a = file.readline()
	
	r = requests.get(url+a)
	s = r.status_code
	
	print('\n¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤')
	print('Domain', url+a)
	print('Status', s)
	print('¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤')
	
file.close()