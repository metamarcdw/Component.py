from Component_py.stubs import __pragma__, require, document  # __:skip
from app import App

React = require("react")
ReactDOM = require("react-dom")

root_component = __pragma__("xtrans",
                            "npx babel --presets=react",
                            "{}", """
    <App />
                            """.strip())
container = document.getElementById("root")
ReactDOM.render(root_component, container)
