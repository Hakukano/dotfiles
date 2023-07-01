import sys

from prompt_toolkit import print_formatted_text, prompt, PromptSession
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.formatted_text import HTML

from tabulate import tabulate

from arch.install import MODULES as arch_modules
from debian.install import MODULES as debian_modules
from macos.install import MODULES as macos_modules
from pop.install import MODULES as pop_modules

if len(sys.argv) < 2:
    print(f'Wrong arguments number: {sys.argv}')
    exit(1)

os_name = sys.argv[1]

MODULES = {}
if os_name == 'arch':
    MODULES = arch_modules
elif os_name == 'debian':
    MODULES = debian_modules
elif os_name == 'macos':
    MODULES = macos_modules
elif os_name == 'pop':
    MODULES = pop_modules
else:
    print(f'Unknown OS type {os_name}')
    exit(2)

MODULE_TABLE_HEADER = [
    'Name',
    'Description',
    'Status',
    'Installed',
]


def modules_to_table():
    rows = []
    for module in MODULES.values():
        rows.append(module.to_brief_row())
    return tabulate(rows, headers=MODULE_TABLE_HEADER)


def modules_to_completion():
    completion = {}
    for key in MODULES.keys():
        completion[key] = None
    return completion


PROMT_CMD = HTML('<orange>cmd</orange> => ')

INTRO = HTML('''
    <cyan>Welcome to Hakukano's dotfiles setup for Arch Linux!</cyan>
    <br/>
    <p>Enter <b>help</b> to see available commands</p>
''')

HELP = HTML('''
    <cyan>Available Commands</cyan>
    <br/>
    <b>help</b> => Show this page
    <b>mods</b> => Module related commands
        <b>list</b> => List all modules
        <b>desc</b> => Describe a module
            <i>module</i> => Module name
        <b>inst</b> => Install a module
                => Install all modules
            <i>module</i> => Module name
    <b>exit</b> => Exit this setup
''')

INVALID_CMD = HTML('''
    <red>Invalid Command!</red>
''')

OUTRO = HTML('''
    <cyan>Goodbye!</cyan>
''')

COMPLETER = NestedCompleter.from_nested_dict({
    'help': None,
    'mods': {
        'list': None,
        'desc': modules_to_completion(),
        'inst': modules_to_completion(),
    },
    'exit': None,
})


def handle_help(cmds):
    print_formatted_text(HELP)


def handle_mods_list(cmds):
    print('')
    print(modules_to_table())
    print('')


def handle_mods_desc(cmds):
    if len(cmds) == 0 or cmds[0] not in MODULES:
        print_formatted_text(INVALID_CMD)
        return
    mod = cmds[0]
    print('')
    print(MODULES[mod].describe())
    print('')


def handle_mods_inst(cmds):
    if len(cmds) == 0:
        confirm = prompt(
            HTML(
                '<red>Are you sure to install all modules? '
                'It will override everthing '
                'without further confirmation!</red> (y|n) => '
            )
        )
        if confirm == 'y':
            pass
        else:
            return
        for module in MODULES.values():
            print('')
            module.install()
            print('')
    else:
        mod = cmds[0]
        if mod not in MODULES:
            print_formatted_text(INVALID_CMD)
            return
        if MODULES[mod].installed():
            confirm = prompt(
                HTML(
                    '<b>{}</b> is fully installed, '
                    'do you want to reinstall it? (y|n) => '.format(
                        mod
                    )
                )

            )
            if confirm == 'y':
                pass
            else:
                return
        print('')
        MODULES[mod].install()
        print('')


def handle_mods(cmds):
    if len(cmds) == 0:
        print_formatted_text(INVALID_CMD)
        return
    cmd_base = cmds[0]
    cmd_rest = cmds[1:]
    if cmd_base == 'list':
        handle_mods_list(cmd_rest)
    elif cmd_base == 'desc':
        handle_mods_desc(cmd_rest)
    elif cmd_base == 'inst':
        handle_mods_inst(cmd_rest)
    else:
        print_formatted_text(INVALID_CMD)
        return


def main():
    print_formatted_text(INTRO)
    session = PromptSession()
    while True:
        cmds = session.prompt(PROMT_CMD, completer=COMPLETER).split()
        if len(cmds) == 0:
            continue
        cmd_base = cmds[0]
        cmd_rest = cmds[1:]
        if cmd_base == 'help':
            handle_help(cmd_rest)
        elif cmd_base == 'mods':
            handle_mods(cmd_rest)
        elif cmd_base == 'exit':
            break
        else:
            print_formatted_text(INVALID_CMD)
            continue
    print_formatted_text(OUTRO)


if __name__ == "__main__":
    main()
