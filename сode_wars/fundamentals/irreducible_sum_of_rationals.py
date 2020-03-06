from fractions import Fraction

from typing import List

####### Very bad solution #######
# def sum_fracts(lst):
#     array_chiselnuk = []
#     array_znamennuk = []
#     similar_divide = 0
#     divivse = []
#     common_divide = []
#     for a in lst:
#         for b in a:
#             array_chiselnuk.append(a[0])
#             array_znamennuk.append(a[1])
#             break
#     for i in range(1, 10000):
#         for j in array_znamennuk:
#             if array_znamennuk.count(j) == len(array_znamennuk):
#                 similar_divide = j
#                 break
#             else:
#                 if i % int(j) == 0:
#                     divivse.append(i)
#                     if divivse.count(i) == len(array_znamennuk):
#                         common_divide.append(i)
#                         break
#                     continue
#     if similar_divide:
#         if sum(array_chiselnuk) % similar_divide == 0:
#             return int(sum(array_chiselnuk) / similar_divide)
#         else:
#             return [sum(array_chiselnuk), similar_divide]
#     else:
#         first_divide = common_divide[0]
#         sum_of_chiselnuka = 0
#         for num in range(len(array_chiselnuk)):
#             multipli = first_divide / array_znamennuk[num]
#             sum_of_chiselnuka += multipli * array_chiselnuk[num]
#         if sum_of_chiselnuka % first_divide == 0:
#             return int(sum_of_chiselnuka / first_divide)
#         else:
#             return [int(sum_of_chiselnuka), int(first_divide)]


#####Little better solution####
def sum_fracts(rationals: List[list]):
    suma = 0
    if rationals:
        for (a, b) in rationals:
            suma += Fraction(a, b)
        silt = []
        let = str(suma).split("/")
        for s in let:
            if len(let) == 1:
                return int(s)
            silt.append(int(s))
        return silt


if __name__ == "__main__":
    print(sum_fracts([[69, 130], [87, 1310], [3, 4]]))

