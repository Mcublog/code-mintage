#!/usr/bin/env python

import argparse

from colorama import Fore as Clr

from code_mintage.jlink_command import (PATH_TO_EXE, build_jlink_command,
                                        build_jlink_launcher_script)
from code_mintage.version import VERSION

DESCRIPTION = f'VSCode mintage {Clr.GREEN}v{VERSION}{Clr.RESET}'

def main():
    print(DESCRIPTION)
    print(build_jlink_command(device="STM32F407VE", path_to_exe=PATH_TO_EXE))
    print(build_jlink_launcher_script())


if __name__ == "__main__":
    main()
