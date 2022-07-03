import json
from dataclasses import asdict, dataclass, field


@dataclass
class SesTask:
    type: str = "shell"
    label: str = "Build: debug"
    command: list = field(default_factory=list)
    presentation: dict = field(default_factory=lambda: {
        "reveal": "always",
        "echo": False,
        "clear": True
    })
    group: dict = field(default_factory=lambda: {"kind": "build", "isDefault": True})
    problemMatcher: list = field(default_factory=lambda: ["$gcc"])


@dataclass
class Tasks:
    version: str = field(default="2.0.0", init=False)
    tasks: list


COMMAND = ("emBuild -threadnum 32 -config {config} "
           "-project ${{config:SES_PROJECT_NAME}} "
           "${{workspaceFolder}}/{path}/${{config:SES_PROJECT_NAME}}.emProject")


def build_tasks(ses_dir: str) -> Tasks:
    tasks = [
        SesTask(command=[COMMAND.format(config="Debug", path=ses_dir)]),
        SesTask(command=[COMMAND.format(config="Release", path=ses_dir)])
    ]
    return Tasks(tasks)
    # output = Tasks(tasks)
    # with open("tasks.json", "w+") as f:
    #     json.dump(asdict(output), f, indent=4)
