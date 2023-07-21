class MovieCollection:
    def __init__(self):
        self.MovieData = []

    def _UserPrompt(self):
        print("""\n********** Movie Collection **********
Enter 1 to Add Movie
Enter 2 to Remove Movie
Enter 3 to View All Movies
Enter 4 to Search for a Movie
Enter q to Quit\n""")  
        
    def Menu(self):
        while True:
            menuDict ={
                "1" : self.add_movie,
                "2" : self.remove_movie,
                "3" : self.view_movie,
                "4" : self.search_movie,
                "q" : print("Thank You Visiting...")
            }
            self._UserPrompt()   # could be anther variable for the string
            UserInput = input()    # snake case in python and all these selections could be stored in a dict
            if UserInput in menuDict:
                menuDict[UserInput]()
            else:    
                print("Invalid Input, Please Try Again")
                
        
    def add_movie(self):
        MovieNumber = len(self.MovieData)+1
        name = input("\nEnter Name of Movie : ")
        year = input("Enter Year of Movie Release : ")
        duration = input("Enter Duration of Movie : ")
        rating = input("Enter Rating of Movie : ")
        
        movie = {
            "Movie Number" : MovieNumber,
            "Name" : name,
            "Year" : year,
            "Duration" : duration,
            "Rating" : rating   
        }
        self.MovieData.append(movie)
    
    def fetch_moive_via_obj(movie):
            print(f"""\n\nMovie Number : {movie["Movie Number"]}
Name : {movie["Name"]}
Year : {movie["Year"]}
Duration : {movie["Duration"]}
Rating : {movie["Rating"]}\n
                  """) # could be used as single prints
            
            
    def view_movie(self):
        for movie in self.MovieData:
            MovieCollection.fetch_moive_via_obj(movie) # space after funtions for readability
            
    def remove_movie(self):
        MovieCollection.view_movie(self)
        try:
            removeMovieNum = int(input("\nEnter Number of Movie to Remove : "))
            self.MovieData.pop(removeMovieNum-1)
        except:
            print("Error, Please Select Again.")
            self.remove_movie()
        
    def search_movie(self):
        user_input = input("\nEnter Movie Name To Search : ").lower()
        for movie in self.MovieData:
            if movie["Name"].lower() !=  user_input:
                continue
            print(f"\nMovie Found at Index {movie['Movie Number']}")
            MovieCollection.fetch_moive_via_obj(movie)
            return
        
        print("\nMovie Not Found...\nKindly check  View Movie Option for Manual Search.\n")
