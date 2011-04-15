class cached_func(object):
    size = 10

    def __init__(self, func):
        self.func = func
        self.cache = {}        
        self.used = []
        self.__name__ = func.__name__
        self.__doc__ = func.__doc__

    def __call__(self, *args):
        #print self.__name__, "being called with", args
        if not self.cache.has_key(args):
            print "not cached"

            if len(self.used) == self.size:
                print "cache full"
                del self.cache[self.used.pop(0)]

            self.cache[args] = self.func(*args)
            self.used.append(args)
                                                    
        else:
            print "cached"            

        return self.cache[args]

@cached_func
def fib(x):
    if x < 2:
        return x

    return fib(x-2) + fib(x-1)


