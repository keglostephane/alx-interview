#!/usr/bin/python3
"""lockboxes module
"""


def canUnlockAll(boxes):
    """Determine if all boxes can be opened"""
    visited = set()
    keys = {0}

    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    while keys:
        current_box = keys.pop()
        visited.add(current_box)

        for key in boxes[current_box]:
            if key not in visited:
                keys.add(key)
            visited.add(key)
    
    return len(visited) == len(boxes)