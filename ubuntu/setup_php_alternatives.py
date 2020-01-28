#!/usr/bin/env python3
import subprocess

VERSIONS = [
    "7.2",
    "7.3"
]

DEFAULT_MODULES = [
    "mbstring",
    "curl",
    "mysql",
    "cli",
    "xml"
]


def check(status_code):
    if status_code != 0:
        print("SOMETHING WENT WRONG")
        exit(status_code)


def install_composer(version, priority):
    php = "/usr/bin/php{}".format(version)
    temp_setup = "/tmp/composer{}-setup.php".format(version)
    composer_file_name = "composer{}".format(version)
    check(subprocess.call([php, "-r", "copy('https://getcomposer.org/installer', '{}');".format(temp_setup)]))
    check(subprocess.call([php, temp_setup, "--install-dir=/usr/bin", "--filename={}".format(composer_file_name)]))
    check(subprocess.call(
        ["update-alternatives", "--install", "/usr/bin/composer", "composer", "/usr/bin/{}".format(composer_file_name), str(priority)]
    ))
    check(subprocess.call([php, "-r", "unlink('{}');".format(temp_setup)]))


def install_version(version, priority):
    php = "php{}".format(version)
    check(subprocess.call(["apt", "install", "-y", php]))
    install_composer(version, priority)
    for module in DEFAULT_MODULES:
        check(subprocess.call(["apt", "install", "-y", "{}-{}".format(php, module)]))


def install_php_alternatives():
    check(subprocess.call(["add-apt-repository", "-y", "ppa:ondrej/php"]))
    check(subprocess.call(["apt", "update", "-y"]))
    priority = 0
    for version in VERSIONS:
        install_version(version, priority)
        priority += 1


if __name__ == '__main__':
    install_php_alternatives()
