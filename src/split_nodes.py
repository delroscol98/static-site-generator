from extract_markdown_images_and_links import (
    extract_markdown_images,
    extract_markdown_links,
)
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


def split_nodes_image(old_nodes):
    res = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            res.append(node)
        else:
            extracted_images = extract_markdown_images(node.text)
            if len(extracted_images) == 0:
                res.append(node)
            else:
                remaining = node.text
                for image in extracted_images:
                    alt, url = image
                    snippet = f"![{alt}]({url})"
                    before, after = remaining.split(snippet, 1)
                    if before != "":
                        res.append(TextNode(before, TextType.TEXT))
                    res.append(TextNode(alt, TextType.IMAGE, url))
                    remaining = after
                if remaining != "":
                    res.append(TextNode(remaining, TextType.TEXT))

    return res


def split_nodes_link(old_nodes):
    res = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            res.append(node)
        else:
            extracted_links = extract_markdown_links(node.text)
            if len(extracted_links) == 0:
                res.append(node)
            else:
                remaining = node.text
                for image in extracted_links:
                    alt, url = image
                    snippet = f"[{alt}]({url})"
                    before, after = remaining.split(snippet, 1)
                    if before != "":
                        res.append(TextNode(before, TextType.TEXT))
                    res.append(TextNode(alt, TextType.LINK, url))
                    remaining = after
                if remaining != "":
                    res.append(TextNode(remaining, TextType.TEXT))

    return res
