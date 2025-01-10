def map_disk(disk_map):
    disk = list()
    for i, char in enumerate(disk_map):
        if i % 2 == 0:
            disk.extend([i // 2] * int(char))
        else:
            disk.extend([None] * int(char))
    return disk, i // 2


def blocks_defrag(disk):
    # disk is updated in place
    i = 0
    j = len(disk) - 1
    while i < j:
        # swap them
        if disk[i] is None and disk[j] is not None:
            disk[i] = disk[j]
            disk[j] = None
            i += 1
            j -= 1
        else:
            # find first block that is None
            if disk[i] is not None:
                i += 1
            # find last block that is not None
            if disk[j] is None:
                j -= 1


def part1(disk_map):
    disk, _ = map_disk(disk_map)  # convert text file to list of blocks
    blocks_defrag(disk)  # defragment the disk
    return sum([i * file_id for i, file_id in enumerate(disk) if file_id])


def find_sequence(disk, value, start_index=0):
    """
    Find the index and length of the sequence of 'value' starting from 'start_index' in the list 'disk'.

    Parameters:
    - disk (list): The list of elements to search through.
    - value: The element to search for as part of a sequence.
    - start_index (int, optional): The index at which to start searching for the sequence. Defaults to 0.

    Returns:
    - tuple: A tuple containing the starting index and length of the sequence found. If no sequence is found, returns (-1, 0).
    """
    try:
        # Find the first occurrence of 'value' starting from 'start_index'
        i = disk.index(value, start_index)

        # Initialize the length of the sequence
        length = 1

        # Expand the sequence to find the full length if possible
        while i + length < len(disk) and disk[i + length] == value:
            length += 1

        return i, length

    except ValueError:
        # Return -1 and 0 if 'value' is not found in the list starting from 'start_index'
        return -1, 0


def find_space(disk, min_size, start_index=0):
    """
    Find the first contiguous block of space on the disk that has at least the specified minimum size.

    Parameters:
    - disk: A list representing the disk blocks. Each element is either None (space) or a value indicating data.
    - min_size: The minimum size of the space to find.
    - start_index: The starting index from which to search for the space block.

    Returns:
    - The index of the first contiguous block with at least the specified minimum size, or -1 if no such block is found.
    """
    # Ensure min_size is positive
    if min_size <= 0:
        return -1

    # Initialize variables to track the start and length of the contiguous space
    start_index = 0
    index, length = find_sequence(disk, None, start_index)

    # Loop to find the first block with a minimum size
    while index != -1 and length < min_size:
        start_index = index + length  # Move to the next potential starting point
        index, length = find_sequence(disk, None, start_index)

    # Check if a valid space block was found
    if index == -1 or length < min_size:
        return -1

    # Return the index of the first contiguous block with at least the minimum size
    return index


def files_defrag(disk, last_file_id):
    # search file_id block in disk starting from the end
    for file_id in range(last_file_id, 0, -1):
        index, length = find_sequence(disk, file_id)
        index_space = find_space(disk, length)
        if index_space != -1 and index_space < index:
            disk[index_space : index_space + length] = [file_id] * length
            disk[index : index + length] = [None] * length

    return disk


def part2(disk_map):
    disk, last_file_id = map_disk(disk_map)  # convert text file to list of blocks
    files_defrag(disk, last_file_id)  # defragment the disk
    return sum([i * file_id for i, file_id in enumerate(disk) if file_id])


if __name__ == "__main__":
    # read text file aoc_2024/adv09.txt into disk_map
    with open("aoc_2024/adv09.txt", "rt") as f:
        disk_map = f.readline().strip()

    print(f"Part 1: {part1(disk_map)}")
    print(f"Part 2: {part2(disk_map)}")
