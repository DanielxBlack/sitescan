#!/usr/local/bin/python3.5

# imports required modules.
import requests
import os
import time
import sys
import cmd
import string, random


"""This utlitly is designed to enumerate a website. It will run through a site such as lamesite.com and check for existing pages such as lamesite.com/admin, lamesite.com/login, lamesite.com/robots.txt, etc. It will then inform the user which of those pages exist. """

# clear the terminal screen and display banner
os.system("clear")

print(".........................................................")
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print(":::::::::::'######::'####:'########:'########::::::::::::")
print("::::::::::'##... ##:. ##::... ##..:: ##.....:::::::::::::")
print(":::::::::: ##:::..::: ##::::: ##:::: ##::::::::::::::::::")
print("::::::::::: ######::: ##::::: ##:::: ######::::::::::::::")
print(":::::::::::..... ##:: ##::::: ##:::: ##...:::::::::::::::")
print("::::::::::'##::: ##:: ##::::: ##:::: ##::::::::::::::::::")
print("::::::::::. ######::'####:::: ##:::: ########::::::::::::")
print(":::::::::::......:::....:::::..:::::........:::::::::::::")
print("::::::::::'######:::'######:::::'###::::'##::: ##::::::::")
print(":::::::::'##... ##:'##... ##:::'## ##::: ###:: ##::::::::")
print("::::::::: ##:::..:: ##:::..:::'##:. ##:: ####: ##::::::::")
print(":::::::::. ######:: ##:::::::'##:::. ##: ## ## ##::::::::")
print("::::::::::..... ##: ##::::::: #########: ##. ####::::::::")
print(":::::::::'##::: ##: ##::: ##: ##.... ##: ##:. ###::::::::")
print(":::::::::. ######::. ######:: ##:::: ##: ##::. ##::::::::")
print("::::::::::......::::......:::..:::::..::..::::..:::::::::")
print("---------------------------------------------------------")
print("--------------------------By Daniel.---------------------")
print('                                                         ')
print("---------------------------------------------------------")
print("")


# enter a url
scan = input("Website to scan: ")
print("")
print("")

# choose between wordlist or standard scan. remove extra spaces and caps.
choice = input("Use wordlist (list) or standard scan (scan)? ")
choice = choice.lower()
choice = choice.strip()
print("")

# allow to import wordlist
if choice == "list":
    wordlist = input("Select a wordlist. ")
    print("")
    with open(wordlist) as f:
        for line in f:
            for listWord in line.split():
                words = [str(listWord)]
                # def show_status and create a for loop
                def view_status(words, scan):
                    for listWord in words:
                        pages = ("http://" + scan + "/" + listWord)
                        wList = requests.get(pages)
                        print("- Status of " + str(pages) + " : " + str(wList))
                        print("  Page exists? " + str(wList.status_code == requests.codes.ok))
                        print("")
                view_status(words,scan)





# scan sites with default scan
elif choice == "scan":
    # script will go through these postfixes
    postfixes = ["","/index.php", "/admin", "/login","/robots.txt","/register","/wp-admin/admin-ajax.php","/wp-admin","/administrator","/feeds","/_/rstc/","/_/","/sitemap","/system","/feed","/system/feeds/sitemap","/auth/login.php","/ftp","/vpn", "/readme.html","/wp-includes/rss-functions.php","/wp-content","/wp-content/plugins","/wp-content/audio-player","/wp-content/plugins/dynamic-content-gallery-plugin/"]

    # def show_status and create a for loop
    def show_status(postfixes, scan):
        for postfix in postfixes:
            name = ("http://" + scan + postfix)
            s = requests.get(name)
            print("- Status of " + str(name) + " : " + str(s))
            print("  Page exists? " + str(s.status_code == requests.codes.ok))
            print("")
    show_status(postfixes,scan)

else:
    print("Please relaunch program.")
