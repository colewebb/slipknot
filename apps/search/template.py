import subprocess
site = "yoursite.com"
input = raw_input("What would you like to search " + site + " for? ")
input = "site:" + site + " " + input
query = "firefox 'https://www.google.com/search?client=ubuntu&channel=fs&q=" + input + "&ie=utf-8&oe=utf-8'"
subprocess.call(query, shell=True)
