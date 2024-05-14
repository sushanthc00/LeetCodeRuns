def numRescueBoats(people, limit):
    people.sort()
    left, right = 0, len(people) - 1
    boats = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        boats += 1

    return boats


if __name__ == '__main__':
    people = [3,2,2,1]
    limit = 3
    print(numRescueBoats(people, limit))
