from collections import Counter

temprature_list = [36.5, 37, 37.5, 39, 38.5, 37.5, 37, 36.5, 37.5, 36.5, 38.5, 39, 36.5, 37, 37.5, 39]
count = Counter(temprature_list)
print(count[36.5])