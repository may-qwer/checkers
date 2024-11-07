# def generator_with_stop(arr, stap, next_stap, stop_item):
#     temp_dict = {i: stap for i in arr[next_stap:]}
#     for key, value in temp_dict.items():
#         if key == stop_item:
#             break
#         yield {key: value}
#
# k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# l = {}
# for item in generator_with_stop(k, 3, 4, 6):
#     l.update(item)
# print(l)

l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
print(l[1])
print(l[l.index(44)])