from math import inf

absent_edge_number = -32768


def make_income_lists(weights, n):
    lists = [[] for _ in range(n)]
    for j in range(n):
        for i in range(n):
            if weights[i][j] != absent_edge_number:
                lists[j].append(i)
    return lists


def topological_sort(weights, n):
    top_sorted, added = [], set()
    for k in range(n):
        for j in range(n):
            if j in added:
                continue
            shall_continue = False
            for i in range(n):
                if weights[i][j] != absent_edge_number and i not in added:
                    shall_continue = True
                    break
            if shall_continue:
                continue
            top_sorted.append(j)
            added.add(j)
    return top_sorted


def modified104_algo(v1, top_sorted, lists, weights, n):
    distances = [-inf for _ in range(n)]
    distances[v1] = 0

    previous = [None for _ in range(n)]

    for k in range(1, n):
        vk = top_sorted[k]
        for w in lists[vk]:
            new_distance = distances[w] + weights[w][vk]
            if new_distance > distances[vk]:
                distances[vk] = new_distance
                previous[vk] = w
    return distances, previous


def reconstruct_path(previous, end):
    path = []
    while end is not None:
        path.append(end)
        end = previous[end]
    return ' '.join(map(str, reversed(path)))


with open('in.txt') as f:
    n = int(f.readline())
    weights = [list(map(int, f.readline().split())) for _ in range(n)]
    v, w = [int(f.readline()) - 1 for _ in range(2)]

lists = make_income_lists(weights, n)
top_sorted = topological_sort(weights, n)
distances, previous = modified104_algo(v, top_sorted, lists, weights, n)

with open('out.txt', 'w') as f:
    if distances[w] != -inf:
        f.write('Y\n')
        f.write(reconstruct_path(previous, w) + '\n')
        f.write(str(distances[w]))
    else:
        f.write('N')

print(distances, previous)
