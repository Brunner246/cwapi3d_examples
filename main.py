from typing import List

import cadwork
import element_controller as ec
import geometry_controller as gc


class Room:
    def __init__(self, element_id: int):
        self.__element_id = element_id
        self.__foot_print_vertices = list()

    def get_foot_print_vertices(self):
        if not self.__foot_print_vertices:
            self.__foot_print_vertices = gc.get_element_vertices(self.element_id)
            sorted(self.__foot_print_vertices, key=lambda vertex: vertex.z)
            threshold = self.__foot_print_vertices[0].z
            self.__foot_print_vertices = [vertex for vertex in self.__foot_print_vertices
                                          if (abs(vertex.z) - threshold) < 1e-4]

        return self.__foot_print_vertices

    @property
    def element_id(self):
        return self.__element_id

    @element_id.setter
    def element_id(self, element_id):
        self.__element_id = element_id


room_objects: List[int] = ec.get_user_element_ids()

rooms: List[Room] = list()
for room_object in room_objects:
    rooms.append(Room(room_object))

for room in rooms:
    print(room.get_foot_print_vertices())
    [ec.create_node(cadwork.point_3d(vertex.x, vertex.y, vertex.z)) for vertex in room.get_foot_print_vertices()]
