def mul(a):
    def helper(b):
        return a * b
    return helper
three_mul=mul(3)
print(three_mul(5))

def first_test():
    print("Test function 1")

def second_test():
    print("Test function 2")

def simple_decore(fn):
    def wrapper():
        print("Start function")

    fn()
    print("Stop function")
    return wrapper

first_test_wrapped=simple_decore(first_test)
second_test_wrapped=simple_decore(second_test)

