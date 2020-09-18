import os, time, pickle


try:
	from clearing import clear
except:
	os.system("pip3 install clearing")
	from clearing import clear


try:
	from colorama import *
	init()
except:
	os.system("pip3 install colorama")
	from colorama import *
	init()
while True:
	start = """H3LL0, W3LC0M3 T0 H4CK3R5 D0C!
1) Create a new Doc
2) Load an existing Doc\n"""

	clear()

	i = 0

	while i < len(start):
		print(Fore.GREEN + start[i],sep="", end="",flush= True)
		time.sleep(0.1)
		i += 1

	choice = input(Fore.GREEN + "Choice: ")

	os.system("ls -p -a | grep -v /")

	nex = "What is the name of the document?\n"

	i = 0
	while i < len(nex):
		print(Fore.GREEN + nex[i], sep="", end="", flush= True)
		time.sleep(0.1)
		i += 1


	name = input("Name: ")
	name = name

	clear()
	print("To go into instert mode press i. To quit without saving, if in insert mode press esc, then press :q and hit enter. To save the doc press esc if in insert mode then press :wq and enter.")
	Style.RESET_ALL
	time.sleep(2.5)
	try:
		f = open(name, "rb")
		contents = pickle.load(f)
		f.close()
		f = open(name, "w")
		f.write(contents)
		f.close()
	except:
		pass
	os.system("vim "+name)
	f = open(name, "r")
	contents = f.read()
	f.close()

	try:
		f = open(name, "wb")
		pickle.dump(contents, f)
		f.close()
	except:
		pass

	clear()