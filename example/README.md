### Example of React development with python using Transcrypt and Component.py
First install Python>=3.6/pip, NodeJS/npm>=5.2, and Git:  
`sudo pacman -S python-pip npm git`  
Next, clone the repo  
```
git clone https://github.com/metamarcdw/Component.py
cd Component.py/
```
Now set up your React/Transcrypt environment:  
(Use of a virtual environment is recommended but not required)  
```
mkvirtualenv transcrypt
pip install git+https://github.com/qquick/transcrypt@master#egg=transcrypt
pip install -e .

cd example/
npm install
```
We can now compile with Transcrypt and run our Webpack server  
```
./compile
npm start
# OR (If running Windows)
npm run win
```
Open up a browser and connect to http://localhost:3000
