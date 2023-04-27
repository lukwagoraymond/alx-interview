#!/usr/bin/python3
"""Defines a function that determines if a box containing a list
of list can be opended using keys stored in the lists
"""


def canUnlockAll(boxes):
    """Determines if boxes can be opened with
    keys in the list"""
    position = 0
    unlocked = {}

    for box in boxes:
        if len(box) == 0 or position == 0:
            unlocked[position] = "Locked indefinity"
        for key in box:
            if key < len(boxes) and key != position:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
        position += 1
    return False
