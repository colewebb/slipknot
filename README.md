# slipknot
Slipknot is a program, rendered in Python, for Linux, that gives new names to commands that you use a lot. It has at its core the dream of ultimate user configurability, where the computer conforms to what you want, not the other way around.


It does this by tapping into a user-created database that contains a list of equivalence statements. 

An example: ff = firefox

Slipknot, when run, presents a prompt similar to a bash shell. With the above example, if you were to type ff at the prompt and press enter, it would send the command firefox to the operating system to execute.

If the user types something that doesn't show up in the database, it will pass the input to the system to execute. This means that you can treat Slipknot as a normal shell.

# install

To install this program, do the following things:


1. Make sure you have Python 2.7 installed, along with the standard libraries subprocess and os.
2. Clone this repo into some otherwise empty directory.
3. Edit /etc/environment, make a new environment variable named SLIPKNOT_HOME, and set it equal to the path of the folder you just cloned this repo into. This must be precise.
4. Run the file slipknot, or run the file slipknot.py in Python.
5. Enjoy!

I'm told that it will run, unmodified, on Unix systems (tested on Mac OS X 10.5). However, I haven't personally seen it in action, so proceed with caution. The worst thing that can happen is that it fails with a callback or it executes some command that you didn't mean it to. 


If it does fail, please copy and paste the entire callback into an Issue. I really appreciate bug reporting. If you feel like fixing it, cool. Make a fork, fix it, and put in a pull request. You know the drill.


I did make a launcher that you can move around to wherever you want. It's in here just as slipknot, and is compiled from slipknot.cpp. This launcher is mobile, so you can put it in your executable path and use it as you would a normal executable.


My Twitter handle is @69codewars. Let me know, over Twitter or GitHub, if there are any problems.


Thanks!


~CW
