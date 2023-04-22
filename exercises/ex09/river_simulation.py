"""River simulationi with bears and fish."""

__author__ = "730465832"

from river import River

my_river: River = River(num_fish=10, num_bears=2)

my_river.one_river_week()