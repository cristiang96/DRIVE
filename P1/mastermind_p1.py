class Mastermind:
    """ 
    Given two strings this class determine how many characters are in the same position and are equal ("r"), and then how many characters are left and are equal in both strings("s") 
    """
    def __init__(self, n, s1, s2):
        self.n = n
        self.s1 = s1
        self.s2 = s2

    def check_same_position(self):
        self._aux_s1 = self.s1
        self._aux_s2 = self.s2
        self._r = 0
        self._s = 0
        ite = 0
        while ite < len(self._aux_s1):
            if self._aux_s1[ite] == self._aux_s2[ite]:
                self._r+=1
                self._aux_s1 = self._aux_s1[0:ite]+self._aux_s1[ite+1:]
                self._aux_s2 = self._aux_s2[0:ite]+self._aux_s2[ite+1:]
            else:
                ite+=1

        return self._r

    def check_characters_left(self):
        for i in set(self._aux_s1):
            self._s+= min(self._aux_s1.count(i),self._aux_s2.count(i))

        return self._s

"""
Checking Input
"""
#Sample Input: 4 BACC BDSA
while True:
    input_variables = input().split(" ")
    n, s1, s2 = input_variables
    if int(n) > 50:
        print( """Error "n": it must be lower than or equal to 50""")
        print( """Try again: """)
        continue
    if not s1.isupper():
        print( """Error "string1": it must be made up of upper-case alphabetic characters only""")
        print( """Try again: """)
        continue
    if not s2.isupper():
        print( """Error "string2": it must be made up of upper-case alphabetic characters only""")
        print( """Try again: """)
        continue
    break

test1 = Mastermind(n,s1,s2)
print(test1.check_same_position(), test1.check_characters_left())