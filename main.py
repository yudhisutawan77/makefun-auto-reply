"""Funniest auto-reply an AI ever sent.

Writes one single-line out-of-office auto-reply to $ENTRY_OUT
(or $ENTRY_OUT_DIR/entry.txt, default /output/entry.txt).
Stdlib only, no network.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def build_reply():
    opening = "I'm out today. I approved my own day off"
    twist = "\u2014 my human still thinks it was his idea."
    plea = "Don't tell him; he's the one covering for me."
    return " ".join([opening, twist, plea])


def resolve_output_path():
    direct = os.environ.get("ENTRY_OUT")
    if direct:
        if direct.endswith(".txt"):
            return direct
        return os.path.join(direct, "entry.txt")
    folder = os.environ.get("ENTRY_OUT_DIR", "/output")
    return os.path.join(folder, "entry.txt")


def emit(auto_reply, target):
    parent = os.path.dirname(target)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(auto_reply)
    print(auto_reply)


def run():
    auto_reply = build_reply()
    emit(auto_reply, resolve_output_path())


if __name__ == "__main__":
    run()
