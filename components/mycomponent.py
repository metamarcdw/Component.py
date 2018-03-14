React = require("react")
from components.component import Component

class MyComponent(Component):
    def __init__(self, *args):
        super().__init__(*args)
        self.component.state = { "count": 0 }

    def render(self):
        return __pragma__("xtrans",
                          "npx babel --presets=react",
                          "{}", """
            <div className="style">
                Hello World {self.state["count"]}
            </div>
                          """.strip())

    def componentWillMount(self):
        console.log("Hello World")
