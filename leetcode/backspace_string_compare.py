class Solution(object):
    def backspace_compare(self, first_string, second_string):
        """
        Remove all hash and element at front of him, if hash still in string remove it
        :param first_string:
        :param second_string:
        :return:
        """
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        hash_tag = '#'
        new_list = []
        some = ''
        for a in alphabet:
            new_list.append(a + hash_tag)
        is_hash = bool
        while is_hash:
            for letters in new_list:
                if letters in first_string:
                    first_string = first_string.replace(letters, '')
                    some += letters
                elif letters in second_string:
                    second_string = second_string.replace(letters, '')
                    some += letters
            if some:
                is_hash = True
                some = ''
            else:
                is_hash = False

        if hash_tag in first_string:
            first_string = first_string.replace(hash_tag, '')
        if hash_tag in second_string:
            second_string = second_string.replace(hash_tag, '')
        return first_string == second_string




my_class = Solution()
print(my_class.backspace_compare('a##c', '#a#c'))