import subprocess
input = raw_input("What would you like to search Reddit for? ")
query = "firefox 'https://www.reddit.com/search?q=" + input + "'"
subprocess.call(query, shell=True)
