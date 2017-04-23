import time


def time_it(method):
    def timed(*args, **kwars):
        t_s = time.time()
        result = method(*args, **kwars)
        t_e = time.time()

        print('%r in %2.2f sec' % (method.__name__, t_e - t_s))
        return result

    return timed
