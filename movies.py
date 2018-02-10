# Get user input for movies

def GetMovieNames():

    valid_iput = False
    while not valid_iput:

        try:
            movie1 = str(raw_input('What is the name of movie 1: '))
            movie2 = str(raw_input('What is the name of movie 2: '))
            print ''

            if movie1.isalnum() and movie2.isalnum():
                valid_iput = True
                return (movie1, movie2)
            else:
                raise Exception()
            
        except Exception as e:
            print 'The movies must be string'
            print ''

def FindActors():

    # Open the file
    file = open('movies.csv', 'r')

    # Get the user's input
    movie1, movie2 = GetMovieNames()

    # Create an empty dictionary to hold the actors names and movie titles
    filmography = []

    # Loop through each line and extract the actor and movies
    for line in file.readlines():

        # Strip the line endings
        clean_line = line.rstrip()

        # Split the line in a list
        words = clean_line.split(',')

        # The first index is the actor's name
        actor_name = words[0]

        # Add the actor and their roles to a Tuple
        actor_roles = (actor_name, words[1:])
        filmography.append(actor_roles)

    first_movie = set()
    second_movie = set()

    for actor in filmography:
        if movie1 in actor[1]:
            first_movie.add(actor[0])
        if movie2 in actor[1]:
            second_movie.add(actor[0])

    both_movies = first_movie.intersection(second_movie)
    first_only = first_movie.difference(second_movie)
    second_only = second_movie.difference(first_movie)

    print 'Actors in {} and {}: {}'.format(movie1, movie2, ', '.join(both_movies))
    print 'Actors only in the {}: {}'.format(movie1, ', '.join(first_only))
    print 'Actors only in the {}: {}'.format(movie2, ', '.join(second_only))
