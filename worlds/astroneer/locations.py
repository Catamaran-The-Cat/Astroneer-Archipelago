from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import AstroneerWorld

# Astroneer's unique ap id
from .constants import ASTRONEER_ID

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
LOCATION_NAME_TO_ID = {
    # xx (location type)
    # 11 (missions) (it won't let me start with 01 :( )
    "Planetfall": 111 + ASTRONEER_ID, # Trailhead01_1.1
    "Astroneering Bas(e)ics": 112 + ASTRONEER_ID, # Trailhead01_1.1.1
    "Breathing Space": 113 + ASTRONEER_ID, # Trailhead01_1.1.1a
    "Resourcing": 114 + ASTRONEER_ID, # Trailhead01_1.1.1b
    "Landfilling": 115, # Trailhead01_1.1.1c
    "Printing Up": 11, # Trailhead01_1.1.1.1
    "Lights in the Distance": 116 + ASTRONEER_ID, # Mission_2-1
    "Well, That's Weird": 117 + ASTRONEER_ID, # Mission_2-2

    # 12 (gatway chambers)
    # Sylva
    "Sylva Gateway Chamber Activated x1": 121 + ASTRONEER_ID,
    "Sylva Gateway Chamber Activated x2": 122 + ASTRONEER_ID,
    "Sylva Gateway Chamber Activated x3": 123 + ASTRONEER_ID,
    "Sylva Gateway Chamber Activated x4": 124 + ASTRONEER_ID,
    "Sylva Gateway Chamber Activated x5": 125 + ASTRONEER_ID,
    "Sylva Gateway Chamber Activated x6": 126 + ASTRONEER_ID,
    # Desolo
    "Desolo Gateway Chamber Activated x1": 127 + ASTRONEER_ID,
    "Desolo Gateway Chamber Activated x2": 128 + ASTRONEER_ID,
    # Calidor
    "Calidor Gateway Chamber Activated x1": 129 + ASTRONEER_ID,
    "Calidor Gateway Chamber Activated x2": 1210 + ASTRONEER_ID,
    "Calidor Gateway Chamber Activated x3": 1211 + ASTRONEER_ID,
    "Calidor Gateway Chamber Activated x4": 1212 + ASTRONEER_ID,
    "Calidor Gateway Chamber Activated x5": 1213 + ASTRONEER_ID,
    "Calidor Gateway Chamber Activated x6": 1214 + ASTRONEER_ID,
    # Vesania
    "Vesania Gateway Chamber Activated x1": 1215 + ASTRONEER_ID,
    "Vesania Gateway Chamber Activated x2": 1216 + ASTRONEER_ID,
    "Vesania Gateway Chamber Activated x3": 1217 + ASTRONEER_ID,
    "Vesania Gateway Chamber Activated x4": 1218 + ASTRONEER_ID,
    "Vesania Gateway Chamber Activated x5": 1219 + ASTRONEER_ID,
    "Vesania Gateway Chamber Activated x6": 1220 + ASTRONEER_ID,
    # Novus
    "Novus Gateway Chamber Activated x1": 1221 + ASTRONEER_ID,
    "Novus Gateway Chamber Activated x2": 1222 + ASTRONEER_ID,
    # Glacio
    "Glacio Gateway Chamber Activated x1": 1223 + ASTRONEER_ID,
    "Glacio Gateway Chamber Activated x2": 1224 + ASTRONEER_ID,
    "Glacio Gateway Chamber Activated x3": 1225 + ASTRONEER_ID,
    "Glacio Gateway Chamber Activated x4": 1226 + ASTRONEER_ID,
    "Glacio Gateway Chamber Activated x5": 1227 + ASTRONEER_ID,
    "Glacio Gateway Chamber Activated x6": 1228 + ASTRONEER_ID,
    # Atrox
    "Atrox Gateway Chamber Activated x1": 1229 + ASTRONEER_ID,
    "Atrox Gateway Chamber Activated x2": 1230 + ASTRONEER_ID,
    "Atrox Gateway Chamber Activated x3": 1231 + ASTRONEER_ID,
    "Atrox Gateway Chamber Activated x4": 1232 + ASTRONEER_ID,
    "Atrox Gateway Chamber Activated x5": 1233 + ASTRONEER_ID,
    "Atrox Gateway Chamber Activated x6": 1234 + ASTRONEER_ID,

    # 13 (cores aka gateway engines)
    "Sylva's Core Activated": 131 + ASTRONEER_ID,
    "Desolo's Core Activated": 132 + ASTRONEER_ID,
    "Calidor's Core Activated": 133 + ASTRONEER_ID,
    "Vesania's Core Activated": 134 + ASTRONEER_ID,
    "Novus's Core Activated": 135 + ASTRONEER_ID,
    "Glacio's Core Activated": 136 + ASTRONEER_ID,
    "Atrox's Core Activated": 137 + ASTRONEER_ID,
}


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class AstroneerLocation(Location):
    game = "Astroneer"


# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: AstroneerWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: AstroneerWorld) -> None:
    # Finally, we need to put the Locations ("checks") into their regions.
    # Once again, before we do anything, we can grab our regions we created by using world.get_region()
    sylva = world.get_region("Sylva")
    desolo = world.get_region("Desolo")
    calidor = world.get_region("Calidor")
    vesania = world.get_region("Vesania")
    novus = world.get_region("Novus")
    glacio = world.get_region("Glacio")
    atrox = world.get_region("Atrox")

    # One way to create locations is by just creating them directly via their constructor.
    #bottom_left_chest = APQuestLocation(
    #    world.player, "Bottom Left Chest", world.location_name_to_id["Bottom Left Chest"], overworld
    #)

    # You can then add them to the region.
    #overworld.locations.append(bottom_left_chest)

    # A simpler way to do this is by using the region.add_locations helper.
    # For this, you need to have a dict of location names to their IDs (i.e. a subset of location_name_to_id)
    # Aha! So that's why we made that "get_location_names_with_ids" helper method earlier.
    # You also need to pass your overridden Location class.
    sylva_missions = get_location_names_with_ids(
        ["Planetfall", "Astroneering Bas(e)ics", "Breathing Space", "Resourcing", "Landfilling", "Lights in the Distance", "Well, That's Weird"]
    )
    sylva.add_locations(sylva_missions, AstroneerLocation)

    # Locations may be in different regions depending on the player's options.
    # In our case, the hammer option puts the Top Middle Chest into its own room called Top Middle Room.
    #top_middle_room_locations = get_location_names_with_ids(["Top Middle Chest"])
    #if world.options.hammer:
    #    top_middle_room = world.get_region("Top Middle Room")
    #    top_middle_room.add_locations(top_middle_room_locations, APQuestLocation)
    #else:
    #    overworld.add_locations(top_middle_room_locations, APQuestLocation)

    # Locations may exist only if the player enables certain options.
    # In our case, the extra_starting_chest option adds the Bottom Left Extra Chest location.
    #if world.options.extra_starting_chest:
        # Once again, it is important to stress that even though the Bottom Left Extra Chest location doesn't always
        # exist, it must still always be present in the world's location_name_to_id.
        # Whether the location actually exists in the seed is purely determined by whether we create and add it here.
    #    bottom_left_extra_chest = get_location_names_with_ids(["Bottom Left Extra Chest"])
    #    overworld.add_locations(bottom_left_extra_chest, APQuestLocation)


def create_events(world: AstroneerWorld) -> None:
    pass

    # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # In our case, the player must press a button in the top left room to open the final boss door.
    # AP has something for this purpose: "Event locations" and "Event items".
    # An event location is no different than a regular location, except it has the address "None".
    # It is treated during generation like any other location, but then it is discarded.
    # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
    #top_left_room = world.get_region("Top Left Room")
    #final_boss_room = world.get_region("Final Boss Room")

    # One way to create an event is simply to use one of the normal methods of creating a location.
    #button_in_top_left_room = APQuestLocation(world.player, "Top Left Room Button", None, top_left_room)
    #top_left_room.locations.append(button_in_top_left_room)

    # We then need to put an event item onto the location.
    # An event item is an item whose code is "None" (same as the event location's address),
    # and whose classification is "progression". Item creation will be discussed more in items.py.
    # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
    # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
    # it is common practice to create the item when creating the location.
    # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
    # we'll create both the event location and the event item in our locations.py code.
    #button_item = items.APQuestItem("Top Left Room Button Pressed", ItemClassification.progression, None, world.player)
    #button_in_top_left_room.place_locked_item(button_item)

    # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
    # Luckily, we have another event we want to create: The Victory event.
    # We will use this event to track whether the player can win the game.
    # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
    #final_boss_room.add_event(
    #    "Final Boss Defeated", "Victory", location_type=APQuestLocation, item_type=items.APQuestItem
    #)

    # If you create all your regions and locations line-by-line like this,
    # the length of your create_regions might get out of hand.
    # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
    # However, it is worth understanding how the actual creation of regions and locations works,
    # That way, we're not just mindlessly copy-pasting! :)
