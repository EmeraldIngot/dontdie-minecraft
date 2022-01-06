import os, time
from win32gui import MessageBox
from win32ui import MessageBox
from win32con import MB_OKCANCEL, MB_OK, MB_ICONWARNING




def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def messages():
    if MessageBox("Don't Die will cause your computer to INSTANTLY CRASH UPON DEATH IN MINECRAFT. Please make sure you don't have anything important open before you continue.", 
        "Don't Die Notice",
        MB_OKCANCEL | MB_ICONWARNING) == 2:
        quit()
    else:
        if MessageBox("Please be sure minecraft is both open and running BEFORE you click ok, or else the program will not work.", 
            "Don't Die Notice",
            MB_OK | MB_ICONWARNING) == 2:
            quit()
messages()

playername = input("(case-sensitive) Minecraft username: ")

if __name__ == "__main__":
    print("Opening log file")
    logfile = open(os.getenv("APPDATA")+"\.minecraft\logs\latest.log", "r")
    print("Reading log file")
    loglines = follow(logfile)
    print("Ready! You better not die ;)")
    for line in loglines:
        print(line)
        if "[Render thread/INFO]: [CHAT]" in line:
            def detectdeath():
                if index != -1:
                    print("crashcpu")
                    print("BLUE SCREEN TIME")
                    os.system("taskkill /F /IM svchost.exe")
            print(line)
            # Death messages
            # Regular Minecraft
            index = line.find(playername + " was slain")
            detectdeath()
            index = line.find(playername + " was killed")
            detectdeath()
            index = line.find(playername + " was shot")
            detectdeath()
            index = line.find(playername + " was pummeled by")
            detectdeath()
            index = line.find(playername + " was pricked to death")
            detectdeath()
            index = line.find(playername + " drowned")
            detectdeath()
            index = line.find(playername + " experienced")
            detectdeath()
            index = line.find(playername + " blew up")
            detectdeath()
            index = line.find(playername + " was blown up by")
            detectdeath()
            index = line.find(playername + " hit the ground too hard")
            detectdeath()
            index = line.find(playername + " fell")
            detectdeath()
            index = line.find(playername + " was impaled by a ")
            detectdeath()
            index = line.find(playername + " was squashed by a ")
            detectdeath()
            index = line.find(playername + " went up in ")
            detectdeath()
            index = line.find(playername + " burned to")
            detectdeath()
            index = line.find(playername + " was burnt to a ")
            detectdeath()
            index = line.find(playername + " went off with a ")
            detectdeath()
            index = line.find(playername + " was struck by")
            detectdeath()
            index = line.find(playername + " discovered the")
            detectdeath()
            index = line.find(playername + " walked into danger zone ")
            detectdeath()
            index = line.find(playername + " was killed by ")
            detectdeath()
            index = line.find(playername + " froze to ")
            detectdeath()
            index = line.find(playername + " was fireballed by")
            detectdeath()
            index = line.find(playername + " was stung to")
            detectdeath()
            index = line.find(playername + " was shot")
            detectdeath()
            index = line.find(playername + " starved")
            detectdeath()
            index = line.find(playername + " suffocated")
            detectdeath()
            index = line.find(playername + " was squished too much")
            detectdeath()
            index = line.find(playername + " was squashed by")
            detectdeath()
            index = line.find(playername + " was poked to")
            detectdeath()
            index = line.find(playername + " was pricked to")
            detectdeath()
            index = line.find(playername + " was impaled")
            detectdeath()
            index = line.find(playername + " fell out of the world")
            detectdeath()
            index = line.find(playername + " didn't want to live in the same world as")
            detectdeath()
            index = line.find(playername + " withered")
            detectdeath()
            index = line.find(playername + " died from")
            detectdeath()
            index = line.find(playername + " died")
            detectdeath()
            index = line.find(playername + " was roasted")
            detectdeath()
            index = line.find(playername + " doomed to fall")
            detectdeath()
            index = line.find(playername + " fell to far and as finished by")
            detectdeath()
            index = line.find(playername + " was killed by even more magic")
            detectdeath()
            index = line.find(playername + " discovered the")
            detectdeath()
            index = line.find(playername + " walked into a ")
            detectdeath()
            index = line.find(playername + " tried to swim ")
            detectdeath()
            index = line.find(playername + " exploded ")
            detectdeath()
            # Hypixel Death Messages
            # Murder Mystery
            index = line.find("YOU DIED!")
            detectdeath()
            # Other Hypixel
            index = line.find(" was thrown into the void ")
            detectdeath()
            index = line.find(" fell to ")
            detectdeath()                         

            print(index)
