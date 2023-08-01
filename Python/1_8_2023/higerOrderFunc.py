# def asfa(func):
#     func()

# asfa(lambda: 5)

movies = [
    {'name': 'The Matrix', 'director': 'Wachowski'},
    {'name': 'The Godfather', 'director': 'Francis Ford Coppola'},
    {'name': 'Pulp Fiction', 'director': 'Quentin Tarantino'},
    {'name': 'Titanic', 'director': 'James Cameron'},
    {'name': 'Shawshank Redemption', 'director': 'Frank Darabont'},
    {'name': 'The Dark Knight', 'director': 'Christopher Nolan'},
    {'name': 'Forrest Gump', 'director': 'Robert Zemeckis'}
]


def find_movie(expected,finder):
    for movie in movies:
        if finder(movie) == expected:
            return movie


find_by = input("Enter the property to find by : ")
looking_for = input("Enter what you are looking for : ")

temp =find_movie(looking_for,lambda movie: movie[find_by])
print(temp or "No Movie Found")