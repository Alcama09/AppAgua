"""
My first application
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class AppAgua(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))
        commit_label = toga.Label(
            "Commit: ", 
            style=Pack(padding = (0,5))
        )
        self.text_input1 = toga.TextInput(style=Pack(flex=1))
        first_box = toga.Box(style=Pack(direction=ROW, padding = 5))
        first_box.add(commit_label)
        first_box.add(self.text_input1)
        button = toga.Button(
            "Commit",
            style=Pack(padding = 5)
        )
        main_box.add(first_box)
        main_box.add(button)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return AppAgua()
