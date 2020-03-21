class Solution(object):
    def remove_outer_parentheses(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        open_brace = '('
        close_brace = ')'
        some_other_list = []
        for a in range(len(expression)):
            if a == 0 or a == len(expression) - 1:
                continue
            some_other_list.append(expression[a])
        print(some_other_list)
        new_list = []
        some_string = ''
        for brace in some_other_list:
            if brace is open_brace:
                new_list.append(close_brace)
            elif brace is close_brace:
                if not new_list or brace != close_brace:
                    some_other_list.remove(brace)
        return some_other_list
my_class = Solution()
print(my_class.remove_outer_parentheses('(()())(())'))
