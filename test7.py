class vechicle:
    def set_vechicle(self):
        self.vechicle_name="i am a vechicle"
class fourwheler(vechicle):
    def set_fourwheler(self):
        self.fourwheler_name="i am a four wheeler"
class car(fourwheler):
    def set_car(self):
        self.car_name="i am a car"
    def display (self):
        print(self.car_name)
        print(self.fourwheler_name)
        print(self.vechicle_name)
a=car()
a.set_car()
a.set_fourwheler()
a.set_vechicle()
a.display()