distance_vertex = []
visited_vertex = []
p = []
max_len = 10000
matrix = \
    [
        [0, 12, 10, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 3, 1, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 8, 0],
        [0, 0, 0, 7, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 11],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]


def qwerty():
    start_vertex = int(input("Введите вершину: "))
    dijkstra(start_vertex - 1)


def dijkstra(start_vertex):
    v = start_vertex + 1

    for i in range(len(matrix)):
        distance_vertex.append(max_len)
        visited_vertex.append(False)
        p.append(v)

    distance_vertex[start_vertex] = 0

    for count in range(len(matrix)):
        index = 0
        min = max_len

        for i in range(len(matrix)):
            if visited_vertex[i] != True and distance_vertex[i] <= min:
                min = distance_vertex[i]
                index = i

        j = index
        visited_vertex[j] = True

        for i in range(len(matrix)):
            if visited_vertex[i] != True and matrix[j][i] and \
                distance_vertex[j] != max_len and \
                distance_vertex[j] + matrix[j][i] < distance_vertex[i]:
                distance_vertex[i] = distance_vertex[j] + matrix[j][i]
                p[i] = j + 1

    for i in range(len(matrix)):
        print(v, " -> ", i + 1, " = ", end="")
        if distance_vertex[i] != max_len:
            print(distance_vertex[i])
        else:
            print("нет пути домой")

    vk = int(input("Введите конечную вершину: "))
    k = vk - 1  # Текущая вершина
    row = str(vk) + " >- " + str(p[k])
    while p[k] != vk and p[k] != v:
        k = p[k] - 1
        row += " >- " + str(p[k])

    if distance_vertex[vk - 1] != max_len:
        print(row[::-1], " = ", distance_vertex[vk - 1])
    else:
        print(v, "не имеет пути до", vk)




qwerty()