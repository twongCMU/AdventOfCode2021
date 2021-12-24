


class ALU():
    def __init__(self):
        self._vars = {"x":0,
                      "y":0,
                      "z":0,
                      "w":0}


    def inp(self, a, val):
        self._vars[a] = val
        
    def add(self, a,b):
        if b in self._vars:
            self._vars[a] += self._vars[b]
        else:
            b = int(b)
            self._vars[a] += b

    def mul(self, a,b):
        if b in self._vars:
            self._vars[a] *= self._vars[b]
        else:
            b = int(b)
            self._vars[a] *= b
            
    def div(self, a,b):
        if b in self._vars:
            self._vars[a] /= self._vars[b]
        else:
            b = int(b)
            self._vars[a] /= b
            self._vars[a] = int(self._vars[a])

    def mod(self, a,b):
        if b in self._vars:
            self._vars[a] %= self._vars[b]
        else:
            b = int(b)
            self._vars[a] %= b

    def eql(self, a,b):
        if b in self._vars:
            if self._vars[a] == self._vars[b]:
                self._vars[a] = 1
            else:
                self._vars[a] = 0
        else:
            b = int(b)
            if self._vars[a] == b:
                self._vars[a] = 1
            else:
                self._vars[a] = 0
                

    def run(self, instructions, inputs):
        i=0
        for row in instructions:
            if "inp" in row:
                if i == 4:
                    print(f"Final ALU {self._vars}")
                    break
                #print(f"***{row} {i}")
                (inp, var) = row.split()
                self.inp(var, inputs[i])
                i+=1
            else:
                #print(f"{row}")
                (instr, var, var2) = row.split()
                if instr == "add":
                    self.add(var, var2)
                if instr == "mul":
                    self.mul(var, var2)
                if instr == "div":
                    self.div(var, var2)
                if instr == "mod":
                    self.mod(var, var2)
                if instr == "eql":
                    self.eql(var, var2)

        #if not self.check():
        return self._vars["z"]


    def check(self):
        if self._vars["z"] == 0:
            return True
        return False


        
