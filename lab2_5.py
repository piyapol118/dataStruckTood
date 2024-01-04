"""stack"""
class ArrayStack:
    """alo"""
    def __init__(self):
        """alo"""
        self.size = 0
        self.data = []
 
    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1
 
    def pop(self):
        """alo"""
        self.size -= 1
        if self.data != []:
            return self.data.pop(-1)
        else:
            print("Underflow: Cannot pop data from an empty list")
            return None
 
    def is_empty(self):
        """popop"""
        return self.data == []
 
    def get_stack_top(self):
        """alo"""
        if self.data != []:
            return self.data[-1]
        else:
            print("Underflow: Cannot get stack top from an empty list")
            return None
 
    def get_size(self):
        """alo"""
        return self.size
 
    def print_stack(self):
        """alo"""
        print(self.data)
 
def is_parentheses_matching(text):
    stacking = ArrayStack()
    counter_1 = text.count("(")
    counter_2 = text.count(")")
    for i in text:
        if i == "(":
            stacking.push(i)
        elif i == ")":
            stacking.pop()
 
    if stacking.is_empty() == True and (counter_1 == counter_2):
        print("Parentheses in %s are matched" % text)
        print(True)
    else:
        print("Parentheses in %s are unmatched" % text)
        print(False)
 
 
is_parentheses_matching(input())
