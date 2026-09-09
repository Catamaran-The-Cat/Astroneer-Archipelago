from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import AstroneerWorld

# A region is a container for locations ("checks"), which connects to other regions via "Entrance" objects.
# Many games will model their Regions after physical in-game places, but you can also have more abstract regions.
# For a location to be in logic, its containing region must be reachable.
# The Entrances connecting regions can have rules - more on that in rules.py.
# This makes regions especially useful for traversal logic ("Can the player reach this part of the map?")

# Every location must be inside a region, and you must have at least one region.
# This is why we create regions first, and then later we create the locations (in locations.py).


def create_and_connect_regions(world: AstroneerWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: AstroneerWorld) -> None:
    # Create the regions
    menu = Region("Menu", world.player, world.multiworld)
    sylva = Region("Sylva", world.player, world.multiworld)
    desolo = Region("Desolo", world.player, world.multiworld)
    calidor = Region("Calidor", world.player, world.multiworld)
    vesania = Region("Vesania", world.player, world.multiworld)
    novus = Region("Novus", world.player, world.multiworld)
    glacio = Region("Glacio", world.player, world.multiworld)
    atrox = Region("Atrox", world.player, world.multiworld)

    # Let's put all these regions in a list.
    regions = [sylva, desolo, calidor, vesania, novus, glacio, atrox]

    # Some regions may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    #if world.options.hammer:
    #    top_middle_room = Region("Top Middle Room", world.player, world.multiworld)
    #    regions.append(top_middle_room)

    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: AstroneerWorld) -> None:
    # We have regions now, but still need to connect them to each other.
    # But wait, we no longer have access to the region variables we created in create_all_regions()!
    # Luckily, once you've submitted your regions to multiworld.regions,
    # you can get them at any time using world.get_region(...).
    menu = world.get_region("Menu")
    sylva = world.get_region("Sylva")
    desolo = world.get_region("Desolo")
    calidor = world.get_region("Calidor")
    vesania = world.get_region("Vesania")
    novus = world.get_region("Novus")
    glacio = world.get_region("Glacio")
    atrox = world.get_region("Atrox")

    # Okay, now we can get connecting. For this, we need to create Entrances.
    # Entrances are inherently one-way, but crucially, AP assumes you can always return to the origin region.
    # One way to create an Entrance is by calling the Entrance constructor.
    #overworld_to_bottom_right_room = Entrance(world.player, "Overworld to Bottom Right Room", parent=overworld)
    #overworld.exits.append(overworld_to_bottom_right_room)

    # You can then connect the Entrance to the target region.
    #overworld_to_bottom_right_room.connect(bottom_right_room)

    # An even easier way is to use the region.connect helper.
    menu.connect(sylva, "Menu to Sylva")

    # The region.connect helper even allows adding a rule immediately.
    # We'll talk more about rule creation in the set_all_rules() function in rules.py.
    overworld.connect(top_left_room, "Overworld to Top Left Room", lambda state: state.has("Key", world.player))

    # Some Entrances may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # In this case, we previously created an extra "Top Middle Room" region that we now need to connect to Overworld.
    if world.options.hammer:
        top_middle_room = world.get_region("Top Middle Room")
        overworld.connect(top_middle_room, "Overworld to Top Middle Room")
