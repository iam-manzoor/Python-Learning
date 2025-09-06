# Program to take the user 3 favorite movie and store it in the list.

# Method-1
favoriteMovie = []
count = 0

while count < 3:
  movie = input("Enter the movie name :")
  favoriteMovie.append(movie)
  count += 1

print(My favorite movies are : ", favoriteMovie)

# Method-2

favoritMovies = input("Enter the movie names with comma seperated :").split(',') # movie1.movie2,movie3
print(favoriteMovies)

# Method-3

movies = []
movies.append(input("Enter 1st movie : "))
movies.append(input("Enter 2nd movie : "))
movies.append(input("Enter 3rd movie : "))

print(movies)
