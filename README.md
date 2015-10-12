# slipknot
Slipknot is a program, rendered in Python, for Linux, that gives new names to commands that you use a lot. It has at its core the dream of ultimate user configurability, where the computer conforms to what you want, not the other way around.


It does this by tapping into a user-created database that containing a list of equivalence statements. 

An example: ff = firefox

Slipknot, when run, presents a prompt similar to a bash shell. With the above example, if you were to type ff at the prompt and press enter, it would send the command firefox to the operating system to execute.

If the user types something that doesn't show up in the database, it will pass the input to the system to execute. This means that you can treat Slipknot as a normal shell.

# install

To install this program, do the following things:


1. Make sure you have Python 2.7 installed, along with the standard libraries subprocess and os.
2. Clone this repo into some otherwise empty directory.
3. Edit /etc/environment, make a new environment variable named SLIPKNOT_HOME, and set it equal to the path of the folder you just cloned this repo into. This must be precise.
4. Enjoy!


I did make a launcher that you can move around to wherever you want. It's in here just as slipknot, and is compiled from slipknot.cpp. This launcher is mobile, so you can put it in your executable path and use it as you would a normal executable.


My Twitter handle is @69codewars. Let me know, over Twitter or GitHub, if there are any problems.


Thanks!


~CW
