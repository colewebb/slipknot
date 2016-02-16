# Slipknot - Advanced Command Line Aliasing
#    Copyright (C) 2015  Cole Webb
#
# This program is free software: you can redistribute it and/or modify it under the terms of
# the GNU General Public License as published by the Free Software Foundation, either version 3
# of the License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.


try:
	import os, subprocess
except:
	print("Your machine is missing one of the following libraries:\n\n    1) os\n    2) subprocess\n\nPlease make sure these libraries are installed, and try again.")
	exit(1)
subprocess.call("/home/rebooted/Scripts/slipknot/startup.sh", shell=True)
try:
	database=open(os.getenv("SLIPKNOT_HOME") + "/database.txt")
	database.close
	main_database_exists=True
	main_database_status="txt"
except:
	main_database_exists=False
	main_database_status=""
database_count=0
if main_database_exists==False:
	print("\nNo databases where found. Please make sure you have\na database named database.txt on the root of the\nslipknot folder.")
	exit(1)
found=False
if main_database_status=="txt":
	for line in database:
		database_count=database_count+1
if input=="exit":
	exit()
elif input=="x":
	exit()
def find_in_text(search):
	found=False
	database=open(os.getenv("SLIPKNOT_HOME") + "/database.txt")
	search=search + " = "
	for line in database:
		if found==False:
			if line.startswith(search):
				execute_platform=line.split(search,1)
				execute=execute_platform[1]
				execute=execute.rstrip()
				found=True
				pass
			else:
				found=False
				continue
	if found==False:
		execute="data not found"
	return execute
while True:
	input=raw_input("slipknot>"+":"+os.getenv("PWD")+" >>> ")
	if input=="x":
		exit()
	elif input=="exit":
		exit()
	elif input=="close":
		exit()
	elif input=="clear":
		subprocess.call("python " + os.getenv("SLIPKNOT_HOME") + "/slipknot.py", shell=True)
		exit()
	elif input=="c":
		subprocess.call("xfce4-terminal -x python " + os.getenv("SLIPKNOT_HOME") + "/slipknot.py", shell=True)
		exit()
	else:
		execute = find_in_text(input)
		if execute == "data not found":
			subprocess.call(input, shell=True)
		else:
			subprocess.call(execute, shell=True)
