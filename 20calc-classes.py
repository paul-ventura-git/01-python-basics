class Operation:
  result = 0

  def __init__(self, argument_1, argument_2):
    self.argument_1 = argument_1
    self.argument_2 = argument_2

class Sum(Operation):
  def __init__(self, argument_1, argument_2):
    super().__init__(argument_1, argument_2)
    
  def sum(self):
    self.result = self.argument_1 + self.argument_2
    return self.result
  
class Substract(Operation):
  def __init__(self, argument_1, argument_2):
    super().__init__(argument_1, argument_2)
    
  def substract(self):
    self.result = self.argument_1 - self.argument_2
    return self.result

class Multiply(Operation):
  def __init__(self, argument_1, argument_2):
    super().__init__(argument_1, argument_2)
    
  def multiply(self):
    self.result = self.argument_1 * self.argument_2
    return self.result
  
class Divide(Operation):
  def __init__(self, argument_1, argument_2):
    super().__init__(argument_1, argument_2)
    
  def divide(self):
    self.result = self.argument_1 / self.argument_2
    return self.result

object_1 = Sum(33, 89)
object_2 = Substract(33, 89)
object_3 = Multiply(33, 89)
object_4 = Divide(33, 89)

print(object_1.sum())
print(object_2.substract())
print(object_3.multiply())
print(object_4.divide())