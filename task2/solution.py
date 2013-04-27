from collections import defaultdict
from collections import deque


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


def zip_with(func, *iterables):
    for args in zip(*iterables):
        yield func(*args)


def cache(func, cache_size):
    cache = deque(maxlen=cache_size)

    def func_cached(*args):
        for cache_args, cache_value in cache:
            if cache_args == args:
                return cache_value
        next_cache = func(*args)
        cache.append((args, next_cache))
        return next_cache

    return func_cached
