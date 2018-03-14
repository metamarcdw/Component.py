React = require("react")
from typing import Union, Dict, Any, Callable

class Component:
    isReactComponent: Dict[str, Any] = {}

    def __init__(self, props: Dict[str, Any], context, updater) -> Component:
        self.component = __new__(React.Component(props, context, updater))

    def setState(self,
                 partialState: Union[Dict[str, Any], Callable],
                 callback: Callable) -> None:
        return self.component.setState(partialState, callback)

    def forceUpdate(self, callback: Callable) -> None:
        return self.component.forceUpdate(callback)

    @property
    def state(self) -> Dict[str, Any]:
        return self.component.state
