from functools import cmp_to_key


def load_data(data):
    rules_before, rules_after = {}, {}
    updates_list = []
    for row in data.split():
        # print(f"Row = [{row}]")
        if "|" in row:
            a, b = list(map(int, row.split("|")))
            # update must be before these updates
            if a in rules_before:
                rules_before[a] = rules_before[a] | {b}
            else:
                rules_before[a] = {b}
            # update must be after these updates
            if b in rules_after:
                rules_after[b] = rules_after[b] | {a}
            else:
                rules_after[b] = {a}
        else:
            updates_list.append(list(map(int, row.split(","))))
    return rules_before, rules_after, updates_list


def is_update_valid(pages, rules_before, rules_after) -> bool:
    for i, current_page in enumerate(pages):
        # rules before check
        if current_page in rules_before:
            # check that pages before current are not in the rules_BEFORE
            for page in pages[:i]:
                if page in rules_before[current_page]:
                    return False
        # # rules after check
        # if current_page in rules_after:
        #     # check that pages after current are not in the rules_AFTER
        #     for page in pages[i:]:
        #         if page in rules_after[current_page]:
        #             return False
    return True


def compute_updates(rules_before, rules_after, updates_list):
    r = 0
    for pages in updates_list:
        if is_update_valid(pages, rules_before, rules_after):
            r += pages[len(pages) // 2]
    return r


def correct_pages_order(pages, rules_before, rules_after):
    return sorted(
        pages,
        key=cmp_to_key(
            lambda page1, page2: 0
            if page1 not in rules_before or page2 not in rules_before[page1]
            else -1
        ),
    )


def compute_corrected_updates(rules_before, rule_after, updates_list):
    r = 0
    for pages in updates_list:
        if not is_update_valid(pages, rules_before, rule_after):
            corrected_pages = correct_pages_order(pages, rules_before, rule_after)
            r += corrected_pages[len(corrected_pages) // 2]
    return r


if __name__ == "__main__":
    print("adv05")
    data = open("aoc_2024/adv05.txt", "r").read()
    print("Loading rules and updates")
    rules_before, rules_after, updates_list = load_data(data)
    print(f"compute 1: {compute_updates(rules_before, rules_after, updates_list)}")
    print(
        f"compute 2: {compute_corrected_updates(rules_before, rules_after, updates_list)}"
    )
