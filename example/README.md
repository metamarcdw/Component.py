### Example of React development with python using Transcrypt
First install Python 3.6/pip, npm>=5.2, and Git:  
`sudo pacman -S python-pip npm git`  
Next clone the repo and set up our React/Transcrypt environment:  
```
git clone https://github.com/metamarcdw/Component_py.git
cd Component_py/

mkvirtualenv transcrypt
pip install --upgrade transcrypt
pip install -e .

cd example/
npm install

make compile  
make go  
```
Open Firefox/Chrome and connect to http://localhost:3000
