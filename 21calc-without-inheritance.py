class Sum():
  sum = 0
  args = [0,0]

  def __init__(self, args):
    self.args[0] = args[0]
    self.args[1] = args[1]
    self.sum = self.args[0]+self.args[1]
  
  def response(self):
    print("The response is: ")
    return self.sum

object_1 = Sum([12,13])

print(object_1.args[0])
print(object_1.args[1])
print(object_1.response())