# Don't Die - A Python Program
A python program that causes your computer to bluescreen whenever you die in Minecraft

# If you want the prerelease with a GUI read below:

***IMPORTANT Be sure to right click and run this program as administrator or run it with sudo or else it won't work!***

<details>
<summary>How do I do that?</summary>

# Windows

If you are on Windows, right click on the exe and click run as administrator. If prompted to allow changes, click yes.

# macOS

If you are on macOS, navigate to the folder containing the .app in the terminal, and run the following:

`sudo ./dontdie.app/Contents/MacOS/dontdie`

<details>
<summary>How do I navigate to the folder in terminal?</summary>
<br>
Mount the downloaded DMG file by double clicking it.

Move dontdie.app off of the DMG onto your desktop.

open the terminal and run the following command:

`cd ~/Desktop`

After that, run the command above.

`sudo ./dontdie.app/Contents/MacOS/dontdie`

It will prompt you for your password. It will not indicate you are typing, but you are. Press enter after typing it.
</details>

# Linux

If you are on Linux, navigate to the folder containing the binary and run the following:

`sudo ./dontdie`

</details>

### Remember to read the instructions. Heres the download! 

https://github.com/EmeraldIngot/dontdie-minecraft/releases/tag/v1.3-pre

# Requirements
***Be sure to right click and run this program as administrator or with sudo or else it won't work!***

Don't Die is now officially supported on Windows, macOS, and Linux!

No requirements to run binaries

Requires Python 3.11 or later to build from source

# Installation Instructions
## Option 1: Download from releases

Go to https://github.com/EmeraldIngot/dontdie-minecraft/releases

Download the latest executable for your operating system


## Option 2: Run from source


<details>
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

<details>
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

<details>
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
 
 If ./build_macos.sh returns an error, pyinstaller might not be in your path.
 
 To fix this, edit build_macos.sh in any text editor, and where is says `pyinstaller` replace it with `~/Library/Python/3.11/bin/pyinstaller`
 
 If you are not using Python 3.11, you can substitute the version for another.

Once it is built, the .app is available at `dist/`

In order to run as root, go to where the .app is, and run the following command
sudo ./dontdie.app/Contents/MacOS/dontdie
</details>


# Other Notes

The new version of Don't Die is currently a release candidate
Hopefully, not much will change from the RC to the full release
