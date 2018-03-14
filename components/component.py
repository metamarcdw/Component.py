React = require("react")

class Component:
    isReactComponent = {}

    def __init__(self, props, context, updater):
        self.component = __new__(React.Component(props, context, updater))

    def setState(self, partialState, callback):
        return self.component.setState(partialState, callback)

    def forceUpdate(self, callback):
        return self.component.forceUpdate(callback)

    @property
    def state(self):
        return self.component.state
