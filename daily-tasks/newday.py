#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime
from jinja2 import Environment, FileSystemLoader


BASE_DIR = Path.cwd()
COUNTER_FILE = BASE_DIR / ".counter"


def get_next_day():
    if not COUNTER_FILE.exists():
        COUNTER_FILE.write_text("0")

    current = int(COUNTER_FILE.read_text().strip())
    next_day = current + 1

    COUNTER_FILE.write_text(str(next_day))

    return next_day


def get_date():
    default = datetime.now().strftime("%d%B%y")

    date_str = input(f"Date [{default}]: ").strip()

    if not date_str:
        date_str = default

    return date_str


def create_folder_structure(folder):
    folder.mkdir(exist_ok=True)

    (folder / "screenshots").mkdir(exist_ok=True)
    (folder / "poc").mkdir(exist_ok=True)
    (folder / "notes").mkdir(exist_ok=True)
    (folder / "attachments").mkdir(exist_ok=True)


def render_templates(folder, day, date_str):
    env = Environment(
        loader=FileSystemLoader("templates")
    )

    year = datetime.now().year

    files = {
        f"Day0x{day}_{date_str}.md": (
            "day.md.j2",
            {
                "day": day,
                "date": date_str
            }
        ),

        "bugs.md": (
            "bugs.md.j2",
            {}
        ),

        "writeup_report.md": (
            "writeup_report.md.j2",
            {}
        ),

        f"cve-{year}-XXXX.md": (
            "cve.md.j2",
            {
                "year": year
            }
        ),
    }

    for filename, (template_name, context) in files.items():

        template = env.get_template(template_name)

        output_file = folder / filename

        with open(output_file, "w") as f:
            f.write(template.render(**context))


def main():
    day = get_next_day()

    date_str = get_date()

    folder_name = f"Day0x{day}"

    folder = BASE_DIR / folder_name

    create_folder_structure(folder)

    render_templates(folder, day, date_str)

    print()
    print(f"[+] Created {folder_name}")
    print(f"[+] Date: {date_str}")
    print()
    print(folder)


if __name__ == "__main__":
    main()
