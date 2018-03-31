from Component_py.stubs import __pragma__, require, document  # __:skip
from app import App

React = require("react")
ReactDOM = require("react-dom")

app = __pragma__("xtrans", None, "{}", "<App />")
ReactDOM.render(app, document.getElementById("root"))
