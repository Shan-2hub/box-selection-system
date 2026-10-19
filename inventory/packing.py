"""
Deterministic 3D corner-point packing heuristic.

This is a heuristic, not a complete 3D bin-packing solver: failure means this
heuristic could not find a placement, not that no possible placement exists.
Dimensions use centimetres and weight uses kilograms.
"""
from dataclasses import dataclass
from itertools import permutations


@dataclass(frozen=True)
class Item:
    key: str
    length: float
    width: float
    height: float


@dataclass(frozen=True)
class Placement:
    key: str
    x: float
    y: float
    z: float
    length: float
    width: float
    height: float


def _overlap(a, b):
    # Positive-volume intersection on all three axes means overlap.
    return (
        a.x < b.x + b.length and a.x + a.length > b.x
        and a.y < b.y + b.width and a.y + a.width > b.y
        and a.z < b.z + b.height and a.z + a.height > b.z
    )


def try_pack(items, box_length, box_width, box_height):
    """
    Place items in descending volume order. For each item, test all unique
    axis-aligned rotations at corners generated from existing placements.
    Returns (True, placements) on success, otherwise (False, partial placements).
    """
    if not items:
        return False, []

    ordered = sorted(
        items,
        key=lambda item: (item.length * item.width * item.height,
                          max(item.length, item.width, item.height)),
        reverse=True,
    )
    placed = []

    for item in ordered:
        orientations = sorted(
            set(permutations((item.length, item.width, item.height))),
            key=lambda dims: (-(dims[0] * dims[1] * dims[2]), dims),
        )
        # Corners from the origin and positive faces of already placed items.
        points = {(0.0, 0.0, 0.0)}
        for p in placed:
            points.add((p.x + p.length, p.y, p.z))
            points.add((p.x, p.y + p.width, p.z))
            points.add((p.x, p.y, p.z + p.height))

        candidates = sorted(points, key=lambda point: (point[2], point[1], point[0]))
        chosen = None
        for x, y, z in candidates:
            for length, width, height in orientations:
                if (x + length > box_length or y + width > box_width
                        or z + height > box_height):
                    continue
                candidate = Placement(item.key, x, y, z, length, width, height)
                if not any(_overlap(candidate, old) for old in placed):
                    chosen = candidate
                    break
            if chosen is not None:
                break

        if chosen is None:
            return False, placed
        placed.append(chosen)

    return True, placed
