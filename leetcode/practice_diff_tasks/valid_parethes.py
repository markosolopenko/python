class Solution:
    def is_valid(self, s: str) -> bool:
        close_b= '})]'
        open_b = '[({'
        dictionary = {'(':')', '{':'}', '[':']'}
        new_list = []
        for a in s:
            if a in open_b:
                new_list.append(dictionary[a])
            elif a in close_b:
                if not new_list or new_list.pop() != a:
                    return False
        if new_list:
            return False
        return True