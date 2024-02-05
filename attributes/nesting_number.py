__author__ = 'Brunner Michael'

from typing import List

import attribute_controller as ac
import element_controller as ec
import utility_controller as uc


class Element:
    def __init__(self, element_id: int):
        if ec.check_element_id(element_id) is False:
            raise ValueError("element_id must be a valid element id")

        self.__element_id = element_id
        self.__nesting_number: str = ""

    @property
    def nesting_number(self):
        if not self.__nesting_number:
            self.__nesting_number = ac.get_associated_nesting_number(self.__element_id)
        return self.__nesting_number

    @property
    def element_id(self):
        return self.__element_id


class Panel(Element):
    def __init__(self, element_id: int):
        super().__init__(element_id)


class Beam(Element):
    def __init__(self, element_id: int):
        super().__init__(element_id)


def main():
    element_ids = ec.get_all_identifiable_element_ids()

    filtered_panel_element_ids = filter(lambda element_id: ac.get_element_type(element_id).is_panel(), element_ids)

    panels: List[Panel] = [Panel(element_id) for element_id in filtered_panel_element_ids if
                           ec.check_element_id(element_id)]

    filtered_beam_element_ids = filter(lambda element_id: ac.get_element_type(element_id).is_rectangular_beam(),
                                       element_ids)

    beams: List[Beam] = [Beam(element_id) for element_id in filtered_beam_element_ids if
                         ec.check_element_id(element_id)]

    user_attribute_nr: int = uc.get_user_int("Please enter the user attribute number for the nesting number: ")

    [ac.set_user_attribute([panel.element_id], user_attribute_nr, panel.nesting_number) for panel in panels]

    [ac.set_user_attribute([beam.element_id], user_attribute_nr, beam.nesting_number) for beam in beams]

    return exit(0)


if __name__ == '__main__':
    main()
