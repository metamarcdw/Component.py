React = require("react")

def MyComponent2():
    return __pragma__("xtrans",
                      "npx babel --presets=react",
                      "{}", """
        <div className="style2">
            <h2>Heading2</h2>
            <p>Paragraph</p>
        </div>
                      """.strip())
