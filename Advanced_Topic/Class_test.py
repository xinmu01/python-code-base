# python class practice

class test_str:
    '''
    Hello world!
    '''
    def __str__(self):
        return "This is a test"

test = test_str()

print (test)
print (test.__doc__)
print (test_str.__doc__)
help(test_str)
help(test)