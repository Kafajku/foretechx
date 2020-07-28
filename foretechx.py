# kafalib
# Python module made by Kazafka
# Copyright (C) since 2020 - All rights reserved

import base64
import keyboard
import playsound
import time
import msvcrt
import os
import ctypes
import requests

class file:
	""" A file class """
	def getBytes(path):
		""" Returns name and raw bytes value of a file """
		def getFileName(s):
			i = s.rfind("\\")
			if i == -1:
				i = s.rfind("/")
			l = list(s)
			return "".join(l[i + 1:len(l)])

		name = getFileName(path)
		file = open(path)
		string = file.read()
		string = base64.b64encode(string)
		return name, string.decode("ascii")
		file.close()

	def writeBytes(pathToFile: str, bytesValue: bytes):
		""" Re-creates a file by it's raw bytes value """
		file = open(pathToFile, "wb")
		normalValue = bytesValue.encode("ascii")
		normalValue = base64.b64decode(normalValue)
		file.write(normalValue)
		file.close()

	def requestFromURL(URL: str, toPath: str):
		def getFileName(s):
			i = s.rfind("\\")
			if i == -1:
				i = s.rfind("/")
			l = list(s)
			return "".join(l[i + 1:len(l)])

		name = getFileName(URL)
		normalValue = requests.get(URL, allow_redirects = True).content
		file_ = open(toPath + name, "wb")
		file_.write(normalValue)
		file_.close()

class key:
	""" Use 'key.bind()' to create a key binding """
	class bind:
		""" Creates a key binding; returns an instance which is used to check whenever the key was pressed """
		def __init__(self, keyName: str, handler):
			""" The INIT function """
			self.__keyName = keyName
			self.__handler = handler

		def isActive(self):
			""" Place in a loop (e.g. 'while' loop); checks if the key was pressed and runs the handler function """
			if keyboard.is_pressed(self.__keyName):
				self.__handler()

	def isActive(keyName: str):
		""" Returns key state ('True' if state is positive, otherwise - 'False') """
		return keyboard.is_pressed(keyName)

	def hold(keyName: str):
		""" Holds a key """
		keyboard.press(keyName)

	def release(keyName: str):
		""" Releases a key """
		keyboard.release(keyName)

	def press(keyName: str):
		""" Presses a key """
		keyboard.press_and_release(keyName)

	def write(keySeq: str):
		""" Presses a key sequence """
		keyboard.write(keySeq)

def playSound(pathToFile: str):
	""" Creates a simple stream, used to play sounds; returns dictionary with key 'soundPath' storing given path """
	playsound.playsound(pathToFile)
	return {
		"soundPath": pathToFile
	}

def sleep(delay):
	""" Waits a specified time in ms """
	delay /= 1000
	time.sleep(delay)

def pause():
	""" Pauses Python script and returns pressed character """
	return msvcrt.getch()

def cls():
	""" Deletes any printed message """
	os.system("cls")

def match(var, container: dict):
	""" Returns variable name with matching value, if there's no matching value - returns bool 'False'; searches in the given container; container must always be defined """
	for var_, val in container.items():
		if var is val:
			if var_ != "var" and var_ != "__annotations__" and var_ != "__dict__":
				return var_
	return False

class cursor:
	""" Class for cursor """
	def setPos(xPos, yPos):
		""" Moves the terminal cursor """
		genPos = xPos + (yPosyPos << 16)
		handler = ctypes.windll.kernel32.GetStdHandle(ctypes.c_long(-11))
		ctypes.windll.kernel32.SetConsoleCursorPosition(handler, ctypes.c_ulong(genPos))

colors = {
	"black": "\033[0;30;40m",
	"gray": '\u001b[30;1m',
	"red": '\u001b[31;1m',
	"green": '\u001b[32;1m',
	"yellow": '\u001b[33;1m',
	"blue": '\u001b[34;1m',
	"magenta": '\u001b[35;1m',
	"cyan": '\u001b[36;1m',
	"white": '\u001b[37;1m',
	"underline": '\u001b[4m',
	"reverse": '\u001b[7m',
	"def": '\u001b[0m'
}

def resize(columns, lines):
	""" Changes columns and lines of the terminal """
	columns = int(columns / 16)
	lines = int(lines / 32)
	os.system("mode con: cols=" + str(columns) + " lines=" + str(lines))
