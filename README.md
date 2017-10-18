# selenium-python-doc
Learning python via python-selenium docs http://selenium-python.readthedocs.io/getting-started.html





#Important Readme(under construction)

#Installations
cd ~/
sudo apt-get install python-pip
sudo pip install --upgrade pip
sudo pip install selenium
sudo apt-get install python-pytest
sudo apt-get install git


#Geckodriver
git clone https://github.com/rishabh27892/webui-test-files/
cd webui-test-files/
tar -xvzf geckodriver-v0.11.1-linux64.tar.gz
chmod +x geckodriver
sudo cp geckodriver /usr/local/bin/
cd ~/
rm -rf webui-test-files/

#Download selenium-python-doc repo
git clone https://github.com/rishabh27892/selenium-python-doc/

#Tests…….


#Generate XML result:
pytest format(-junitxml) <nameofresultfile> <testfile>

