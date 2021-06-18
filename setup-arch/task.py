from module import Module

CONFIGS = [
    '.taskrc',
]

PROGRAMS = {
    'task': 'sudo pacman -S taskwarrior-tui',
}


class Task(Module):
    def __init__(self):
        super().__init__(
            'task',
            'taskwarrior + taskwarrior-tui',
            CONFIGS,
            PROGRAMS
        )
