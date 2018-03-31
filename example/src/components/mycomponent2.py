from Component_py.stubs import require  # __:skip
React = require("react")

def MyComponent2():
    return __pragma__("xtrans", None, "{}", """ (
        <div className="style2">
            <h2>Heading2</h2>
            <p>Paragraph</p>
        </div>
    ); """)
