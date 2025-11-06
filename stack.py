# stack.py
class Stack:
    def __init__(self, max_size=None):
        self._stack = []
        self.max_size = max_size

    def push(self, item):
        # prevent duplicates of same ID at top: still allow duplicates generally
        self._stack.append(item)
        if self.max_size and len(self._stack) > self.max_size:
            # remove oldest (bottom of stack)
            self._stack.pop(0)

    def pop(self):
        if self._stack:
            return self._stack.pop()
        return None

    def peek(self):
        if self._stack:
            return self._stack[-1]
        return None

    def items(self):
        # return reversed for most-recent-first
        return list(reversed(self._stack))

    def clear(self):
        self._stack = []