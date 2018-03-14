React = require("react")
ReactDOM = require("react-dom")

from components.mycomponent import MyComponent
from components.mycomponent2 import MyComponent2

root_component = __pragma__("xtrans",
                            "npx babel --presets=react",
                            "{}", """
    <div>
        <MyComponent />
        <MyComponent2 />
    </div>
                            """.strip())
container = document.getElementById("root")
ReactDOM.render(root_component, container)
