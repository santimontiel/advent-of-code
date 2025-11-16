import time

def summary(f):

    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print(f"Summary for {f.__name__}:")
        print(f"   >>> Result: {result}")
        print(f"   >>> Time: {((te-ts) * 1e3):.3f} ms")
        return result

    return timed