# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "toga",
# ]
# ///
"""
An app to turn natural language into mathematical animations.
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from typing import Self

def greeting(name: str) -> str:
    return f"Hello, {name if name else "stranger"}!"

class mAInim(toga.App):
    def startup(self: Self) -> None:
        main_box: toga.Box = toga.Box(style=Pack(direction=COLUMN))

        name_label: toga.Label = toga.Label(
            "Your name: ",
            style=Pack(padding=(0, 5))
        )
        self.name_input: toga.TextInput = toga.TextInput(style=Pack(flex=1))

        name_box: toga.Box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button: toga.Button = toga.Button(
            "Say Hello!",
            on_press=self.say_hello,
            style=Pack(padding=5)
        )

        main_box.add(name_box)
        main_box.add(button)

        self.main_window: toga.MainWindow = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    async def say_hello(self: Self, _) -> None:
        await self.main_window.dialog(
            toga.InfoDialog(
                greeting(self.name_input.value),
                "Hi, there!",
            )
        )


def main():
    return mAInim()
