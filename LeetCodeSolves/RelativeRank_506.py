def relativeRank(score):
    sorted_score = sorted(enumerate(score), key= lambda x: x[1], reverse=True)
    answer = [None] * len(score)

    for rank, (index, _) in enumerate(sorted_score, start=1):
        if rank == 1:
            answer[index] = "Gold Medal"
        elif rank == 2:
            answer[index] = "Silver Medal"
        elif rank == 3:
            answer[index] = "Bronze Medal"
        else:
            answer[index] = str(rank)

    return answer


if __name__ == '__main__':
    score = [5, 4, 3, 2, 1]
    print(relativeRank(score))