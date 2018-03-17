React = require("react")

from components.component import Component
from components.mycomponent import MyComponent
from components.mycomponent2 import MyComponent2

class App(Component):
    def render():
        return __pragma__("xtrans",
                          "npx babel --presets=react",
                          "{}", """
            <div>
                <MyComponent />
                <MyComponent2 />
            </div>
                          """.strip())
