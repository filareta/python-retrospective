from collections import defaultdict
from collections import OrderedDict


def groupby(func, seq):
    keys = map(func, seq)
    group_values = defaultdict(list)
    iterator = iter(keys)
    for item in seq:
        group_values[next(iterator)].append(item)
    return group_values


def composer(f, g):
    return lambda x: f(g(x))


def iterate(func):
    yield lambda x: x
    composition = func
    while True:
        yield composition
        composition = composer(func, composition)


def length(iterable):
    for index, item in enumerate(iterable):
        length_ = index + 1
    return length_


def zip_with(func, *iterables):
    if not all([item is None for item in iterables]):
        min_length = min(map(length, iterables))
        for i in range(min_length):
            yield func(*(map(lambda k: k[i], iterables)))


def cache(func, cache_size):
    def func_cached(*args):
        if not hasattr(func, '_cache'):
            func._cache = OrderedDict()
        if len(func._cache) > cache_size:
            func._cache.popitem(False)
        if not args in func._cache:
            func._cache[args] = func(*args)
        return func._cache[args]
    return func_cached
