from enum import Enum

from leafnode import LeafNode

TextType = Enum("TextType", ["TEXT", "BOLD", "ITALIC", "CODE", "LINK", "IMAGE"])


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    text_type = text_node.text_type
    text = text_node.text
    url = text_node.url
    if text_type == TextType.TEXT:
        return LeafNode(None, text)
    if text_type == TextType.BOLD:
        return LeafNode("b", text)
    if text_type == TextType.ITALIC:
        return LeafNode("i", text)
    if text_type == TextType.CODE:
        return LeafNode("code", text)
    if text_type == TextType.LINK:
        return LeafNode("a", text, {"href": url})
    if text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": url, "alt": text})
    raise TypeError("text_type must be a TextType member")
