
# mangled names aren’t available for direct access.
class SampleClass:
  def __init__(self, value):
    self.__value = value
  def __method(self):
    print(self.__value)

sample_instance = SampleClass("Hello!")

print(vars(sample_instance))
print(vars(SampleClass))

print(sample_instance.__value)
print(sample_instance.__method())