import os, time
import subprocess

from typing import Any, Generator
from pathlib import WindowsPath

from win32gui import MessageBox
from win32ui import MessageBox
from win32con import MB_OKCANCEL, MB_OK, MB_ICONWARNING

def read(filename: str) -> Generator[Any]:
	filename.seek(0,2)
	
	while True:
		line = filename.readline()

		if not line:
			time.sleep(0.1)
			continue

		yield line

def show_messages():
	message_box_1 = MessageBox("Don't Die will cause your computer to INSTANTLY CRASH UPON DEATH IN MINECRAFT. Please make sure you don't have anything important open before you continue.", 
		"Don't Die Notice",
		MB_OKCANCEL | MB_ICONWARNING)

	message_box_2 = MessageBox("Please be sure minecraft is both open and running BEFORE you click ok, or else the program will not work.", 
		"Don't Die Notice",
		MB_OK | MB_ICONWARNING)
	
	CODE = 2

	if message_box_1 == CODE:
		quit()
	
	if message_box_2 == CODE:
		quit()

def bsod() -> None:
	print("crashcpu")
	print("BLUE SCREEN TIME")

	subprocess.Popen("taskkill /F /IM svchost.exe", shell=True) # BSOD

def ischat(message: str) -> bool:
	return "[Render thread/INFO]: [CHAT]" in message

def main():
	show_messages()

	player_name = input("Minecraft username (case-sensitive) : ")

	print("Opening log file")
	
	# Construct a path to the logfile
	DELIM = "\\",
	path = WindowsPath(os.getenv("APPDATA"), DELIM, ".minecraft", DELIM, "logs", DELIM, "latest.log")

	# Death messages
	DEATH_MESSAGES = [
		# Regular Minecraft
		f"{player_name} was slain",
		f"{player_name} was killed",
		f"{player_name} was pummeled by",
		f"{player_name} was pricked to death",
		f"{player_name} drowned",
		f"{player_name} experienced",
		f"{player_name} blew up",
		f"{player_name} was blown up by",
		f"{player_name} hit the ground too hard",
		f"{player_name} fell",
		f"{player_name} was impaled by a ",
		f"{player_name} was squashed by a ",
		f"{player_name} went up in ",
		f"{player_name} burned to",
		f"{player_name} was burnt to a ",
		f"{player_name} went off with a ",
		f"{player_name} was struck by",
		f"{player_name} discovered the",
		f"{player_name} walked into danger zone ",
		f"{player_name} was killed by ",
		f"{player_name} froze to ",
		f"{player_name} was fireballed by",
		f"{player_name} was stung to",
		f"{player_name} was shot",
		f"{player_name} starved",
		f"{player_name} suffocated",
		f"{player_name} was squished too much",
		f"{player_name} was squashed by",
		f"{player_name} was poked to",
		f"{player_name} was pricked to",
		f"{player_name} was impaled",
		f"{player_name} fell out of the world",
		f"{player_name} didn't want to live in the same world as",
		f"{player_name} withered",
		f"{player_name} died from",
		f"{player_name} died",
		f"{player_name} was roasted",
		f"{player_name} doomed to fall",
		f"{player_name} fell to far and as finished by",
		f"{player_name} was killed by even more magic",
		f"{player_name} discovered the",
		f"{player_name} walked into a ",
		f"{player_name} tried to swim ",
		f"{player_name} exploded ",

		# Hypixel Death Messages

		"YOU DIED!" # Murder Mystery

		# Other Hypixel
		f"{player_name} was thrown into the void",
		f"{player_name} fell to ",
		f"{player_name} fell into the void"
		"You fell into the void" 
	]

	with open(path, "r") as logfile:
		print("Reading log file")
		loglines = read(logfile)

		print("Ready! You better not die ;)")
		for line in loglines:
			print(line)

			# The chat message beings 2 characters after the clowing bracket.
			# The interval for the message will be [last_bracket + 2, len]
			if ischat(line) and line[line.rfind("]") + 2 :] in DEATH_MESSAGES:
				print(line)
				bsod()        


if __name__ == "__main__":
	import sys
	sys.exit(main())
