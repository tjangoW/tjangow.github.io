#!python3
from datetime import datetime


def generate_from_template(title: str):
    with open("template/_template.md", "r") as f:
        template_str = f.read()

    template_str = template_str.format(title=title)

    now = datetime.now()
    new_filename = "_posts/{y}-{m:02d}-{d:02d}-{title}.md".format(y=now.year, m=now.month, d=now.day,
                                                                 title=title.lower().strip().replace(" ", "-"))

    with open(new_filename, "w") as f:
        f.write(template_str)
        print("File \"{}\" has been created successfully. Exiting...".format(new_filename))


if __name__ == "__main__":
    title = input(
        "Please enter topic name (with spaces and without date):\n>>")
    generate_from_template(title)
