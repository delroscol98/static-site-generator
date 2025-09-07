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

    abs_dest_path = os.path.abspath(dest_path)
    parent_path = os.path.dirname(abs_dest_path)

    os.makedirs(parent_path, exist_ok=True)

    with open(os.path.abspath(dest_path), "w") as file:
        file.write(template)


def generate_pages_recursive(source_dir_path, template_path, dest_dir_path):
    source_path = os.path.abspath(source_dir_path)
    source_path_contents = os.listdir(source_path)

    for content in source_path_contents:
        content_path = os.path.join(source_path, content)
        from_path = os.path.join(source_dir_path, content)
        dest_path = os.path.join(dest_dir_path, content)
        if os.path.isfile(content_path):
            name, extension = os.path.splitext(content)
            if extension == ".md" or extension == ".markdown":
                generate_page(from_path, template_path, f"{dest_dir_path}/{name}.html")
        elif os.path.isdir(content_path):
            generate_pages_recursive(from_path, template_path, dest_path)
