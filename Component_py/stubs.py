from typing import Any, Callable
__pragma__: Callable[[str], None] = lambda *s: None  # __:skip
__pragma__("skip")
require: Callable[[str], Any] = lambda *s: None
class Document:
    def getElementById(self, str_): pass
document = Document()
__pragma__("noskip")
