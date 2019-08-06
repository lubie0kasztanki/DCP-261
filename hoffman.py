class node():

    val = "*"
    left = None
    right = None
    
    #st for string representing a letter
    #let for a letter

    def add(self, st, let):
        if len(st) == 1:
            if st == "0":
                self.left = node()
                self.left.val = let
            
            if st == "1":
                self.right = node()
                self.right.val = let
        
        else:
            if st[0] == "0":
                if self.left:
                    self.left.add(st[1:], let)

                else:
                    self.left = node()
                    self.left.add(st[1:], let)

            if st[0] == "1":
                if self.right:
                    self.right.add(st[1:], let)

                else:
                    self.right = node()
                    self.right.add(st[1:], let)
    
    def get(self, st):
        if len(st) == 1:
            if st == "0":
                return self.left.val
            if st == "1":
                return self.right.val
        else:
            if st[0] == "0":
                return self.left.get(st[1:])
            if st[0] == "1":
                return self.right.get(st[1:])
                    
    def build(self, tab):
        for letter, st in tab.items():
            self.add(st, letter)



#example with some data, r is a root node
tab = {
    'a' : '01', 'c' : '000', 't' : '10', 's' : '111'}

r = node()
r.build(tab)
print(r.get('01'))


