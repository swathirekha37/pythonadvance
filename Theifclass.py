import random

class Thief:
    sneaky=True

    def pickpocket(self):
        print("called by {}" .format(self))
        return bool(random.randint(0,1))

sepher=Thief()
print(sepher.sneaky)
sepher.sneaky=False
print(sepher.sneaky)
print(sepher.pickpocket()) 