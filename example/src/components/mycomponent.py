from Component_py.component import Component
from Component_py.stubs import require  # __:skip
React = require("react")

class MyComponent(Component):
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.state: Dict[str, int] = { "count": 0 }

    def render(self):
        return __pragma__("xtrans",
                          "npx babel --presets=react",
                          "{}", """
            <div className="style">
                Hello World {self.state["count"]}
            </div>
                          """.strip())

    def componentDidMount(self) -> None:
        self.setState({ "count": 1 })
        console.log("Hello World")
