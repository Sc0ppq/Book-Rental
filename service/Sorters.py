def mergeSort(list, key=None, reverse=False):
    if len(list) <= 1:
        return list

    mid = len(list) // 2
    leftHalf = list[:mid]
    rightHalf = list[mid:]

    sortedLeft = mergeSort(leftHalf, key, reverse)
    sortedRight = mergeSort(rightHalf, key, reverse)

    return merge(sortedLeft, sortedRight, key, reverse)

def merge(left, right, key=None, reverse=False):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        left_key = key(left[i]) if key else left[i]
        right_key = key(right[j]) if key else right[j]

        if (left_key < right_key and not reverse) or (left_key > right_key and reverse):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def bingoSort(list, key=None, reverse=False):
    # gasim cel mai mic elem din lista folosind cheia
    bingo = min(list, key=key) if key else min(list)

    # gasim cel mai mare elem din lista folosind cheia
    largest = max(list, key=key) if key else max(list)
    nextBingo = largest
    nextPos = 0

    while bingo != nextBingo:
        startPos = nextPos
        for i in range(startPos, len(list)):
            current = key(list[i]) if key else list[i]
            bingo_val = key(bingo) if key else bingo

            if current == bingo_val:
                list[i], list[nextPos] = list[nextPos], list[i]
                nextPos += 1
            elif current < key(nextBingo) if key else nextBingo:
                nextBingo = list[i]

        bingo = nextBingo
        nextBingo = largest

    if reverse:
        list.reverse()

    return list