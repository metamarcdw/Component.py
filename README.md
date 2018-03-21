### Example of React development with python using Transcrypt
First install Python 3.6/pip, npm>=5.2, and Git:  
`sudo pacman -S python-pip npm git`  
Next clone the repo and set up our React/Transcrypt environment:  
```
git clone https://github.com/metamarcdw/react-transcrypt.git
cd react-transcrypt/

npm install
mkvirtualenv react-transcrypt
pip install --upgrade transcrypt

make compile  
make go  
```
