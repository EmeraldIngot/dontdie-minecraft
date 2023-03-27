# Don't Die - A Python Program
A python program that causes your computer to bluescreen whenever you die in Minecraft

# If you want the prerelease with a GUI download it here:
***Be sure to right click and run this program as administrator or with sudo or else it won't work!***
https://github.com/EmeraldIngot/dontdie-minecraft/releases/tag/v1.3-pre

# Requirements
***Be sure to right click and run this program as administrator or with sudo or else it won't work!***

Don't Die is now officially supported on Windows, macOS, and Linux!

No requirements to run binaries

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
 
 `build_windows.bat`

Executable is available at `dist/dontdie.exe`

Rigth click and run with administrator!

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
 
 ***Make sure you run python with sudo or login to the root account with `sudo su` first or else the computer will not bluescreen***
 
  you might have to reinstall the python modules as root after doing so
 
 `python dontdie.py`


# Build Instructions

 - Follow instructions to run from source
 
 - Install pyinstaller
 
 `pip install pyinstaller`

 - Build executable
 
 `./build_linux.sh`

Binary is available at `dist/dontdie`

Remember to run with `sudo` or else it won't work!
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
 
 ***Make sure you run python with sudo or log into the root account with `sudo su` before or else the computer will not bluescreen***
 
 you might have to reinstall the python modules as root after doing so
 
 `python dontdie.py`


# Build Instructions

 - Follow instructions to run from source
 
 - Install pyinstaller
 
 `pip install pyinstaller`

 - Build executable
 
 `./build_macos.sh`

.app is available at `dist/dontdie`

In order to run as root, go to where the .app is, and run the following command
sudo ./dontdie.app/Contents/MacOS/dontdie
</details>


# Other Notes

The new version of Don't Die is currently a pre-release
