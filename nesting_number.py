__author__ = 'Brunner Michael'

from typing import List

import attribute_controller as ac
import cadwork
import element_controller as ec
import utility_controller as uc


class Panel:
    def __init__(self, element_id: int):
        if ec.check_element_id(element_id) is False:
            raise ValueError("element_id must be a valid element id")

        self.__element_id = element_id
        self.__nesting_number: str = ac.get_associated_nesting_number(self.__element_id)

    @property
    def nesting_number(self):
        return self.__nesting_number

    @property
    def element_id(self):
        return self.__element_id


def main():
    element_ids = ec.get_all_identifiable_element_ids()
    # filter just the panels
    filtered_element_ids = filter(lambda element_id: ac.get_element_type(element_id).is_panel(), element_ids)
    try:
        panels: List[Panel] = [Panel(element_id) for element_id in filtered_element_ids]
    except ValueError as e:
        print(e)
        return exit(1)

    user_attribute_nr: int = uc.get_user_int("Please enter the user attribute number for the nesting number: ")

    for panel in panels:
        print(panel.nesting_number)
        ac.set_user_attribute([panel.element_id], user_attribute_nr, panel.nesting_number)

    return exit(0)


if __name__ == '__main__':
    main()
