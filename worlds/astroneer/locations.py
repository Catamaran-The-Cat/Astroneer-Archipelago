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
    # MissionTrailhead01-Base
    "Planetfall": 111 + ASTRONEER_ID, # Trailhead01_1.1
    "Astroneering Bas(e)ics": 112 + ASTRONEER_ID, # Trailhead01_1.1.1
    "Breathing Space": 113 + ASTRONEER_ID, # Trailhead01_1.1.1a
    "Resourcing": 114 + ASTRONEER_ID, # Trailhead01_1.1.1b
    "Landfilling": 115 + ASTRONEER_ID, # Trailhead01_1.1.1c
    "Re-Tooling": 116 + ASTRONEER_ID, # Trailhead01_1.1.1d
    "Printing Up": 117 + ASTRONEER_ID, # Trailhead01_1.1.1.1
    # PowerMissionPathData
    "Powerful Problems": 118 + ASTRONEER_ID, # Trailhead01_1.1.1.1.1
    "Battery Backup": 119 + ASTRONEER_ID, # Trailhead01_1.1.1.1.1.1
    "Eyes On Lithium": 1110 + ASTRONEER_ID, # Trailhead01_1.1.1.1.1.1.1
    "Medium Battery": 1111 + ASTRONEER_ID, # Trailhead01_1.1.1.1.1.1.1.1
    "High Tech Spec": 1112 + ASTRONEER_ID, # Trailhead01_1.1.1.1.1.1.1.1.1 (that's a lot of 1s)
    # CraftingAndExplorationMissionPathData
    "Smeltering Hot": 1113 + ASTRONEER_ID, # Trailhead01_1.1.1.1.2
    "To Parts Unknown": 1114 + ASTRONEER_ID, # Trailhead01_1.1.1.1.2.1
    "Forward Progress": 1115 + ASTRONEER_ID, # Trailhead01_1.1.1.1.2.1.1
    "Safe as Houses": 1116 + ASTRONEER_ID, # Trailhead01_1.1.1.1.2.1.1.1
    "Talking Tungsten": 1117 + ASTRONEER_ID, # Trailhead01_1.1.1.1.2.2
    "Materials Matters": 1118 + ASTRONEER_ID, # Trailhead01_1.1.1.1.2.2.1
    "From Thin Air": 1119 + ASTRONEER_ID, # Trailhead01_1.1.1.1.2.2.1.1
    "Fuel for Thought": 1120 + ASTRONEER_ID, # Trailhead01_1.1.1.1.2.2.1.1.1
    "Composite Perfection": 1121 + ASTRONEER_ID, # Trailhead01_1.1.1.1.2.2.1.1.2
    "Movin' & Haulin'": 1122 + ASTRONEER_ID, # Trailhead01_1.1.1.1.2.3
    "Relocation Package": 1123 + ASTRONEER_ID, # Trailhead01_1.1.1.1.2.3.1
    "Shred, Scrap, Trade": 1124 + ASTRONEER_ID, # Trailhead01_1.1.1.1.2.3.1.1
    # ResearchMissionPathData
    "For Science!": 1125 + ASTRONEER_ID, # Trailhead01_1.1.1.1.3
    "Take a Byte": 1126 + ASTRONEER_ID, # Trailhead01_1.1.1.1.3.1
    "Advanced Explorer Kit": 1127 + ASTRONEER_ID, # Trailhead01_1.1.1.1.3.1.1
    "Unlocked Potential": 1128 + ASTRONEER_ID, # Trailhead01_1.1.1.1.3.1.1.1
    "Here We Go A Sampling": 1129 + ASTRONEER_ID, # Trailhead01_1.1.1.1.3.2
    "Master of Unboxing": 1130 + ASTRONEER_ID, # Trailhead01_1.1.1.1.3.2.1
    "Cracking Caches": 1131 + ASTRONEER_ID, # Trailhead01_1.1.1.1.3.3
    # AutomationMissionPathData
    "Arm Yourself!": 1132 + ASTRONEER_ID, # Trailhead01_1.1.1.1.4
    "Stuffed Storage": 1133 + ASTRONEER_ID, # Trailhead01_1.1.1.1.4.1
    "Unearthed": 1134 + ASTRONEER_ID, # Trailhead01_1.1.1.1.4.1.1
    # MissionTrailhead02-Gateways
    "Lights in the Distance": 1135 + ASTRONEER_ID, # Mission_2-1
    "Well, That's Weird": 1136 + ASTRONEER_ID, # Mission_2-2
    "A Core Concept": 1137 + ASTRONEER_ID, # Mission_2-3
    "There's Something Out There": 1138 + ASTRONEER_ID, # Mission_2-4
    "Multi-Core Processing": 1139 + ASTRONEER_ID, # Mission_2-5
    "Through the Looking Glass": 1140 + ASTRONEER_ID, # Mission_2-6
    # MissionTrailhead03-Wanderer
    "Echoes of the Past": 1141 + ASTRONEER_ID, # Mission_3-1
    "Chasing Signals": 1142 + ASTRONEER_ID, # Mission_3-2
    "Things to Remember": 1143 + ASTRONEER_ID, # Mission_3-3
    "When and Where?": 1144 + ASTRONEER_ID, # Mission_3-4
    # MissionTrailhead04-Vehicle
    "Prototype Recovery": 1145 + ASTRONEER_ID, # Vehicle1
    "Tracing the Transmission": 1146 + ASTRONEER_ID, # Vehicle2
    "Ingredient Investigations": 1147 + ASTRONEER_ID, # Vehicle3-1
    "Electrical Engineering": 1148 + ASTRONEER_ID, # Vehicle3-2
    "Onboarding": 1149 + ASTRONEER_ID, # Vehicle4
    "Vertical Thinking": 1150 + ASTRONEER_ID, # Vehicle5
    "Bootstrapping": 1151 + ASTRONEER_ID, # Vehicle6
    "Substance Selection": 1152 + ASTRONEER_ID, # Vehicle7-1
    "What The Thrust?": 1153 + ASTRONEER_ID, # Vehicle7-2
    "Further Refinement": 1154 + ASTRONEER_ID, # Vehicle8
    "Analysis Paralysis": 1155 + ASTRONEER_ID, # Vehicle9
    "Finished Product": 1156 + ASTRONEER_ID, # Vehicle10
    "Globe Trotting": 1157 + ASTRONEER_ID, # VehicleGlobe1
    # MissionTrailhead05-Snails
    "Bait & Switch": 1158 + ASTRONEER_ID, # Snails000
    "Strange Object": 1159 + ASTRONEER_ID, # Snails001
    "Jumper Cables": 1160 + ASTRONEER_ID, # Snails002
    "A Breath of Fresh Air": 1161 + ASTRONEER_ID, # Snails003
    "Know Thy Galastropod": 1162 + ASTRONEER_ID, # Snails004
    "Tracking Power": 1163 + ASTRONEER_ID, # Snails010
    "Galastropod Care": 1164 + ASTRONEER_ID, # Snails011
    "Signal Boost": 1165 + ASTRONEER_ID, # Snails020
    "Wholesome Produce": 1166 + ASTRONEER_ID, # Snails021
    "Overcharged": 1167 + ASTRONEER_ID, # Snails030
    "All Together Now": 1168 + ASTRONEER_ID, # Snails040
    "Final Entry": 1169 + ASTRONEER_ID, # Snails041
    # MissionSnails-Sylva
    "G. sylva: Shells": 1170 + ASTRONEER_ID, # Snails100
    "G. sylva: Terrarium": 1171 + ASTRONEER_ID, # Snails101
    "G. sylva: Recovery": 1172 + ASTRONEER_ID, # Snails102
    "G. sylva: Verification": 1173 + ASTRONEER_ID, # Snails103
    # MissionSnails-Desolo
    "G. desolo: Shells": 1174 + ASTRONEER_ID, # Snails200
    "G. desolo: Terrarium": 1175 + ASTRONEER_ID, # Snails201
    "G. desolo: Recovery": 1176 + ASTRONEER_ID, # Snails202
    "G. desolo: Verification": 1177 + ASTRONEER_ID, # Snails203
    # MissionSnails-Calidor
    "G. calidor: Shells": 1178 + ASTRONEER_ID, # Snails300
    "G. calidor: Terrarium": 1179 + ASTRONEER_ID, # Snails301
    "G. calidor: Recovery": 1180 + ASTRONEER_ID, # Snails302
    "G. calidor: Verification": 1181 + ASTRONEER_ID, # Snails303
    # MissionSnails-Vesania
    "G. vesania: Shells": 1182 + ASTRONEER_ID, # Snails400
    "G. vesania: Terrarium": 1183 + ASTRONEER_ID, # Snails401
    "G. vesania: Recovery": 1184 + ASTRONEER_ID, # Snails402
    "G. vesania: Verification": 1185 + ASTRONEER_ID, # Snails403
    # MissionSnails-Novus
    "G. novus: Shells": 1186 + ASTRONEER_ID, # Snails500
    "G. novus: Terrarium": 1187 + ASTRONEER_ID, # Snails501
    "G. novus: Recovery": 1188 + ASTRONEER_ID, # Snails502
    "G. novus: Verification": 1189 + ASTRONEER_ID, # Snails503
    # MissionSnails-Glacio
    "G. glacio: Shells": 1190 + ASTRONEER_ID, # Snails600
    "G. glacio: Terrarium": 1191 + ASTRONEER_ID, # Snails601
    "G. glacio: Recovery": 1192 + ASTRONEER_ID, # Snails602
    "G. glacio: Verification": 1193 + ASTRONEER_ID, # Snails603
    # MissionSnails-Atrox
    "G. atrox: Shells": 1194 + ASTRONEER_ID, # Snails700
    "G. atrox: Terrarium": 1195 + ASTRONEER_ID, # Snails701
    "G. atrox: Recovery": 1196 + ASTRONEER_ID, # Snails702
    "G. atrox: Verification": 1197 + ASTRONEER_ID, # Snails703
    # MissionTrailhead06-Railways
    "Digging Deeper": 1198 + ASTRONEER_ID, # Rails000
    # MissionRails-DepotA
    "Snow Piercer": 1199 + ASTRONEER_ID, # Rails001
    "Windup": 11100 + ASTRONEER_ID, # Rails002a
    "Logistical Chip": 11101 + ASTRONEER_ID, # Rails002b
    "Back On Track": 11102 + ASTRONEER_ID, # Rails003
    "Engine-uity": 11103 + ASTRONEER_ID, # Rails004a
    "All Aboard": 11104 + ASTRONEER_ID, # Rails004b
    "Reinstation": 11105 + ASTRONEER_ID, # Rails005
    "Site-ings": 11106 + ASTRONEER_ID, # Rails006
    "Better Freight Than Never": 11107 + ASTRONEER_ID, # Rails007a
    "Cooler Runnings": 11108 + ASTRONEER_ID, # Rails007b
    "Rubberstamp": 11109 + ASTRONEER_ID, # Rails008
    # MissionRails-DepotB
    "Curiouser And Curiouser": 11110 + ASTRONEER_ID, # Rails009
    "Sunrise": 11111 + ASTRONEER_ID, # Rails010a
    "Chipping In": 11112 + ASTRONEER_ID, # Rails010b
    "Manifestation": 11113 + ASTRONEER_ID, # Rails011
    "Pile On": 11114 + ASTRONEER_ID, # Rails012
    "Just The Facts": 11115 + ASTRONEER_ID, # Rails013a
    "They Belong In a Museum": 11116 + ASTRONEER_ID, # Rails013b
    "Logbook": 11117 + ASTRONEER_ID, # Rails014
    # MissionRails-DepotC
    "Travelling Companion": 11118 + ASTRONEER_ID, # Rails015
    "Discovery Train": 11119 + ASTRONEER_ID, # Rails016
    "Central Processing": 11120 + ASTRONEER_ID, # Rails017
    "Day & Night": 11121 + ASTRONEER_ID, # Rails018a
    "Dip Some Chips": 11122 + ASTRONEER_ID, # Rails018b
    "Un-arailable": 11123 + ASTRONEER_ID, # Rails019
    "Mystery Shrooms": 11124 + ASTRONEER_ID, # Rails020a
    "Singular Substance": 11125 + ASTRONEER_ID, # Rails020b
    "Training Complete": 11126 + ASTRONEER_ID, # Rails021
    # MissionTrailhead07-Chronos
    "HELP": 11127 + ASTRONEER_ID, # Chronos001
    "A Fault in the Stars": 11128 + ASTRONEER_ID, # Chronos002
    "Hi, I'm EVA": 11129 + ASTRONEER_ID, # Chronos002a
    "We Need to Talk": 11130 + ASTRONEER_ID, # Chronos002b
    "I Know You Like Missions": 11131 + ASTRONEER_ID, # Chronos002c
    "Controlled Fire(wall)": 11132 + ASTRONEER_ID, # Chronos002d
    "Behind the Curtain": 11133 + ASTRONEER_ID, # Chronos003
    "Time Out": 11134 + ASTRONEER_ID, # Chronos004
    "Files Missing": 11135 + ASTRONEER_ID, # Chronos005
    "Need Input": 11136 + ASTRONEER_ID, # Chronos005a
    "Memory Disassembly": 11137 + ASTRONEER_ID, # Chronos005b
    "Novus Roses": 11138 + ASTRONEER_ID, # Chronos006
    "Memory Fault: Peril": 11139 + ASTRONEER_ID, # Chronos007a
    "Memory Fragment: Peril": 11140 + ASTRONEER_ID, # Chronos007b
    "Memory Integration: Peril": 11141 + ASTRONEER_ID, # Chronos007c
    "What Was Lost": 11142 + ASTRONEER_ID, # Chronos007d
    "The Crash": 11143 + ASTRONEER_ID, # Chronos007e
    "You Are a Very Good Helper": 11144 + ASTRONEER_ID, # Chronos007f
    "There is More Bad News": 11145 + ASTRONEER_ID, # Chronos007g
    "Memory Fault: Discovery": 11146 + ASTRONEER_ID, # Chronos008a
    "Memory Fragment: Discovery": 11147 + ASTRONEER_ID, # Chronos008b
    "Memory Integration: Discovery": 11148 + ASTRONEER_ID, # Chronos008c
    "What Was Found": 11149 + ASTRONEER_ID, # Chronos008d
    "The Mind Bank and You": 11150 + ASTRONEER_ID, # Chronos008e
    "Echoes of Astroneers Past": 11151 + ASTRONEER_ID, # Chronos008f
    "Anyway, Our Mission": 11152 + ASTRONEER_ID, # Chronos008g
    "Memory Fault: Hope": 11153 + ASTRONEER_ID, # Chronos009a
    "Memory Fragment: Hope": 11154 + ASTRONEER_ID, # Chronos009b
    "Memory Integration: Hope": 11155 + ASTRONEER_ID, # Chronos009c
    "What Was Left Behind": 11156 + ASTRONEER_ID, # Chronos009d
    "Chronos Loves Reading": 11157 + ASTRONEER_ID, # Chronos009e
    "I Am a Fox": 11158 + ASTRONEER_ID, # Chronos009f
    "Almost There": 11159 + ASTRONEER_ID, # Chronos009g
    "Final Approval": 11160 + ASTRONEER_ID, # Chronos010
    "[ERROR]": 11161 + ASTRONEER_ID, # Chronos011
    "S-O-S": 11162 + ASTRONEER_ID, #Chronos012
    "So Long...": 11163 + ASTRONEER_ID, # Chronos013
    "...For Now": 11164 + ASTRONEER_ID, # Chronos014

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
