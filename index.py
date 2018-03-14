React = require("react")
ReactDOM = require("react-dom")

from components.mycomponent import MyComponent

mycomponent = __pragma__("xtrans",
						 "npx babel --presets=react",
						 "{}", """
	<MyComponent />
						 """.strip())
container = document.getElementById("root")
ReactDOM.render(mycomponent, container)
