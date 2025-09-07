import os

from extract_markdown import extract_title
from markdown_to_html import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print("*******************************************")
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    print("*******************************************")

    markdown = open(os.path.abspath(from_path)).read()
    template = open(os.path.abspath(template_path)).read()

    node = markdown_to_html_node(markdown)
    html = node.to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    with open(os.path.abspath(dest_path), "w") as file:
        file.write(template)
