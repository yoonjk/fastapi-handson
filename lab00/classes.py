
class Animals:
  def __init__(self, eyes, ears):
    self.eyes = eyes
    self.ears = ears 
    
  def shout(self, sound):
    print(f"{sound} {sound} {sound}")
    
class Mammals(Animals):
  def __init__(self, eyes, ears, legs, arms):
    Animals.__init__(self, eyes, ears)
    self.legs = legs 
    self.arms = arms 
  
  def run(self):
    print('run run run run')
  
class Birds(Animals):
  def __init__(self, eyes, ears, legs, wings):
    Animals.__init__(self, eyes, ears)
    self.legs = legs 
    self.wings = wings 
    
  def fly(self):
    print('fly fly fly')
    
class Hybrid(Mammals, Birds):
  def __init__(self, eyes, ears, legs, arms, wings):
    Mammals.__init__(self, eyes, ears, legs, arms)
    Birds.__init__(self, eyes, ears, legs, wings)

unicorn = Hybrid(eyes = 2, ears = 2, legs = 4, arms = 0, wings = 2)

unicorn.fly()

  