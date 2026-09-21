from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import AstroneerWorld

# Astroneer's unique ap id
from .constants import ASTRONEER_ID

# Every item must have a unique integer ID associated with it.
# We will have a lookup from item name to ID here that, in world.py, we will import and bind to the world class.
# Even if an item doesn't exist on specific options, it must be present in this lookup.
ITEM_NAME_TO_ID = {
    # xx (item type)
    # 11 (Filler) (we start at 11 because 01 is just 1)
    "Compound": 121 + ASTRONEER_ID,

    # 12 (traps)

    # 13 (research catalog items)
    # Tier 1
    "Small Printer": 131 + ASTRONEER_ID, # unlocked by default
    "Packager": 132 + ASTRONEER_ID,
    "Leveling Block": 133 + ASTRONEER_ID,
    "Tethers": 134 + ASTRONEER_ID, # unlocked by default
    "Oxygen Filters": 135 + ASTRONEER_ID, # unlocked by default
    "Oxygen Tank": 136 + ASTRONEER_ID,
    "Portable Oxygenator": 137 + ASTRONEER_ID,
    "Small Canister": 138 + ASTRONEER_ID, # unlocked by default
    "Beacon": 139 + ASTRONEER_ID, # unlocked by default
    "Worklight": 1310 + ASTRONEER_ID, # unlocked by default
    "Glowsticks": 1311 + ASTRONEER_ID,
    "Floodlight": 1312 + ASTRONEER_ID,
    "Small Generator": 1313 + ASTRONEER_ID, # unlocked by default
    "Power Cells": 1314 + ASTRONEER_ID,
    "Small Solar": 1315 + ASTRONEER_ID,
    "Small Wind Turbine": 1316 + ASTRONEER_ID,
    "Small Battery": 1317 + ASTRONEER_ID,
    "Boost Mod": 1318 + ASTRONEER_ID,
    "Wide Mod": 1319 + ASTRONEER_ID,
    "Narrow Mod": 1320 + ASTRONEER_ID,
    "Inhibitor Mod": 1321 + ASTRONEER_ID,
    "Alignment Mod": 1322 + ASTRONEER_ID,
    "Drill Mod 1": 1323 + ASTRONEER_ID,
    "Drill Mod 2": 1324 + ASTRONEER_ID,
    "Drill Mod 3": 1325 + ASTRONEER_ID,
    "Dynamite": 1326 + ASTRONEER_ID,
    "Fireworks": 1327 + ASTRONEER_ID,
    "Small Camera": 1328 + ASTRONEER_ID,
    "Small Trumpet Horn": 1329 + ASTRONEER_ID,
    "Holographic Figurine": 1330 + ASTRONEER_ID,
    "Terrain Analyzer": 1331 + ASTRONEER_ID,
    "Probe Scanner": 1332 + ASTRONEER_ID,
    "Solid-Fuel Jump Set": 1333 + ASTRONEER_ID,
    "Hydrazine Jet Pack": 1334 + ASTRONEER_ID,
    "Hoverboard": 1335 + ASTRONEER_ID, # mission unlocked
    # Tier 2
    "Medium Printer": 1336 + ASTRONEER_ID, # unlocked by default
    "Oxygenator": 1337 + ASTRONEER_ID,
    "Medium Shredder": 1338 + ASTRONEER_ID,
    "Field Shelter": 1339 + ASTRONEER_ID,
    "Auto Arm": 1340 + ASTRONEER_ID,
    "Medium Resource Canister": 1341 + ASTRONEER_ID,
    "Medium Fluid & Soil Canister": 1342 + ASTRONEER_ID,
    "Medium Gas Canister": 1343 + ASTRONEER_ID,
    "Power Sensor": 1344 + ASTRONEER_ID,
    "Storage Sensor": 1345 + ASTRONEER_ID,
    "Battery Sensor": 1346 + ASTRONEER_ID,
    "Button Repeater": 1347 + ASTRONEER_ID,
    "Proximity Repeater": 1348 + ASTRONEER_ID,
    "Delay Repeater": 1349 + ASTRONEER_ID,
    "Count Repeater": 1350 + ASTRONEER_ID,
    "Power Extenders": 1351 + ASTRONEER_ID,
    "Power Switch": 1352 + ASTRONEER_ID,
    "Splitter": 1353 + ASTRONEER_ID,
    "Medium Generator": 1354 + ASTRONEER_ID,
    "Medium Solar Panel": 1355 + ASTRONEER_ID,
    "Medium Wind Turbine": 1356 + ASTRONEER_ID,
    "Medium Battery": 1357 + ASTRONEER_ID,
    "RTG": 1358 + ASTRONEER_ID,
    "Medium Platform A": 1359 + ASTRONEER_ID, # unlocked by default
    "Medium Platform B": 1360 + ASTRONEER_ID,
    "Medium Platform C": 1361 + ASTRONEER_ID,
    "Tall Platform": 1362 + ASTRONEER_ID,
    "Medium Storage": 1363 + ASTRONEER_ID, # unlocked by default
    "Medium Storage Silo": 1364 + ASTRONEER_ID,
    "Tall Storage": 1365 + ASTRONEER_ID,
    "Rover Seat": 1366 + ASTRONEER_ID, # unlocked by default
    "Tractor": 1367 + ASTRONEER_ID,
    "Trailer": 1368 + ASTRONEER_ID,
    "Medium Buggy Horn": 1369 + ASTRONEER_ID,
    "Winch": 1370 + ASTRONEER_ID,
    "Paver": 1371 + ASTRONEER_ID,
    "Drill Strength 1": 1372 + ASTRONEER_ID,
    "Drill Strength 2": 1373 + ASTRONEER_ID,
    "Drill Strength 3": 1374 + ASTRONEER_ID,
    "Solid-Fuel Thruster": 1375 + ASTRONEER_ID,
    "Hydrazine Thruster": 1376 + ASTRONEER_ID,
    "Rail Post Bundle": 1377 + ASTRONEER_ID,
    "Tall Rail Post Bundle": 1378 + ASTRONEER_ID,
    "Rail Junction Bundle": 1379 + ASTRONEER_ID,
    # Tier 3
    "Large Printer": 1380 + ASTRONEER_ID, # unlocked by default
    "Smelting Furnace": 1381 + ASTRONEER_ID,
    "Soil Centrifuge": 1382 + ASTRONEER_ID,
    "Chemistry Lab": 1383 + ASTRONEER_ID,
    "Atmospheric Condenser": 1384 + ASTRONEER_ID,
    "Research Chamber": 1385 + ASTRONEER_ID, # unlocked by default
    "EXO Request Platform": 1386 + ASTRONEER_ID, # unlocked by default and might not be relevent to a randomizer
    "Trade Platform": 1387 + ASTRONEER_ID,
    "Large Shredder": 1388 + ASTRONEER_ID,
    "Large Solar Panel": 1389 + ASTRONEER_ID,
    "Large Wind Turbine": 1390 + ASTRONEER_ID,
    "Large Platform A": 1391 + ASTRONEER_ID, # unlocked by default
    "Large Platform B": 1392 + ASTRONEER_ID,
    "Large Platform C": 1393 + ASTRONEER_ID,
    "Large T-Platform": 1394 + ASTRONEER_ID,
    "Large Curved Platform": 1395 + ASTRONEER_ID,
    "Large Extended Platform": 1396 + ASTRONEER_ID,
    "Large Resouce Canister": 1397 + ASTRONEER_ID,
    "Large Storage": 1398 + ASTRONEER_ID,
    "Large Storage Silo A": 1399 + ASTRONEER_ID,


    "Small Shuttle": 130002,
}

