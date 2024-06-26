from __future__ import annotations
from typing import Any


class Stack:
    def __init__(self) -> None:
        self.items: list[Any] = []

    def push(self, item: Any) -> Stack:
        self.items.append(item)
        return self

    def pop(self) -> Any:
        if self.__bool__():
            return self.items.pop()
        else:
            raise ValueError("Stack is empty")

    def __bool__(self) -> bool:
        return len(self.items) > 0


stack = Stack()
stack.push(1).push(2).push(3).pop()
print(stack.items)
