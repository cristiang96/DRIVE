class musicNotation:
    """
    This class prints a sequence of notes of specified pitches and durations in a text-based pentagram representation 
    """
    def __init__(self,n,notesList):
        self.dicNot = {"G":"","F":"","E":"","D":"","C":"","B":"","A":"","g":"","f":"","e":"","d":"","c":"","b":"","a":""}
        self.aux=["F","D","B","g","e","a"]
        self.notes_list = notesList
        self.__n = n

    def representation(self):
        for i in self.notes_list:
            letter = i[0]
            times = int(i[1:]) if len(i)>1 else 1 
            # print(letter,times,line)
            for j in self.dicNot.keys():
                if j in self.aux:
                    self.dicNot[j] +="-"*(times+1)
                else:
                    self.dicNot[j] +=" "*(times+1)

            line = self.dicNot[letter] 
            self.dicNot[letter] = line[0:-times-1]+"*"*times+"-" if letter in self.aux else line[0:-times-1]+"*"*times+" "

        self._printTextBased()

    def _printTextBased(self):
        for let, val in self.dicNot.items():
            print(f"{let}: {val}")

"""
Checking Input
"""
#Sample Input: 
#  n = 27   
#  notes = "C C D E C E D2 C C D E C2 B2 C C D E F E D C B g A B C2 C2"
while True:
    n = input()
    if not int(n) >= 1 and int(n) <= 100:
        print( """Error "n": it must be in the range of 1 to 100""")
        print( """Try again: """)
        continue
    notes = input().split(" ")
    if not len(notes)==int(n):
        print(f"Error \"length\": it doesn't match with the integer \"n\": {int(n)}")
        print( """Try again: """)
        continue
    break
"test: " 


test1 = musicNotation(n, notes)
test1.representation()


