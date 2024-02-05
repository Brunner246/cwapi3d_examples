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


if __name__ == '__main__':
    auto_attribute_element_ids = cadwork.get_auto_attribute_elements()

    elements = [Element(element_id) for element_id in auto_attribute_element_ids]

    [cadwork.set_auto_attribute([element.element_id], str(element.nesting_number)) for element in elements]
