React = require("react")

from components.mycomponent import MyComponent
from components.mycomponent2 import MyComponent2

def App():
    return __pragma__("xtrans",
	                  "npx babel --presets=react",
	                  "{}", """
        <div>
            <MyComponent />
            <MyComponent2 />
        </div>
                      """.strip())
