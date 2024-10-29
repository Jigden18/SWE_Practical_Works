# Stack class with size management
class Stack:
    def __init__(self):
        self.items = []
        self.size = 0 

    def is_empty(self):
        return self.size == 0  # Check if stack is empty

    def push(self, item):
        self.items.append(item)  # Add item to the stack
        self.size += 1  # Increment size

    def pop(self):
        if not self.is_empty():
            self.size -= 1  # Decrement size
            return self.items.pop()  # Remove and return the top item
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Return the top item without removing it
        else:
            raise IndexError("Stack is empty")
    
    def get_size(self):
        return self.size  # Return the current size of the stack

# 1. Evaluating Postfix Expressions using a Stack
def evaluate_postfix(expression):
    stack = Stack()
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y if y != 0 else float('inf')}
    
    for token in expression.split():
        if token.isdigit():  # Operand
            stack.push(int(token))
        elif token in operators:  # Operator
            b = stack.pop()
            a = stack.pop()
            result = operators[token](a, b)
            stack.push(result)
        else:
            raise ValueError(f"Unknown token: {token}")

    if stack.get_size() != 1:
        raise ValueError("The expression is not valid.")
    
    return stack.pop()

# testing the evaluate_postfix()
expression = "5 1 2 + 4 * + 3 -"
result = evaluate_postfix(expression)
print(f"The result of the postfix expression '{expression}' is: {result}")

# 2. Implementing a Queue using Two Stacks
class QueueUsingStacks:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        if self.stack2.is_empty():
            raise IndexError("Queue is empty")
        return self.stack2.pop()

    def front(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        if self.stack2.is_empty():
            raise IndexError("Queue is empty")
        return self.stack2.peek()

    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()

    def size(self):
        return self.stack1.get_size() + self.stack2.get_size()

# 3. Task Scheduler using a Queue
class TaskScheduler:
    def __init__(self):
        self.task_queue = QueueUsingStacks()

    def add_task(self, task):
        self.task_queue.enqueue(task)

    def process_tasks(self):
        while not self.task_queue.is_empty():
            task = self.task_queue.dequeue()
            print(f"Processing task: {task}")

# test case
scheduler = TaskScheduler()
scheduler.add_task("Task 1")
scheduler.add_task("Task 2")
scheduler.add_task("Task 3")
scheduler.process_tasks()

# 4. Infix to Postfix Conversion using a Stack
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = Stack()
    output = []

    for token in expression.split():
        if token.isalnum():  # Operand
            output.append(token)
        elif token in precedence:  # Operator
            while (not stack.is_empty() and
                   stack.peek() in precedence and
                   precedence[stack.peek()] >= precedence[token]):
                output.append(stack.pop())
            stack.push(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  # Pop '('
        else:
            raise ValueError(f"Unknown token: {token}")

    while not stack.is_empty():
        output.append(stack.pop())

    return ' '.join(output)

# test case
infix_expression = "A + B * C - D"
postfix_expression = infix_to_postfix(infix_expression)
print(f"The postfix expression of '{infix_expression}' is: {postfix_expression}")
