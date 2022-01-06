# Don't Die - A Python Program
A python program that causes your computer to bluescreen whenever you die in Minecraft

# Requirements
Don't Die only works on Windows right now, but I thinking about porting it to other operating systems

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
 - `python dontdie.py`


# Build Instructions

 - Follow instructions to run from source
 
 - Install pyinstaller
 `pip install pyinstaller`

 - Build executable
 `pyinstaller --onefile dontdie.py`

Executable is available at `dist/dontdie.exe`

 
