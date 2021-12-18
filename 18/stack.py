import re


# I started out thinking I needed a stack but really this is just a list
# representation of the string split into tokens
class Stack():
    def __init__(self):
        self._stack = []

    def push(self, value):
        self._stack.append(value)

    def pop(self):
        value = self._stack.pop(-1)
        return value

    
    def create(self, string):
        # convert string to tokenized list
        i = 0
        while i < len(string):
            if string[i:i+1] == "[":
                self.push("[")
                i+=1
            elif string[i:i+1] == "]":
                self.push("]")
                i+=1
            elif string[i:i+1] == ",":
                self.push(",")
                i+=1
            else:
                #print(f"number {string[i:]} {i} {len(string)}")
                res = re.match(r"(^\d+)", string[i:])
                self.push(int(res.group()))
                i+=len(res.group())

    def get_string(self):
        # convert tokenized list to string
        string = ""
        for v in self._stack:
            string+=f"{v}"
        return string

    def find_depth_4(self):
        # Returns index into stack where 5th nested thing is
        depth = 0
        for i, v in enumerate(self._stack):
            if v == "[":
                depth+=1
                if depth == 5:
                    return i
            elif v == "]":
                depth-=1


        return None
    
    def find_next_number(self, start, direction):
        # from a given position find the next number's index
        # to the right or left (direction = 1, or -1)
        while start < len(self._stack) and start >= 0:
            v = self._stack[start]
            if v == "[" or v == "]" or v == ",":
                start+=direction
                continue
            
            return start
        return None

        
    def explode(self):
        start = self.find_depth_4()
        if start is None:
            return False
        #print("explode")
        a = self._stack[start+1]
        b = self._stack[start+3] #+2 is the comma between them

        # +5 is one after the closing brace
        next_right = self.find_next_number(start+5, 1)
        next_left = self.find_next_number(start, -1)

        if next_right is not None:
            self._stack[next_right] += b
        if next_left is not None:
            self._stack[next_left] += a

        self._stack.pop(start+4)
        self._stack.pop(start+3)
        self._stack.pop(start+2)
        self._stack.pop(start+1)
        self._stack[start] = 0

        return True
            
    def split_num(self):
        #print("split")
        i = 0
        while i < len(self._stack):
            if type(self._stack[i]) == int:
                if self._stack[i] >= 10:
                    a = int(self._stack[i]/2)
                    b = a

                    if a+b < self._stack[i]:
                        b += 1

                    self._stack[i] = "["
                    self._stack.insert(i+1, a)
                    self._stack.insert(i+2, ",")
                    self._stack.insert(i+3, b)
                    self._stack.insert(i+4, "]")
                    
                    return True
            i+=1
        return False

    def compute_sum(self):
        stop = 1000
        while len(self._stack) > 1 and stop > 0:
            #print(f"Computing sum {self._stack}")
            for i in range(len(self._stack)-4):
                if self._stack[i] == "[" and self._stack[i+2] == "," and self._stack[i+4] == "]":
                    val = 3*self._stack[i+1] + 2*self._stack[i+3]
                    self._stack.pop(i+4)
                    self._stack.pop(i+3)
                    self._stack.pop(i+2)
                    self._stack.pop(i+1)
                    self._stack[i] = val
                    break
                i+=1
                
            stop-=1
        return self._stack[0]
                
