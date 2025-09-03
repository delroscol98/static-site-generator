class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("This node has not been implemented")

    def props_to_html(self):
        if type(self.props) is dict:
            res = []
            for key, value in self.props.items():
                res.append(f'{key}="{value}"')

            return " ".join(res)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
