#!/bin/bash
mkdir ~/slipknot
cd ~/slipknot
echo Installing python, if you don’t have it already
lwp-download https://www.python.org/ftp/python/2.7.11/python-2.7.11-macosx10.6.pkg
sudo installer -pkg ~/slipknot/python-2.7.11-macosx10.6.pkg -target /
echo Getting Slipknot source code
lwp-download https://github.com/colewebb/slipknot/blob/master/slipknot.py
lwp-download https://github.com/colewebb/slipknot/blob/master/startup.sh
lwp-download https://github.com/colewebb/slipknot/blob/master/default.db
chmod a+x ./slipknot.py
chmod a+x ./startup.sh