# Items should have a defined default classification.
# In our case, we will make a dictionary from item name to classification.
DEFAULT_ITEM_CLASSIFICATIONS = {
    "Compound": ItemClassification.filler,
    "Floodlight": ItemClassification.filler,
    "Small Shuttle": ItemClassification.progression,
    "Large Printer": ItemClassification.progression,
    "Solid-Fuel Thruster": ItemClassification.progression,
    "Smelting Furnace": ItemClassification.progression,
    "Small Solar": ItemClassification.progression | ItemClassification.useful,
}


# Each Item instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Item class and override the "game" field.
class AstroneerItem(Item):
    game = "Astroneer"


# Ontop of our regular itempool, our world must be able to create arbitrary amounts of filler as requested by core.
# To do this, it must define a function called world.get_filler_item_name(), which we will define in world.py later.
# For now, let's make a function that returns the name of a random filler item here in items.py.
def get_random_filler_item_name(world: AstroneerWorld) -> str:
    # APQuest has an option called "trap_chance".
    # This is the percentage chance that each filler item is a Math Trap instead of a Confetti Cannon.
    # For this purpose, we need to use a random generator.

    # IMPORTANT: Whenever you need to use a random generator, you must use world.random.
    # This ensures that generating with the same generator seed twice yields the same output.
    # DO NOT use a bare random object from Python's built-in random module.
    #if world.random.randint(0, 99) < world.options.trap_chance:
    #    return "Math Trap"
    return "Compound"


def create_item_with_correct_classification(world: AstroneerWorld, name: str) -> AstroneerItem:
    # Our world class must have a create_item() function that can create any of our items by name at any time.
    # So, we make this helper function that creates the item by name with the correct classification.
    # Note: This function's content could just be the contents of world.create_item in world.py directly,
    # but it seemed nicer to have it in its own function over here in items.py.
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    # It is perfectly normal and valid for an item's classification to differ based on the player's options.
    # In our case, Health Upgrades are only relevant to logic (and thus labeled as "progression") in hard mode.
    #if name == "Health Upgrade" and world.options.hard_mode:
        #classification = ItemClassification.progression

    return AstroneerItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


