class Solution(object):
    def remove_duplicates(self, some_string):
        """
        :type some_string: str
        :rtype: str
        """
        some = ''
        list_with_doubles = []
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for a in alphabet:
            new_string = a + a
            list_with_doubles.append(new_string)
        is_double = bool
        while is_double:
            for letters in list_with_doubles:
                if letters in some_string:
                    some += letters
                    some_string = some_string.replace(letters, '')
            if some:
                is_double = True
                some = ''
            else:
                is_double = False
        return some_string


    # def __str__(self):
    #     return f'{self.remove_duplicates("abbaca")}'

if __name__ == '__main__':
    my_class = Solution()
    print(my_class.remove_duplicates('abac'))


