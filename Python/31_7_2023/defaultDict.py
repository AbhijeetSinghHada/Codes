from collections import defaultdict

val = [('Rolf','MIT',7.5),('Jen','Oxford',7.2),('Jen','Cambridge',7.8),('Charlie','Oxford',7.6),('Charlie','Cambridge',7.8),('Charlie','MIT',7.4),('Jen','MIT',7.9),('Rolf','Oxford',7.4),('Rolf','Cambridge',7.5)]

college_dict = defaultdict(list)

for i in val:
    college_dict[i[0]].append(i[1])
    
print(college_dict['Rolf'])
print(college_dict['Abhi'])

####################################################################################
print('\n\n******************************************************************************\n\n')
my_company = 'Google'
coworkers =['Abhi','Kittu','Tunnu']
other_coworkers = [('Rolf','Apple'),('Jen','Amazon'),('Anna','Facebook'),('Charlie','Microsoft')]

coworkers_companies = defaultdict(lambda: my_company)

for person,company in other_coworkers:
    coworkers_companies[person]=company
    
print(coworkers_companies['Abhi'])