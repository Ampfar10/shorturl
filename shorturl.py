import pyshorteners
import colorama
from colorama import Fore
import pyfiglet
import time

while True:
    print(Fore.BLUE + pyfiglet.figlet_format("ShotUrl",font = 'larry3d'))

    link = input("Enter your link : ")
    short = pyshorteners.Shortener()
    x = short.tinyurl.short(link)
    print(Fore.RED + "Please wait....")
    time.sleep(2)
    print(Fore.GREEN + "Done")
    time.sleep(1)
    print(Fore.MAGENTA + "Link to shorten: " + link)
    time.sleep(1)
    print(Fore.CYAN + "Shorten url: " + x)
    time.sleep(1)
    link2 = input(Fore.YELLOW +"Would you like to shorten another link ")
    if link2 == "no" or link2 == "No":
        print(Fore.RED + "Goodbye!!!")
        break
      

    







  
  
