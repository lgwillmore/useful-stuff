#!/usr/bin/env python3
import subprocess

# First run this:
#   wget -q https://packages.microsoft.com/config/ubuntu/19.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
#   sudo dpkg -i packages-microsoft-prod.deb
#
# Then run this as sudo.
#

install_and_update_deps = [
    "apt-get update".split(),
    "apt-get install -y apt-transport-https".split(),
    "apt-get update".split(),
]

dotnet_core_sdk_versions = [
    "2.1",
    "2.2",
    "3.0"
]


def check(status_code):
    pass
    if status_code != 0:
        print("SOMETHING WENT WRONG")
        exit(status_code)


def install_dotnet_sdk(version, priority):
    check(subprocess.call("apt-get install -y dotnet-sdk-{}".format(version).split()))
    check(subprocess.call("cp -rf /usr/share/dotnet /usr/share/dotnet_core_{}".format(version).split()))
    check(subprocess.call(
        "update-alternatives --install /usr/bin/dotnet dotnet /usr/share/dotnet_core_{version}/dotnet {priority}".format(
            version=version,
            priority=priority
        ).split()))


def install_dotnet_alternatives():
    for command in install_and_update_deps:
        check(subprocess.call(command))
    priority = 1
    for version in dotnet_core_sdk_versions:
        install_dotnet_sdk(version, priority)
        priority += 1


if __name__ == '__main__':
    install_dotnet_alternatives()
