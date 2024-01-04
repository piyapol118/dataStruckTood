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
 
def main(group, all_student):
    """stax"""
    stupid = ArrayStack()
    var_x = [[] for _ in range(0, group)]
    for _ in range(1, all_student+1):
        stupid.push(input())
    for i in range(0, all_student):
        counter = i % group
        var_x[counter].append(stupid.pop())
 
    for i in range(len(var_x)):
        print(f"Group {i+1}:", ", ".join(map(str, var_x[i])))
 
main(int(input()), int(input()))
