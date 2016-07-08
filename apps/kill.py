import subprocess
kill = raw_input("What program would you like me to obliterate for you? ")
list = ["killall " + kill,
"sudo apt-get -y remove " + kill,
"sudo apt-get -y autoremove",
"sudo apt-get -y purge " + kill]
for item in list:
	subprocess.call(item, shell=True)
