from string import ascii_letters
spisok=[]
class Index:

    def __init__(self, spisok):
        self.spisok = spisok

    def __getitem__(self, item):
          return self.spisok[item-1]

    def __setitem__(self, item, value):
        self.spisok[item-1] = value

    def __str__(self):
        print( self.spisok.str)

spisok = Index([0, 1, 2, 3])
print(spisok[1])