from leetcode.binary_tree.diiferent_task_with_binary_tree.diameter_of_binary_tree import TreeNode


class Solution:
    def convert_bst(self, root: TreeNode) -> TreeNode:
        list_elements = self.convert_to_list(root)
        new_list = []
        for i in range(len(list_elements)):
            res = list_elements[i]
            for j in range(len(list_elements)):
                if i != j and list_elements[i] < list_elements[j]:
                    res += list_elements[j]
            new_list.append(res)
        if new_list:
            new_root = TreeNode(new_list.pop(0))
            for a in new_list:
                self.insert_element(new_root, a)
            return new_root

    def convert_to_list(self, root):
        res = []
        if root:
            res.append(root.val)
            res = res + self.convert_to_list(root.right)
            res = res + self.convert_to_list(root.left)
        return res

    def insert_element(self, root: TreeNode, value):
        if root:
            if root.val < value:
                if root.left is None:
                    root.left = TreeNode(value)
                else:
                    self.insert_element(root.left, value)
            elif root.val > value:
                if root.right is None:
                    root.right = TreeNode(value)
                else:
                    self.insert_element(root.right, value)


# def bst_size(self, root, count=0):
    #     if root is None:
    #         return count
    #     return self.bst_size(root.left, self.bst_size(root.right, count + 1))

if __name__ == '__main__':
    mine = Solution()
    new_node = TreeNode(2)
    new_node.insert(0)
    new_node.insert(3)
    new_node.insert(-4)
    new_node.insert(1)
    # print(mine.bst_size(new_node))
    # print(new_node.val, new_node.left.val, new_node.right.val, new_node.left.right.val)
    # print(mine.convert_to_list(new_node))
    some = mine.convert_bst(new_node)
    print(some.val, some.left.val, some.right.val, some.left.right.val, some.right.left.val)
