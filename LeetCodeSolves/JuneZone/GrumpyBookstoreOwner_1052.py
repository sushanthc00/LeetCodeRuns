def maxSatisfied(customers, grumpy, minutes):
    n = len(customers)
    customer_satisfaction = 0
    current_satisfaction = 0
    max_additional = 0

    for i in range(n):
        if grumpy[i] == 0:
            customer_satisfaction += customers[i]

    for i in range(n):
        current_satisfaction += customers[i] * grumpy[i]
        if i >= minutes:
            current_satisfaction -= customers[i - minutes] * grumpy[i - minutes]
        max_additional = max(max_additional, current_satisfaction)

    return customer_satisfaction + max_additional


if __name__ == '__main__':
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    minutes = 3
    print(maxSatisfied(customers, grumpy, minutes))
