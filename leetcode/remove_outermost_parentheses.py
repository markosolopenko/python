class Solution(object):
    def remove_outer_parentheses(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        new_list = []
        open_brace = '('
        close_brace = ')'
        string = ''
        new_string = ''
        for element in expression:
            if element is open_brace:
                string += open_brace
            elif element is close_brace:
                string += close_brace
                if string.count(open_brace) == string.count(close_brace):
                    new_list.append(string)
                    string = ''
        for a in new_list:
            for i in range(len(a)):
                if i == 0 or i == len(a) - 1:
                    continue
                else:
                    new_string += a[i]
        return new_string

    




my_class = Solution()
print(my_class.remove_outer_parentheses("(()())(())(()(()))"))


