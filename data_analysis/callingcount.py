

class CallingCounter(object):
    def __init__ (self, func):
        self.func = func
        self.count = 0

    def __call__ (self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)



class Test:
    @CallingCounter
    def test():
        print('我被调用了')

for i in range(10):
    Test.test()

print(f'我被调用了{Test.test.count}次')