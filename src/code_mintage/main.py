#!/usr/bin/env python

import argparse

from colorama import Fore as Clr

import code_mintage.cpp_properties as cpp_properties
import code_mintage.jlink_scripts as jlink_scripts
import code_mintage.tasks as tasks
from code_mintage.version import VERSION

DESCRIPTION = f'VSCode mintage {Clr.GREEN}v{VERSION}{Clr.RESET}'


def main():
    print(DESCRIPTION)
    print(
        jlink_scripts.command(device="STM32F407VE",
                              path_to_exe=jlink_scripts.PATH_TO_EXE))
    print(jlink_scripts.launcher())
    tasks.create(ses_dir="SES")
    cpp_properties.get(defines=[
        "ARM_MATH_CM4", "STM32L431xx", "__STM32L431_SUBFAMILY", "__STM32L4XX_FAMILY"
    ])


if __name__ == "__main__":
    main()
