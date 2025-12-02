"""Solution for Advent of Code 2025 Day 02."""


def part1(input_data: list[str]) -> int:
    # Convert input to a list of (start, end) as int.
    ranges = input_data[0].strip().split(",")
    ranges = [list(map(int, rang.split("-"))) for rang in ranges]

    # Iterate through the ranges.
    counter = 0
    for rang in ranges:
        start, end = rang
        for num in range(start, end + 1):
            len_str = len(str(num))
            half_len_str = len(str(num)) // 2
            if len_str % 2 != 0:
                continue
            else:
                if str(num)[:half_len_str] == str(num)[half_len_str:]:
                    counter += num

    return counter


def part2(input_data: list[str]) -> int:
    def chunkify(s, n):
        chunks = []
        for start in range(0, len(s), n):
            chunks.append(s[start : start + n])
        return chunks

    def is_invalid(num, max_window_size):
        for window_size in range(1, max_window_size + 1):
            chunks = chunkify(str(num), window_size)
            rets = []
            for chunk in chunks:
                rets.append(chunks.count(chunk))
            is_invalid_p1 = all([ret > 1 for ret in rets])
            if is_invalid_p1:
                for ws in range(1, max_window_size + 1):
                    new_chunks = chunkify(str(num), ws)
                    is_invalid_p2 = len(set(new_chunks)) == 1
                    if is_invalid_p2:
                        return True
        return False

    # Convert input to a list of (start, end) as int.
    ranges = input_data[0].strip().split(",")
    ranges = [list(map(int, rang.split("-"))) for rang in ranges]

    # Iterate through the ranges.
    counter = 0
    for rang in ranges:
        start, end = rang
        max_window_size = len(str(end)) // 2
        for num in range(start, end + 1):
            if is_invalid(num, max_window_size):
                counter += num
    return counter
