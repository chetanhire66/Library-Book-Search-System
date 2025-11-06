# bst.py
class Node:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, book_id, title, author):
        node = Node(book_id, title, author)
        if not self.root:
            self.root = node
            return
        current = self.root
        while True:
            if book_id < current.book_id:
                if current.left:
                    current = current.left
                else:
                    current.left = node
                    return
            elif book_id > current.book_id:
                if current.right:
                    current = current.right
                else:
                    current.right = node
                    return
            else:
                # duplicate id: replace data
                current.title = title
                current.author = author
                return

    def search(self, book_id):
        current = self.root
        while current:
            if book_id == current.book_id:
                return current
            elif book_id < current.book_id:
                current = current.left
            else:
                current = current.right
        return None

    def inorder(self):
        result = []

        def _inorder(node):
            if not node:
                return
            _inorder(node.left)
            result.append({"id": node.book_id, "title": node.title, "author": node.author})
            _inorder(node.right)

        _inorder(self.root)
        return result

    def delete(self, book_id):
        def _delete(node, key):
            if not node:
                return None
            if key < node.book_id:
                node.left = _delete(node.left, key)
            elif key > node.book_id:
                node.right = _delete(node.right, key)
            else:
                # node found
                if not node.left and not node.right:
                    return None
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                # two children: find inorder successor
                succ = node.right
                while succ.left:
                    succ = succ.left
                node.book_id, node.title, node.author = succ.book_id, succ.title, succ.author
                node.right = _delete(node.right, succ.book_id)
            return node

        self.root = _delete(self.root, book_id)