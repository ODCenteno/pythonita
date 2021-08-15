"""Muralla China Y La Luna
La famosa muralla china tiene 11 000 m de largo, de 5 a 8 metros de altura y 6 metros en la parte inferior,
hasta 5 metros la parte superior. Tiene 67 torres de vigilancia y se encuentra a 980 metros sobre el nivel del mar.

La luna es el único satélite natural de la Tierra. Con un diámetro ecuatorial de 3476 Km,
es el quinto satélite más grande del sistema solar. Está a una distancia 384,400 Km del planeta tierra.

¿Cuántas murallas chinas necesitaríamos para darle la vuelta completa a la luna?

¿Cuántas torres de vigilancias tendría en total la muralla alrededor de la luna?
"""

from math import pi

wall_length_km = 11
wall_towers = 67

moon_diameter_km = 3476

moon_perimeter_km = moon_diameter_km * pi

walls_to_moon = moon_perimeter_km / wall_length_km
print(f"Number of Chineses walls needed to round the moon: {round(walls_to_moon)}")

towers_on_moon = walls_to_moon * wall_towers
print(f"Number of tower on the moon: {round(towers_on_moon)}")
