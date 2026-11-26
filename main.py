"""One-line joke entry for the "Make the Judge Laugh in One Line" bounty.

The whole point of this program is tiny: take a single funny sentence
about a dieting smart fridge and save it where the bounty expects it,
in entry.txt. Nothing fancy — just the Python standard library, no
third-party packages, no network calls.
"""

import os

LINE = (
    "I told my smart fridge I'm on a diet - now it hides the ice cream "
    "behind the vegetables and judges me in Celsius."
)


def validate(text):
    """Make sure the joke is fit to submit.

    A valid joke is a plain string on exactly one line, written in
    ASCII, between 1 and 200 characters long, with real content in it
    (not just blanks), and with no stray spaces at the edges or
    doubled up inside. Anything off spec raises ValueError.
    """
    if type(text) is not str:
        raise ValueError("joke must be a string")
    if len(text) < 1 or len(text) > 200:
        raise ValueError("joke must be between 1 and 200 characters")
    for ch in text:
        if ch == "\n" or ch == "\r":
            raise ValueError("joke must fit on a single line")
        if ord(ch) > 127:
            raise ValueError("joke must use ASCII characters only")
    if text.strip() == "":
        raise ValueError("joke cannot be blank or whitespace only")
    if text.startswith(" ") or text.endswith(" "):
        raise ValueError("joke cannot start or end with a space")
    if text.find("  ") != -1:
        raise ValueError("joke cannot contain two spaces in a row")
    return text


def main():
    """Check the joke, then drop it into entry.txt and echo it.

    The destination folder comes from MAKEFUN_OUTPUT_DIR and falls
    back to /output when that variable is not set. The folder is
    created on the fly if it is missing, and the file always ends
    with a trailing newline.
    """
    checked = validate(LINE)
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not os.path.isdir(folder):
        os.makedirs(folder)
    target = os.path.join(folder, "entry.txt")
    handle = open(target, "w", encoding="utf-8")
    try:
        handle.write(checked + "\n")
    finally:
        handle.close()
    print(checked)


if __name__ == "__main__":
    main()
