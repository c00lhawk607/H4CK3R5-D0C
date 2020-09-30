#Functions for H4CK3R'5 D0C#
import os, time, pickle, base64

def bash(cmd):
	"""Executes command in seperate bash terminal."""
	os.system(cmd)

from colorama import *
init()

from clearing import clear


def printG(message):
	print(Fore.GREEN + message,sep="", end="",flush= True)

def inputG(message):
	input(Fore.GREEN + message)
	###############################################
	

while True:
	start = """H3LL0, W3LC0M3 T0 H4CK3R5 D0C!\n"""

	clear()

	i = 0

	while i < len(start):
		printG(start[i])
		time.sleep(0.09)
		i += 1
	
	time.sleep(2)
	clear()

	bash("ls -p -a | grep -v /")

	nex = "What is the name of the document?\n"

	i = 0
	while i < len(nex):
		printG(nex[i])
		time.sleep(0.09)
		i += 1


	name = input("Name: ")

	clear()
	printG("To go into instert mode press i. To quit without saving, if in insert mode press esc, then press :q and hit enter. To save the doc press esc if in insert mode then press :wq and enter.")
	Style.RESET_ALL
	time.sleep(2.5)
	clear()
	
	try:
		f = open(name, "rb")
		contents = pickle.load(f)
		contents = base64.b64decode(contents)
		contents = contents.decode("utf8")
		f.close()
		f = open(name, "w")
		f.write(contents)
		f.close()
	except:
		pass
	bash("vim "+name)

	if ".py" in name:
		bash("python3 "+ name)
	else:
		pass

	if ".html" in name:
		bash("firefox "+ name)
	else:
		pass
	
	if ".sh" in name:
		bash("bash "+ name)
	else:
		pass
	
	time.sleep(1.0)
	


	f = open(name, "r")
	contents = f.read()
	contents = contents.encode("utf8")
	contents = base64.b64encode(contents)
	f.close()

	try:
		f = open(name, "wb")
		pickle.dump(contents, f)
		f.close()
	except:
		pass

	clear()