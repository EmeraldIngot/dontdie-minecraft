# Don't Die - A Python Program
A python program that causes your computer to bluescreen whenever you die in Minecraft

# What I'm working on now 
I'm working on turning it into a minecraft mod

I would like to add mac and linux support, but neither have a way like windows
to cause a bluescreen without admin privilages.
The only other thing I can think of is maybe a fork bomb on linux, but that wouldn't do the same thing

Most of my modding experience is with fabric, but I will try to make a version for forge too

UPDATE: Finished the Forge version of the mod, but I have to update it to 1.18.2

Still testing it

Fabric doesn't seem to have any way to detect deaths, so I'm not sure there will be a Fabric version

# Requirements
***Be sure to right click and run this program as administrator or else it won't work!***

Don't Die only works on Windows right now, but I'm thinking about porting it to other operating systems

No requirements to run executable

Requires Python 3.9 or later to build from source

# Installation Instructions
**Option 1: Download from releases**
Go to https://github.com/EmeraldIngot/dontdie-minecraft/releases

download the latest executable


**Option 2: Run from source**

Make sure you have python for windows installed

Open CMD

 - Download source
 
 If you have git for windows installed then 

 `git clone https://github.com/EmeraldIngot/dontdie-minecraft.git`
 
 `cd dontdie-minecraft`
 
 otherwise, just download the source zip file and extract it
 
 - If you downloaded the source zip folder, move into the directory by typing
 
 `cd dontdie-minecraft-master`
 
 from where you extracted it to
 
 Run `dir` to make sure you are in the right directory
 
 If returns a bunch of stuff like dontdie.py and dontdie.ico, then you're good to go
 
 - Install python dependencies
  
`pip install -r requirements.txt`

 - Run Don't Die
 
 ***Make sure you run cmd as administrator or else the computer will not bluescreen***
 
 `python dontdie.py`


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
