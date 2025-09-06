import os
import shutil


def copy_to_destination(source_path, destination_path):
    source_path_contents = os.listdir(source_path)
    for content in source_path_contents:
        new_path = os.path.join(source_path, content)
        if os.path.isfile(new_path):
            shutil.copy(new_path, destination_path)
        elif os.path.isdir(new_path):
            new_destination_path = os.path.join(destination_path, content)
            os.mkdir(new_destination_path)
            copy_to_destination(new_path, new_destination_path)


def copy_source_to_dest(source_dir, destination_dir):
    # Clean destination directory
    destination_path = os.path.abspath(destination_dir)
    if not os.path.exists(destination_path):
        raise ValueError("Destination directory does not exist")

    shutil.rmtree(destination_path)

    # Recreate destination directory
    source_path = os.path.abspath(source_dir)
    root_dir = os.path.dirname(source_path)
    destination_path = os.path.join(root_dir, destination_dir)
    os.mkdir(destination_path)

    # Recursively copy files to destination directory
    copy_to_destination(source_path, destination_path)


def main():
    copy_source_to_dest("static", "public")


main()
