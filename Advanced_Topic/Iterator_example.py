class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    # After define the __iter__, the iter() and for in loop can be used.
    def __iter__(self):
        return self

    #As long as define __next__, the next() can be used.
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
    
    def reset(self):
        self.index = len(self.data)

a = Reverse("I am Xin")
print (next(a))
for i in a:
    print (i)
print()

a.reset()
for i in a:
    print(i)
print()

a.reset()
b = iter(a)
print (next(b))
for i in b:
    print(i)
print()

##Convert List to Iterator
test_list = [1,2,3]
test_list_iter = iter(test_list)
print(next(test_list_iter))
print(next(test_list_iter))
print(next(test_list_iter))

##Generator Example
def generator_example(a):
    for i in a:
        yield i

generator_example = generator_example([1,2,3])
print(next(generator_example))
for i in generator_example:
    print (i)




