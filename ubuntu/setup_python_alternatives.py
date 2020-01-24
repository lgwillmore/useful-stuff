#!/usr/bin/env python3
import subprocess

# Run as sudo

VERSIONS = ["2.7", "3.7"]
MAJORS = ["", "3"]
MODULES = ["pip"]


def check(status_code):
    pass
    if status_code != 0:
        print("SOMETHING WENT WRONG")
        exit(status_code)


def install_version(version, priority):
    python = "python{}".format(version)
    check(subprocess.call(["apt", "install", "-y", python]))
    check(subprocess.call(
        ["update-alternatives", "--install", "/usr/bin/python", "python", "/usr/bin/{}".format(python), str(priority)]
    ))


def install_major_modules(major):
    for module in MODULES:
        check(subprocess.call(["apt", "install", "-y", "python{}-{}".format(major, module)]))


def install_alternatives(versions=None):
    check(subprocess.call(["apt", "update", "-y"]))
    if versions is None:
        versions = VERSIONS
    priority = 1
    for version in versions:
        install_version(version, priority)
        priority += 1
    for major in MAJORS:
        install_major_modules(major)


if __name__ == '__main__':
    install_alternatives()
