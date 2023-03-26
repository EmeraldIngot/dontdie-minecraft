# Don't Die - A Python Program
A python program that causes your computer to bluescreen whenever you die in Minecraft


# Requirements
***Be sure to right click and run this program as administrator or else it won't work!***

Don't Die is now officially supported on Windows, macOS, and Linux!

No requirements to run executable

Requires Python 3.11 or later to build from source

# Installation Instructions
**Option 1: Download from releases**
Go to https://github.com/EmeraldIngot/dontdie-minecraft/releases

Download the latest executable for your operating system


**Option 2: Run from source**

Instructions are not provided here for building on macOS and Linux


<details open>
<summary><strong>Windows</strong></summary>
<br>
Make sure you have the correct version of python for windows installed (3.11)

Open CMD

 - Download source
 
 If you have git for windows installed then run the following

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
 
 `pyinstaller dontdie.spec`

Executable is available at `dist/dontdie.exe`
</details>

<details open>
<summary><strong>Linux</strong></summary>
<br>
Make sure you have the correct version of python installed (3.11)

Open the terminal
 - Download source
 
Either run the following

 `git clone https://github.com/EmeraldIngot/dontdie-minecraft.git`
 
 `cd dontdie-minecraft`
 
or download the source zip and extract it
 
 - If you downloaded the source zip folder, move into the directory by typing
 
 `cd dontdie-minecraft-master`
 
 from where you extracted it to
 
 Run `ls` to make sure you are in the right directory
 
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
 
 `pyinstaller dontdie.spec`

Binary is available at `dist/dontdie`
</details>

<details open>
<summary><strong>macOS</strong></summary>
<br>
Make sure you have the correct version of python for macOS installed (3.11)

Open the terminal
 - Download source
 
Either run the following

 `git clone https://github.com/EmeraldIngot/dontdie-minecraft.git`
 
 `cd dontdie-minecraft`
 
or download the source zip and extract it
 
 - If you downloaded the source zip folder, move into the directory by typing
 
 `cd dontdie-minecraft-master`
 
 from where you extracted it to
 
 Run `ls` to make sure you are in the right directory
 
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
 
 `pyinstaller dontdie.spec`

Binary is available at `dist/dontdie`
</details>


# Other Notes

The new version of Don't Die is currently a pre-release
