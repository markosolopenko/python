from leetcode.binary_tree.diameter_of_binary_tree import TreeNode

class Solution:
    def find_target(self, root: TreeNode, target: int) -> bool:
        list_from_elements = self.traverse_tree(root)
        if len(list_from_elements) > 1:
            for i in range(len(list_from_elements)):
                for j in range(len(list_from_elements)):
                    if list_from_elements[i] + list_from_elements[j] == target and i != j:
                        return True
            return False
        else:
            return False




    def traverse_tree(self, root):
        result = []
        if root:
            result = self.traverse_tree(root.left)
            result.append(root.val)
            result = result + self.traverse_tree(root.right)
        return result


if __name__ == '__main__':
    mine = Solution()
    new_root = TreeNode(5)
    new_root.insert(3)
    new_root.insert(6)
    new_root.insert(2)
    new_root.insert(7)
    new_root.insert(4)
    print(mine.find_target(new_root, 28))