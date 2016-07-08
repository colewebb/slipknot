import subprocess
get_object = raw_input("What program do you want to painlessly install? ")
string = "sudo apt-get -y install " + get_object + " && " + get_object
subprocess.call(string, shell=True)
