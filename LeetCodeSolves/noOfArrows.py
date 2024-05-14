def numberOfArrows(points):
    if not points:
        return 0

    points.sort(key=lambda x: x[1])
    arrow = 0
    ends = points[0][1]

    for balloon in points[1:]:
        if balloon[0] > ends:
            arrow += 1
            ends = balloon[1]
        else:
            ends = min(ends, balloon[1])

    arrow += 1

    return arrow


if __name__ == '__main__':
    points1 = [[10, 16], [2, 8], [1, 6], [7, 12]]
    print(numberOfArrows(points1))


