"""
Find all multiples of 3 and 5 below (this number)
"""
def solution(number):
    count_multiples = 0
    for num in range(3,number):
        if num % 5 == 0 and num % 3 == 0:
            count_multiples += num
        elif num % 3 == 0 or num % 5 == 0:
            count_multiples += num
    return count_multiples

if __name__ == "__main__":
    print(solution(10))

