import json
from dataclasses import asdict
from pathlib import Path

import src.code_mintage.tasks as tasks


def test_task_creation():
    task = tasks.create(ses_dir="SES")
    with open(Path(__file__).resolve().parent.joinpath("tasks.json"), "w+") as f:
        json.dump(asdict(task), f, indent=4)


if __name__ == "__main__":
    test_task_creation()
