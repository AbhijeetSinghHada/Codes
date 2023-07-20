SampleNumbers = [1,2,3,4,5,6,7,8,9,10]

doubledNumbers = [number * 3 for number in SampleNumbers]

print(doubledNumbers)

TableOfThree = [f"Table of three {number*3}" for number in SampleNumbers]

TableOfThree = "\n".join([str(numbers) for numbers in TableOfThree])

print(TableOfThree)
