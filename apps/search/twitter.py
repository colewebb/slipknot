import subprocess
print("This search doesn't currently work with hashtags. Look for this\nin upcoming versions.")
input = raw_input("What would you like to search Twitter for? ")
query = "firefox 'https://twitter.com/search?q=" + input + "&src=typd'"
subprocess.call(query, shell=True)
