import re

expression = '[A-z\.]+@[a-z]+\.[a-z]+'
email = 'abhijeet.hada@gmail.com'

matches = re.findall(expression, email)

print(matches)

# price = 'Price: $10,023.24'
# expression = 'Price: \$([0-9,]*.[0-9]*)'

# match = re.search(expression,price)
# print(match.group(0))
# print(match.group(1))

# priceNumber = match.group(1).replace(',','')
# priceNumber = float(priceNumber)
# priceNumber +=1000

# print(priceNumber)
