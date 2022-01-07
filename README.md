# Don't Die - A Python Program
A python program that causes your computer to bluescreen whenever you die in Minecraft

# Requirements
***Be sure to right click and run this program as administrator or else it won't work!***

Don't Die only works on Windows right now, but I'm thinking about porting it to other operating systems

Requires Python 3.9 or later to run

# Installation Instructions
**Option 1: Download from releases**
Go to https://github.com/EmeraldIngot/dontdie-minecraft/releases
Download the latest executable

**Option 2: Run from source**

 - Download source:
 `git clone https://github.com/EmeraldIngot/dontdie-minecraft.git`
 
 `cd dontdie-minecraft`
 - Install python dependencies
`pip install -r requirements.txt`
 - Run Don't Die
 
 ***Make sure you run cmd as administrator or else the computer will not bluescreen***
 - `python dontdie.py`


# Build Instructions

 - Follow instructions to run from source
 
 - Install pyinstaller
 `pip install pyinstaller`

 - Build executable
 `pyinstaller --onefile --icon dontdie.ico dontdie.py`

Executable is available at `dist/dontdie.exe`


# Other Notes
I didn't write Don't Die in a very efficient way, and I am probably going to completely overhaul it later

There are a few things I'd like to change, specifically in how it detects deaths

I might even turn it into a Minecraft mod later, as python really isn't the best way to interface with Minecraft
