store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]
cheapest = map(min, store1, store2)
cheapest

for item in cheapest:
    print(item)

print(store1[2])
a = str(store2[:2])
print(a)
print(type(2))


a = [1, 2, 3, 4]
b = [2, 1, 2, 5]
print(map(max, a, b))