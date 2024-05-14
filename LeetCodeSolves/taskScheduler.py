from collections import Counter


def leastInterval(tasks, n):
    tasks_count = Counter(tasks)

    max_freq = max(tasks_count.values())

    max_freq_task_count = sum(1 for count in tasks_count.values() if count == max_freq)

    return max(len(tasks), (max_freq - 1) * (n + 1) + max_freq_task_count)


if __name__ == '__main__':
    tasks = ["A", "C", "A", "B", "D", "B", "C"]
    n = 22
    print(leastInterval(tasks, n))
