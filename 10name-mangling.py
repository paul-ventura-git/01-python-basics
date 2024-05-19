
# mangled names aren’t available for direct access.
class SampleClass:
  def __init__(self, value):
    self.__value = value
  def __method(self):
    print(self.__value)

sample_instance = SampleClass("Hello!")

print(vars(sample_instance))
print(vars(SampleClass))

# This internal behavior hides the names, creating the illusion of a private attribute or method.
# However, they’re not strictly private. You can access them through their mangled names:

print(sample_instance._SampleClass__value)
print(sample_instance._SampleClass__method())

# Name mangling is particularly useful when you want to ensure that a given attribute or method won’t get accidentally overwritten. 
# It’s a way to avoid naming conflicts between classes or subclasses. 
# It’s also useful to prevent subclasses from overriding methods that have been optimized for better performance.