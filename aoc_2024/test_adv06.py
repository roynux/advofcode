import pytest
from aoc_2024.adv06 import Room, detect_loop_in_room, part2


@pytest.fixture
def fixture_initial_map():
    return """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".splitlines()


def test_load_initial_map(fixture_initial_map):
    room = Room(fixture_initial_map)
    assert room.map == fixture_initial_map
    assert room.height == 10
    assert room.width == 10
    assert room.guard == (6, 4, "^")  # line 6, column 4 and guard looking up
    assert room.obstacles == {
        (0, 4),
        (1, 9),
        (3, 2),
        (4, 7),
        (6, 1),
        (7, 8),
        (8, 0),
        (9, 6),
    }


def test_room_step(fixture_initial_map):
    room = Room(fixture_initial_map)
    room.step()
    room.guard == (5, 4, "^")
    room.step()
    room.guard == (4, 4, "^")
    room.step()
    room.guard == (3, 4, "^")
    room.step()
    room.guard == (2, 4, "^")
    room.step()
    room.guard == (1, 4, ">")  # turn right because of obstacle at 0,4
    room.step()
    room.guard == (1, 5, ">")
    room.guard_positions_history = (
        (5, 4, "^"),
        (4, 4, "^"),
        (3, 4, "^"),
        (2, 4, "^"),
        (1, 4, ">"),
        (1, 5, ">"),
    )


def test_guard_inside_map(fixture_initial_map):
    room = Room(fixture_initial_map)
    room.guard = (0, 0, "^")
    assert room.guard_inside_map is True
    room.step()
    assert room.guard_inside_map is False


def test_walk_until_outside(fixture_initial_map):
    room = Room(fixture_initial_map)

    while room.guard_inside_map and len(room.guard_positions_history) < 100:
        room.step()
    assert len(room.guard_positions_history) == 56
    assert room.guard_distinct_positions == 41
    assert room.guard_inside_map is False


def test_loop_detected(fixture_initial_map):
    room = Room(fixture_initial_map)
    room.obstacles.add((6, 3))
    while (
        room.guard_inside_map
        and (room.loop_detected is False)
        and len(room.guard_positions_history) < 100
    ):
        room.step()

    assert room.loop_detected is True


def test_detected_loop(fixture_initial_map):
    assert detect_loop_in_room(fixture_initial_map, 6, 3) is True
    assert detect_loop_in_room(fixture_initial_map, 7, 6) is True
    assert detect_loop_in_room(fixture_initial_map, 7, 7) is True
    assert detect_loop_in_room(fixture_initial_map, 8, 1) is True
    assert detect_loop_in_room(fixture_initial_map, 8, 3) is True
    assert detect_loop_in_room(fixture_initial_map, 9, 7) is True
    assert detect_loop_in_room(fixture_initial_map, 6, 4) is False
    assert detect_loop_in_room(fixture_initial_map, 0, 0) is False


def test_part2(fixture_initial_map):
    assert part2(fixture_initial_map) == 6
