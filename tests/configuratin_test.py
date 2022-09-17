import json
from dataclasses import asdict
from pathlib import Path

import src.code_mintage.cpp_properties as cpp_properties


def test_cpp_properties():
    prop = cpp_properties.get(defines=[
        "ARM_MATH_CM4", "STM32L431xx", "__STM32L431_SUBFAMILY", "__STM32L4XX_FAMILY"
    ])
    with open(Path(__file__).resolve().parent.joinpath("cpp_properties.json"), "w+") as f:
        json.dump(asdict(prop), f, indent=4)


if __name__ == "__main__":
    test_cpp_properties()
