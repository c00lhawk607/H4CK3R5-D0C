#Functions for H4CK3R'5 D0C#
import os, time, pickle, base64

def bash(cmd):
	"""Executes command in seperate bash terminal."""
	os.system(cmd)

def pip(package):
	"""
	Installs a package from pypi.
	"""
	bash("pip install "+package)

try:
	pip("--upgrade pip")
except:
	pass


try:
	from colorama import *
	init()
except:
	pip("colorama")
	from colorama import *
	init()

try:
	from clearing import clear
except:
	pip("clearing")
	from clearing import clear


def printG(message):
	print(Fore.GREEN + message,sep="", end="",flush= True)

def inputG(message):
	input(Fore.GREEN + message)