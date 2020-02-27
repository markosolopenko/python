"""
Should to take two biggest number from list
"""

def two_oldest_ages(ages):
    """
    :param ages:
    :return:
    """
    # arr = []
    # for number in range(0,2):
    #     arr.append(max(ages))
    #     ages.remove(max(ages))
    # return sorted(arr)
    return sorted(ages)[-2:]







print(two_oldest_ages([1, 5, 87, 45, 8, 8]))
