nums = lambda line: map(int, line.split("  ")); input = map(nums, open("input.txt","r").read().splitlines()); lists = {0: [], 1: []}; process_line = lambda line: [lists[i].append(elem) for i, elem in enumerate(line)]; _ = [*map(process_line, input)]; similarity = sum(element * lists[1].count(element) for element in lists[0]); print(similarity)
