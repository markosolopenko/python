from leetcode.binary_tree.diameter_of_binary_tree import TreeNode


class Solution:
    def get_minimum_difference(self, root: TreeNode) -> int:
        elements = self.convert_to_list(root)
        new_list = []
        for a in range(len(elements)):
            if a == len(elements) - 1:
                break
            else:
                if elements[a] > elements[a + 1]:
                    new_list.append(elements[a] - elements[a + 1])
                else:
                    new_list.append(elements[a+1] - elements[a])
        return min(new_list)

    def convert_to_list(self, root):
        res = []
        if root:
            res = self.convert_to_list(root.left)
            res.append(root.val)
            res = res + self.convert_to_list(root.right)
        return res




if __name__ == '__main__':
    mine = Solution()
    node = TreeNode(1)
    node.insert(2)
    node.insert(3)
    print(mine.get_minimum_difference(node))