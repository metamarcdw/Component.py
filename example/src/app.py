from Component_py.stubs import require  # __:skip
from Component_py.component import Component
from components.mycomponent import MyComponent
from components.mycomponent2 import MyComponent2

React = require("react")

class App(Component):
    def render(self):
        return __pragma__("xtrans",
                          "npx babel --presets=react",
                          "{}", """
            <div>
                <MyComponent />
                <MyComponent2 />
            </div>
                          """.strip())
