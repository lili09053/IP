sets = []
matrix = [
            [0, 7, 8, 0, 0, 0],
            [7, 0, 11, 2, 0, 0],
            [8, 11, 0, 6, 9, 0],
            [0, 2, 6, 0, 11, 9],
            [0, 0, 9, 11, 0, 10],
            [0, 0, 0, 9, 10, 0]
         ]
point_tree = []
ost_tree = []


def check_points(v1, v2):
    temp = -1
    for i in range(len(point_tree)):
        if v1 in point_tree[i] and v2 in point_tree[i]:
            temp = -2
            break
        elif v1 not in point_tree[i] and v2 not in point_tree[i]:
            temp = -1
        else:
            temp = i
            break
    return temp


def try_union(v1, v2):
    for i in range(len(point_tree) - 1):
        for j in range(i, len(point_tree)):
            if v1 in point_tree[i] and v1 in point_tree[j] or v2 in point_tree[i] and v2 in point_tree[j]:
                for elem in point_tree[j]:
                    if elem not in point_tree[i]:
                        point_tree[i].append(elem)
                point_tree.pop(j)
                break;


def kraskal():
    spanning_tree = []
    ost_tree.clear()
    point_tree.clear()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            elem = [matrix[i][j], i + 1, j + 1]  # (длина ребра, 1-я вершина, 2-я вершина)
            reverse_elem = [matrix[i][j], j + 1, i + 1]
            if tuple(elem) not in spanning_tree \
                    and tuple(reverse_elem) not in spanning_tree \
                    and matrix[i][j] != 0 and i != j:
                spanning_tree.append(tuple(elem))

    spanning_tree.sort()
    for elem in spanning_tree:
        print(elem)
    print()

    for tpl in spanning_tree:
        temp = check_points(tpl[1], tpl[2])
        if temp != -2:  # если обе вершины ОДНОВРЕМЕННО в каком-либо множестве вершин
            if temp != -1:  # если одна из вершин есть в i-ом множестве вершин
                if tpl[1] not in point_tree[temp]:
                    point_tree[temp].append(tpl[1])
                if tpl[2] not in point_tree[temp]:
                    point_tree[temp].append(tpl[2])
                ost_tree.append(tpl)
                try_union(tpl[1], tpl[2])  # попытка объединить множества вершин
            else:  # если обе вершины НЕТ ни в каком-либо множестве вершин
                point_tree.append([])
                point_tree[len(point_tree) - 1].append(tpl[1])
                point_tree[len(point_tree) - 1].append(tpl[2])
                ost_tree.append(tpl)
        if len(point_tree[0]) == len(matrix):
            break

    for elem in ost_tree:
        print(elem)


kraskal()
