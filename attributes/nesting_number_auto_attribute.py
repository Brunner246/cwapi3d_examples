import attribute_controller as ac

import cadwork


class Element:
    def __init__(self, element_id: int):
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


if __name__ == '__main__':
    element_ids = cadwork.get_auto_attribute_elements()

    filtered_panel_element_ids = filter(lambda element_id: ac.get_element_type(element_id).is_panel(),
                                        element_ids)
    panels = [Panel(element_id) for element_id in filtered_panel_element_ids]

    filtered_beam_element_ids = filter(lambda element_id: ac.get_element_type(element_id).is_rectangular_beam(),
                                       element_ids)
    beams = [Beam(element_id) for element_id in filtered_beam_element_ids]

    [cadwork.set_auto_attribute([panel.element_id], str(panel.nesting_number)) for panel in panels]

    [cadwork.set_auto_attribute([beam.element_id], str(beam.nesting_number)) for beam in beams]
