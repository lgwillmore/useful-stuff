#!/usr/bin/env python3
import subprocess

DEFAULT_VERSIONS = [
    "7.2",
    "7.3"
]

DEFAULT_MODULES = [
    "mysql",
    "cli",
    "xml"
]


def check(status_code):
    if status_code != 0:
        exit(status_code)

def install_version(version):
    php = "php{}".format(version)
    check(subprocess.call(["apt", "install", "-y", php]))
    for module in DEFAULT_MODULES:
        check(subprocess.call(["apt", "install", "-y", "{}-{}".format(php, module)]))



def install_php_alternatives(versions=None):
    check(subprocess.call(["add-apt-repository", "-y", "ppa:ondrej/php"]))
    check(subprocess.call(["apt", "update", "-y"]))
    if versions is None:
        versions = DEFAULT_VERSIONS
    for version in versions:
        install_version(version)


if __name__ == '__main__':
    install_php_alternatives()
