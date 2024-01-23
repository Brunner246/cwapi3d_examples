from typing import List

import cadwork
import element_controller as ec
import geometry_controller as gc


class Room:
    def __init__(self, element_id: int):
        self.element_id = element_id
        self.__foot_print_vertices = list()
        self.__foot_print_facet: List[cadwork.point_3d] = list()

    def get_foot_print_vertices(self):
        if not self.__foot_print_vertices:
            vertices = gc.get_element_vertices(self.element_id)
            lowest_vertex = min(vertices, key=lambda vertex: vertex.z)
            threshold = lowest_vertex.z
            self.__foot_print_vertices = [vertex for vertex in vertices
                                          if abs(vertex.z - threshold) < 1e-4]
        return self.__foot_print_vertices

    def get_foot_print_facet(self):
        facets: cadwork.facet_list = gc.get_element_facets(self.element_id)
        vertices: List[cadwork.vertex_list] = list()
        for facet in range(facets.count()):
            vertices.append(facets.get_external_polygon(facet))

        self.__foot_print_facet = min(vertices, key=lambda vertex: vertex.at(0).z)

        return [self.__foot_print_facet.at(i) for i in range(self.__foot_print_facet.count())]


if __name__ == '__main__':

    room_objects: List[int] = ec.get_user_element_ids()

    rooms: List[Room] = [Room(room_object) for room_object in room_objects]

    for room in rooms:
        [ec.create_node(cadwork.point_3d(vertex.x, vertex.y, vertex.z)) for vertex in room.get_foot_print_vertices()]
        ec.create_surface(room.get_foot_print_facet())
