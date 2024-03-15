#!/usr/bin/python3
"""
A lockbox module
"""


def can_unlock_all(boxes):
    """
    This function determines if all boxes can be opened.
    :param boxes: a list of lists, where each sublist represents a box and
    contains keys to other boxes
    :return: True if all boxes can be opened, else False
    """
    # The set of unlocked boxes, starting with box 0 since it
    # is initially unlocked
    unlocked = {0}
    # A list of keys, starting with the keys from the first box
    keys = boxes[0].copy()

    # As long as there are keys to try, continue trying to unlock boxes
    while keys:
        new_keys = []  # A list to hold newly found keys

        # Iterate over all available keys
        for key in keys:
            # If the key corresponds to a box (and not out of range)
            # and the box hasn't been unlocked yet, unlock it
            if 0 <= key < len(boxes) and key not in unlocked:
                unlocked.add(key)  # Add the box to the set of unlocked boxes
                new_keys.extend(boxes[key])  # Add the keys from the newly box

        # Update the list of keys with the newly found keys
        keys = new_keys

    # Check if we've unlocked all boxes (compare the number of unlocked boxes
    # with the total number of boxes)
    return len(unlocked) == len(boxes)
