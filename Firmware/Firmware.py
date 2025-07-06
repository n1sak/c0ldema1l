import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D0, board.D1, board.D2, board.D3, board.D4, board.D5]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        # Key 0 - Personal intro / passion statement
        KC.MACRO(
            "tidr;\n"
            "I love everything about what (Company) is doing. I don't have many hobbies outside coding. "
            "I am not athletic, bad at singing, don't drink, can't dance. Building is the only thing I am good at. "
            "At this point, I want to be a part of taking something from 0 -> 1 or 1 -> 100. I just want to be heads down chasing that goal\n\n"
        ),

        # Key 1 - Greeting + interest + relevant experience summary
        KC.MACRO(
            "Hi (Name),\n"
            "Really loved what you were building at (Company) and wanted to reach out to see if there were any openings for Engineers in the early team. "
            "I have (X) years of relevant experience building full-stack applications primarily data-driven at (Previous Companies/Projects), "
            "often on early teams where I helped scale internal systems to thousands of users.\n\n"
        ),

        # Key 2 - Skills & systems overview in Soham style
        KC.MACRO(
            "Being part of super lean teams, one of my strongest suits has been the ability to work across the stack—from building scalable backend systems "
            "to high-throughput data ingestion pipelines and production-grade frontend components in React. "
            "I have built end-to-end systems involving UI (Next.js), Backend (Python, Node, Go services using GraphQL and gRPC), and infrastructure "
            "(AWS, GCP on Kubernetes), from complex workflows and DAG visualizations to drag-and-drop component canvases.\n\n"
        ),

        # Key 3 - Closing interest + cultural fit
        KC.MACRO(
            "I would love to be part of the early team at (Company) and help define its work and culture. Looking forward to hearing from you soon!\n\n"
        ),

        # Key 4 - Sign off
        KC.MACRO(
            "Best,\n"
            "(Your Name)\n"
        ),

        # Key 5 - Full email all together (for convenience)
        KC.MACRO(
            "tidr;\n"
            "I love everything about what (Company) is doing. I don't have many hobbies outside coding. "
            "I am not athletic, bad at singing, don't drink, can't dance. Building is the only thing I am good at. "
            "At this point, I want to be a part of taking something from 0 -> 1 or 1 -> 100. I just want to be heads down chasing that goal\n\n"
            "Hi (Name),\n"
            "Really loved what you were building at (Company) and wanted to reach out to see if there were any openings for Engineers in the early team. "
            "I have (X) years of relevant experience building full-stack applications primarily data-driven at (Previous Companies/Projects), "
            "often on early teams where I helped scale internal systems to thousands of users.\n\n"
            "Being part of super lean teams, one of my strongest suits has been the ability to work across the stack—from building scalable backend systems "
            "to high-throughput data ingestion pipelines and production-grade frontend components in React. "
            "I have built end-to-end systems involving UI (Next.js), Backend (Python, Node, Go services using GraphQL and gRPC), and infrastructure "
            "(AWS, GCP on Kubernetes), from complex workflows and DAG visualizations to drag-and-drop component canvases.\n\n"
            "I would love to be part of the early team at (Company) and help define its work and culture. Looking forward to hearing from you soon!\n\n"
            "Best,\n"
            "(Your Name)\n"
        ),
    ]
]

# Combos sending main URLs as text
keyboard.combos = {
    (0, 1): KC.MACRO("https://linkedin.com\n"),
    (0, 2): KC.MACRO("https://github.com\n"),
    (1, 2): KC.MACRO("https://discord.com\n"),
    (2, 3): KC.MACRO("https://sheets.google.com\n"),
}

if __name__ == '__main__':
    keyboard.go()
