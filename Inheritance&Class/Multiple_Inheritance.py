class Dad() :
    def skills(self):
        print("gardening, programming")

class Mom() :
    def skills(self):
        print("cooking, art")

class Kid(Dad, Mom):
    def skills(self):
        Jui.skills(self)
        Durgesh.skills(self)
        print("sports")

a = Aum()
a.skills()
