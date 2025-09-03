from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value of leaf node cannot be none")
        if self.tag is None:
            return self.value

        if self.props is not None:
            attributes = super().props_to_html()

            return f"<{self.tag} {attributes}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
