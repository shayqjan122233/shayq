import base64

import os
from colorama import Fore as color 

from time import sleep



def sh():
	sd=input("inter name file !?  ")
	with open(sd,"r") as file:
		fil=file.read()
	encod = fil.encode("utf-8")
	b16 = base64.b16encode(encod)
	print(b16)
	
	dd=input("enter name file ;:  ")
	with open (dd,"wb") as d:
		dd=d.write(b16)
		
	print(dd)
		
sh()
		
	






def data():
	dat=input("inter nem file ")
	with open (dat,"rb") as file:
		fil=file.read()
	b16=base64.b16decode(fil).decode("utf-8")
	print(b16)
	
	ded=input("inet name file : ")
	with open(ded,"w") as fd:
		fd.write(b16)
	print(fd)




def returne():
	print("   ")
	print(color.RED+"plesss ines cloning .  .   .   .")
	sleep(1.5)
	os.system("clear")
	
	
	
	print(color.GREEN+"""
	____________________
	"""+color.CYAN+"""
	       KYhan RM"""+color.GREEN+"""
	____________________
	
	
	""")
	
	sleep(1.5)
	
	print(color.CYAN+" [1]=>"+color.GREEN+"encode base64 :?  ")
	
	print(color.CYAN+" [1]=>"+color.GREEN+"decode base64 :? ")
	print("_"*64)
	
	print(color.CYAN+"plese inter mat ? :    ")
	
	sd=input(color.GREEN+"plesee unter base :  ")
	if sd==1:
		os.system("clear")
		sleep(1.5)
		print("welcom   to base ")
		sh()
	else:
		os.system("clear")
		data()
	
	
	
	
	
returne()