# With those two helper functions defined, let's now get to actually creating and submitting our itempool.
def create_all_items(world: AstroneerWorld) -> None:
    # This is the function in which we will create all the items that this world submits to the multiworld item pool.
    # There must be exactly as many items as there are locations.
    # In our case, there are either six or seven locations.
    # We must make sure that when there are six locations, there are six items,
    # and when there are seven locations, there are seven items.

    # Creating items should generally be done via the world's create_item method.
    # First, we create a list containing all the items that always exist.

    itempool: list[Item] = [
        world.create_item("Floodlight"),
        world.create_item("Small Shuttle"),
        world.create_item("Solid-Fuel Thruster"),
        world.create_item("Smelting Furnace"),
        world.create_item("Small Solar"),
    ]

    # Some items may only exist if the player enables certain options.
    # In our case, If the hammer option is enabled, the sixth item is the Hammer.
    # Otherwise, we add a filler Confetti Cannon.
    #if world.options.hammer:
        # Once again, it is important to stress that even though the Hammer doesn't always exist,
        # it must be present in the worlds item_name_to_id.
        # Whether it is actually in the itempool is determined purely by whether we create and add the item here.
        #itempool.append(world.create_item("Hammer"))

    # Archipelago requires that each world submits as many locations as it submits items.
    # This is where we can use our filler and trap items.
    # APQuest has two of these: The Confetti Cannon and the Math Trap.
    # (Unfortunately, Archipelago is a bit ambiguous about its terminology here:
    #  "filler" is an ItemClassification separate from "trap", but in a lot of its functions,
    #  Archipelago will use "filler" to just mean "an additional item created to fill out the itempool".
    #  "Filler" in this sense can technically have any ItemClassification,
    #  but most commonly ItemClassification.filler or ItemClassification.trap.
    #  Starting here, the word "filler" will be used to collectively refer to APQuest's Confetti Cannon and Math Trap,
    #  which are ItemClassification.filler and ItemClassification.trap respectively.)
    # Creating filler items works the same as any other item. But there is a question:
    # How many filler items do we actually need to create?
    # In regions.py, we created either six or seven locations depending on the "extra_starting_chest" option.
    # In this function, we have created five or six items depending on whether the "hammer" option is enabled.
    # We *could* have a really complicated if-else tree checking the options again, but there is a better way.
    # We can compare the size of our itempool so far to the number of locations in our world.

    # The length of our itempool is easy to determine, since we have it as a list.
    number_of_items = len(itempool)

    # The number of locations is also easy to determine, but we have to be careful.
    # Just calling len(world.get_locations()) would report an incorrect number, because of our *event locations*.
    # What we actually want is the number of *unfilled* locations. Luckily, there is a helper method for this:
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    # Now, we just subtract the number of items from the number of locations to get the number of empty item slots.
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    # Finally, we create that many filler items and add them to the itempool.
    # To create our filler, we could just use world.create_item("Confetti Cannon").
    # But there is an alternative that works even better for most worlds, including APQuest.
    # As discussed above, our world must have a get_filler_item_name() function defined,
    # which must return the name of an infinitely repeatable filler item.
    # Defining this function enables the use of a helper function called world.create_filler().
    # You can just use this function directly to create as many filler items as you need to complete your itempool.
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    # But... is that the right option for your game? Let's explore that.
    # For some games, the concepts of "regular itempool filler" and "additionally created filler" are different.
    # These games might want / require specific amounts of specific filler items in their regular pool.
    # To achieve this, they will have to intentionally create the correct quantities using world.create_item().
    # They may still use world.create_filler() to fill up the rest of their itempool with "repeatable filler",
    # after creating their "specific quantity" filler and still having room left over.

    # But there are many other games which *only* have infinitely repeatable filler items.
    # They don't care about specific amounts of specific filler items, instead only caring about the proportions.
    # In this case, world.create_filler() can just be used for the entire filler itempool.
    # APQuest is one of these games:
    # Regardless of whether it's filler for the regular itempool or additional filler for item links / etc.,
    # we always just want a Confetti Cannon or a Math Trap depending on the "trap_chance" option.
    # We defined this behavior in our get_random_filler_item_name() function, which in world.py,
    # we'll bind to world.get_filler_item_name(). So, we can just use world.create_filler() for all of our filler.

    # Anyway. With our world's itempool finalized, we now need to submit it to the multiworld itempool.
    # This is how the generator actually knows about the existence of our items.
    world.multiworld.itempool += itempool

    # Sometimes, you might want the player to start with certain items already in their inventory.
    # These items are called "precollected items".
    # They will be sent as soon as they connect for the first time (depending on your client's item handling flag).
    # Players can add precollected items themselves via the generic "start_inventory" option.
    # If you want to add your own precollected items, you can do so via world.push_precollected().

    # A list containing all the default unlocked research catalog items.
    starting_research_catalog_items = ["Small Shuttle"]
    # Add all the starting catalog items
    # for every item
    for starting_item in starting_research_catalog_items:
        # make it an item and add it to your starting items
        item = world.create_item(starting_item)
        world.push_precollected(item)
