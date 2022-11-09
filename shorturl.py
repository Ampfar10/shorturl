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
    #sleep(2)
    print(Fore.GREEN + "Done")
    print(Fore.MAGENTA + "Link to shorten: " + link)
    print(Fore.CYAN + "Shorten url: " + x)
    link2 = input(Fore.YELLOW +"Would you like to shorten another link ")
    if link2 == "no" or link2 == "No":
        print(Fore.RED + "Goodbye!!!")
        break
      

    







  
  
