#!/usr/bin/env python

import argparse

from colorama import Fore as Clr

from code_mintage.cpp_properties import cpp_properties
from code_mintage.jlink_scripts import (PATH_TO_EXE, jlink_command,
                                        jlink_launcher_script)
from code_mintage.tasks import build_tasks
from code_mintage.version import VERSION

DESCRIPTION = f'VSCode mintage {Clr.GREEN}v{VERSION}{Clr.RESET}'

def main():
    print(DESCRIPTION)
    print(jlink_command(device="STM32F407VE", path_to_exe=PATH_TO_EXE))
    print(jlink_launcher_script())
    build_tasks(ses_dir="SES")
    cpp_properties(defines=[
        "ARM_MATH_CM4", "STM32L431xx", "__STM32L431_SUBFAMILY", "__STM32L4XX_FAMILY"
    ])

if __name__ == "__main__":
    main()
