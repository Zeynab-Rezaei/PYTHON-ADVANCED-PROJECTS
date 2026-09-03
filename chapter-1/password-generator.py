#modules and global variables
from abc import ABC, abstractmethod 
import string
import random
#create password generator abstract class
class PasswordGeneratirAbstract(ABC):
    @abstractmethod
    def geneerate_password(self, length=8):
        pass

#create numeric password generator
class NumericPasswordGenerator(PasswordGeneratirAbstract):
    letters = string.digits
    def geneerate_password(self, length=8):
        return "".join(str(random.choice(self.letters)) for _ in range(length))

    
#create letters password generator 
class LetterPasswordGenerator(PasswordGeneratirAbstract):
    letters = string.ascii_letters
    def geneerate_password(self, length=8):
        return "".join(str(random.choice(self.letters)) for _ in range(length))


#create mixed password ganerator
class MixPasswordGenerator(PasswordGeneratirAbstract):
    letters = string.ascii_letters + string.digits
    def geneerate_password(self, length=8):
        return "".join(str(random.choice(self.letters)) for _ in range(length))


#run the application
generator1 = NumericPasswordGenerator()
generator2 = LetterPasswordGenerator()
generator3 = MixPasswordGenerator()

print(generator1.geneerate_password())
print(generator2.geneerate_password(20))
print(generator3.geneerate_password(30))


