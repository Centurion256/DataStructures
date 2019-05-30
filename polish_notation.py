import re
from Stack.Stack import Stack

class PolishExpression(object):

    def __init__(self, expr):

        self.expr = re.findall(r"(?m)\*{2}|\d{1,}|[-+*/^]",expr)
        self.expr = ["**" if (x == "^") or (x == "↑") else x for x in self.expr]
    
    def __str__(self):

        return " ".join(self.expr)

class PrefixExpression(PolishExpression):

    def evaluate(self):

        op_stack = Stack()
        num_stack = Stack()
        expr = self.expr[:]
        while expr:

            char = expr.pop()
            if re.match(r"\d{1,}", char):

                    num_stack.push(char)
            
            else:

                    op_stack.push(char)

            if not op_stack.is_empty():

                num_stack.push(eval(f"{num_stack.pop()}{op_stack.pop()}{num_stack.pop()}"))

        return int(num_stack.pop())


class PostfixExpression(PolishExpression):

    @staticmethod
    def evaluate(self):

        op_stack = Stack()
        num_stack = Stack()
        expr = self.expr[:]
        while expr:

            char = expr.pop(0)
            if re.match(r"\d{1,}", char):

                    num_stack.push(char)
            
            else:

                    op_stack.push(char)

            if not op_stack.is_empty():

                num_stack.push(eval("{num1}{op}{num2}".format(num2 = num_stack.pop(), num1 = num_stack.pop(), op = op_stack.pop())))

        return int(num_stack.pop())

    def to_prefix(self):

        """Fully functional."""

        num_stack = Stack()
        expr = self.expr[:]
        prefix = []
        while expr:

            char = expr.pop(0)
            if re.match(r"\d{1,}", char):

                num_stack.push(char)
                continue

            tmp_lst = []
            tmp_lst.insert(0, num_stack.pop())
            tmp_lst.insert(0, num_stack.pop())
            tmp_lst.insert(0, char)
            num_stack.push(" ".join(tmp_lst))
        
              
        while not num_stack.is_empty():

            prefix.append(num_stack.pop())
        
        return " ".join(prefix)

def main():

    expr = PrefixExpression("/ - * 2 5 * 1 2 - 11 9")
    #x = expr.evaluate()
    #assert(expr.evaluate(), 4)


if __name__ == "__main__":
    
    import auger
    with auger.magic([PostfixExpression, PrefixExpression]):

        main()