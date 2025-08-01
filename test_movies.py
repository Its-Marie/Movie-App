from movie_storage_sql import add_movie, list_movies, delete_movie, update_movie

# Filme hinzufügen
add_movie("Inception", 2010, 8.8)
add_movie("Interstellar", 2014, 8.6)
add_movie("The Dark Knight", 2008, 9.0)

# Filme anzeigen
print("Movies after adding:")
print(list_movies())

# Bewertung aktualisieren
update_movie("Interstellar", 9.1)
print("Movies after updating:")
print(list_movies())

# Einen Film löschen
delete_movie("The Dark Knight")
print("Movies after deleting:")
print(list_movies())
