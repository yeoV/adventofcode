import sys
from collections import defaultdict
read = sys.stdin.read

sections = read().split("\n\n")
rules = [tuple(map(int, line.split("|"))) for line in sections[0].split("\n")]
updates = [list(map(int, line.split(","))) for line in sections[1].split("\n")]

def build_graph(rules):
    rules_graph = defaultdict(list)
    for x, y in rules:
        rules_graph[x].append(y)
    return rules_graph

def check_update(update, graph):
    for idx, x in enumerate(update[:-1]):
        for y in update[idx + 1:]:
            if y not in graph[x]:
                return False
    return True


rules_graph = build_graph(rules)
valid_update = [update for update in updates if check_update(update, rules_graph)]
result = sum([update[len(update)//2] for update in valid_update])
print(result)

