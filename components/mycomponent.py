React = require("react")
from components.component import Component

class MyComponent(Component):
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.state = { "count": 0 }

    def render(self):
        return __pragma__("xtrans",
                          "npx babel --presets=react",
                          "{}", """
            <div className="style">
                Hello World {self.state["count"]}
            </div>
                          """.strip())

    def componentWillMount(self) -> None:
        console.log("Hello World")
