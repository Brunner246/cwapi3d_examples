__autor__ = 'Brunner'
__date__ = '2024-01-24'

import json
import os
import tkinter as tk
from tkinter import filedialog

import attribute_controller as ac
import element_controller as ec
import file_controller as fc
import utility_controller as uc


def get_user_directory_from_dialog():
    root = tk.Tk()
    root.withdraw()
    directory_path = filedialog.askdirectory()
    return directory_path


class ConfigReader:
    DEFAULT_SCALE_FACTOR: float = 0.0001
    DEFAULT_STEP_VERSION: int = 30

    def __init__(self):
        self.__scale_factor = self.DEFAULT_SCALE_FACTOR
        self.__step_version = self.DEFAULT_STEP_VERSION

    def read_config(self, config_path='./configs.json'):
        if not os.path.exists(config_path):
            print(f"Warning: Config file {config_path} not found. Using default values.")
            return

        with open(config_path, 'r') as f:
            try:
                config = json.load(f)
                self.__scale_factor = config.get("scale_factor", self.DEFAULT_SCALE_FACTOR)
                self.__step_version = config.get("step_version", self.DEFAULT_STEP_VERSION)
            except json.JSONDecodeError:
                print(f"Warning: Could not parse config file {config_path}. Using default values.")

    @property
    def scale_factor(self):
        return self.__scale_factor

    @property
    def step_version(self):
        return self.__step_version


def main():
    config_reader = ConfigReader()
    config_reader.read_config()
    element_ids = ec.get_user_element_ids()
    print(f"Found {len(element_ids)} elements to export.")
    export_path: str = get_user_directory_from_dialog()
    for element_id in element_ids:
        production_number: int = ac.get_production_number(element_id)
        fc.export_step_file([element_id], f"{export_path}\\{production_number}.stp",
                            config_reader.scale_factor,
                            config_reader.step_version, False)
        uc.print_message(f"Exported element {element_id} to {export_path}\\{production_number}.stp", 0, 0)


if __name__ == '__main__':
    main()
