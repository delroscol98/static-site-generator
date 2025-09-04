from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    res = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            res.append(node)
        else:
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise ValueError("There is a missing delimiter in markdown syntax")
            for i in range(len(parts)):
                if parts[i] == "":
                    continue
                if i % 2 == 0:
                    res.append(TextNode(parts[i], TextType.TEXT))
                else:
                    res.append(TextNode(parts[i], text_type))

    return res
