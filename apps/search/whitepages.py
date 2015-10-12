import subprocess
search = raw_input("Enter a 9-digit phone number with hyphens, such as 253-845-9920: ")
search="firefox http://www.whitepages.com/phone/1-" + search
subprocess.call(search, shell=True)
