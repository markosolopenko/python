def buddy_strings(string_to_swap: str, string_to_check: str) -> bool:
    if len(string_to_swap) != len(string_to_check):
        return False
    s = False
    count = 0
    t = 0
    for i in range(len(string_to_swap)):
        if string_to_swap[i] not in string_to_check or string_to_check[i] not in string_to_swap or \
                string_to_swap.count(string_to_swap[i]) != string_to_check.count(string_to_check[i]):
            s = False
            break
        elif string_to_swap.count(string_to_swap[i]) == 1:
            t += 1
        elif string_to_swap.count(string_to_swap[i]) == len(string_to_swap) and \
                string_to_check.count(string_to_check[i]) == len(string_to_check):
            s = True
            break
        elif string_to_swap[i] != string_to_check[i] and \
                string_to_swap.count(string_to_swap[i]) == string_to_check.count(string_to_swap[i]):
            s = True
            count += 1
        elif string_to_swap.count(string_to_swap[i]) == string_to_check.count(string_to_swap[i]) and \
                string_to_swap.count(string_to_swap[i]) != 1 and len(string_to_swap) > 2:

            s = True

    if s and count <= 2 and t != len(string_to_swap):
        return True
    return False




    # s = False
    # count = 0
    # for i in range(len(A)):
    #     if A.count(A[i]) != B.count(B[i]) or B[i] not in A:
    #         s = False
    #         break
    #     elif A.count(A[i]) == len(A) and B.count(B[i]) == len(B):
    #         s = True
    #         break
    #     elif A[i] != B[i] and A.count(A[i]) == B.count(B[i]):
    #         count += 1
    #         s = True
    # if s and count <= 2:
    #     return True
    # return False



if __name__ == '__main__':
    print(buddy_strings('abab', 'abab'))
