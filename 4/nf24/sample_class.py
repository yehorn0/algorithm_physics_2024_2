class SampleClass:
    def __init__(self, v):
        self.v = v

    def multiply_value(self, multiplier=2):
        return self.v * multiplier

    # @staticmethod
    # def add(a, b):
    #     return a + b


sample_object = SampleClass(5)
print(sample_object.multiply_value())

sample_object_2 = SampleClass.__new__(SampleClass)
SampleClass.__init__(sample_object_2, 10)

print(SampleClass.multiply_value(sample_object_2, multiplier=5))
