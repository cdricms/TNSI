def merge(seq1, seq2):

    result = []

    l1 = len(seq1)
    l2 = len(seq2)

    left = 0
    right = 0

    while left < l1 and right < l2:
        if seq1[left] < seq2[right]:
            result.append(seq1[left])
            left += 1
        else:
            result.append(seq2[right])
            right += 1

    result += seq1[left:]
    result += seq2[right:]

    print(result)
    return result


def mergesort(seq):
    length = len(seq)

    print(seq)

    if length == 1:
        return seq

    middle = length // 2

    left = mergesort(seq[:middle])
    right = mergesort(seq[middle:])

    print("left: ", left, "right: ", right)

    return merge(left, right)


a = [5, 8, 2, 7, 1, 9]

print(mergesort(a))
