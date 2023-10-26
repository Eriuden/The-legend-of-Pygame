from csv import reader
from os import walk
import pygame

def import_csv_layout(path):

    terrain_map=[]

    with open(path) as level_map:
        layout = reader(level_map, delimiter= ",")
        for row in layout:
            terrain_map(list(row))
        return terrain_map

def import_folder(path):

    surface_list = []

    for img_files in walk(path):
        for image in img_files:
            full_path = path + "/" + image
            image_surface = pygame.image.load(full_path).pygame.Surface.convert_alpha()()
            surface_list.append(image_surface)

    return surface_list

import_folder("../graphics/Grass")