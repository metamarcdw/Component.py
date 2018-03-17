React = require("react")
ReactDOM = require("react-dom")

from app import App

root_component = __pragma__("xtrans",
                            "npx babel --presets=react",
                            "{}", """
    <App />
                            """.strip())
container = document.getElementById("root")
ReactDOM.render(root_component, container)
