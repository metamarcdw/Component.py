from typing import Dict, Any, Callable
from Component_py.stubs import require  # __:skip
React = require("react")

class Component:
    isReactComponent: Dict[str, Any] = {}

    def __init__(self, props: Dict[str, Any], context, updater) -> None:
        self.component = __new__(React.Component(props, context, updater))
        self.setState = self.component.setState.bind(self)
        self.props = props

    def forceUpdate(self, callback: Callable) -> None:
        return self.component.forceUpdate(callback)

    @property
    def state(self) -> Dict[str, Any]:
        return self.component.state

    @state.setter
    def state(self, initial_state: Dict[str, Any]) -> None:
        self.component.state = initial_state

class PureComponent(Component):
    def __init__(self, props: Dict[str, Any], context, updater) -> None:
        self.component = __new__(React.PureComponent(props, context, updater))
        self.setState = self.component.setState.bind(self)

def destruct(dict_, *names):
    return [dict_[name] for name in names]
