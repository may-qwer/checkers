def neighborhood(iterable):
    if len(iterable) != 0:
        iterator = iter(iterable)
        current_item = next(iterator)
        for next_item in iterator:
            yield (current_item, next_item)
            current_item = next_item

k = []
l = {1: 'one', 2: 'two', 3: 'tree', 4: 'four'}
for i, j in neighborhood(k):
    print(i, j)
    print(l[i])