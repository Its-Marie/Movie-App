import random
import statistics
import requests
import movie_storage_sql as storage
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def list_movies():
    """
    Prints the total number of movies and details for each movie.
    Fetches movies from the storage and displays them with their rating and release year.
    """
    movies = storage.list_movies()

    count_movies = len(movies)
    print(f"{count_movies} movies in total")
    for title, info in movies.items():
        print(f"{title}: Rating {info['rating']}, Year {info['year']}")


def add_movie():
    """
    Adds a new movie by fetching data from the OMDb API.
    The user only enters the movie title, and the program retrieves title, year, rating, and poster URL.
    Handles errors for movies not found or API connection issues.
    """
    movies = storage.list_movies()
    new_movie = input("Please enter movie name: ")

    if any(title.lower() == new_movie.lower() for title in movies.keys()):
        print(f"Movie '{new_movie}' is already in the database.")
        return

    try:
        response = requests.get(
            f"http://www.omdbapi.com/?t={new_movie}&apikey={API_KEY}"
        )
        if response.status_code != 200:
            print("Error: OMDb API is not reachable.")
            return

        data = response.json()
        if data.get("Response") == "False":
            print(f"Movie '{new_movie}' was not found.")
            return

        title = data.get("Title")
        year = int(data.get("Year", 0))
        rating = float(data.get("imdbRating", 0)) if data.get("imdbRating") != "N/A" else 0
        poster = data.get("Poster", "N/A")

        storage.add_movie(title, year, rating, poster)
        print(f"New movie added: {title}, Rating: {rating}, Year: {year}, Poster: {poster}")

    except requests.exceptions.RequestException:
        print("Error: Cannot connect to OMDb API. Please check your internet connection.")


def delete_movie():
    """
    Deletes a movie from the database if it exists.
    Asks the user for the movie title and removes it from storage.
    """
    movies = storage.list_movies()
    name = input("What movie should be deleted? ")

    if name in movies:
        storage.delete_movie(name)
        print(f"Movie '{name}' has been deleted.")
    else:
        print(f"Movie '{name}' not found.")


def update_movie():
    """
    Updates the rating of an existing movie in the database.
    Asks for the movie title and a new rating between 1-10.
    """
    movies = storage.list_movies()
    movie_name = input("Please enter movie name: ")

    if movie_name in movies:
        try:
            new_rating = float(input("Please enter your rating between 1-10: "))
            if 1 <= new_rating <= 10:
                storage.update_movie(movie_name, new_rating)
                print(f"Movie rating updated: {movie_name}: {new_rating}")
            else:
                print("Rating must be between 1 and 10.")
        except ValueError:
            print("Invalid input. Rating must be a number.")
    else:
        print("Movie not found.")


def show_statistics():
    """
    Displays average, median, best, and worst-rated movies.
    Uses statistical functions to analyze movie ratings.
    """
    movies = storage.list_movies()

    if not movies:
        print("No movies in database.")
        return

    ratings = [info["rating"] for info in movies.values()]

    # Average rating
    average_rating = statistics.mean(ratings)
    print(f"Average rating: {average_rating}")

    # Median rating
    median = statistics.median(ratings)
    print(f"Median rating: {median}")

    # Best movie(s)
    max_rating = max(ratings)
    best_movies = [title for title, info in movies.items() if info["rating"] == max_rating]
    print(f"Best movie(s) (rating {max_rating}):")
    for movie in best_movies:
        print(movie)

    # Worst movie(s)
    min_rating = min(ratings)
    worst_movies = [title for title, info in movies.items() if info["rating"] == min_rating]
    print(f"Worst movie(s) (rating {min_rating}):")
    for movie in worst_movies:
        print(movie)


def random_movie():
    """
    Selects and displays a random movie from the database.
    """
    movies = storage.list_movies()

    if not movies:
        print("No movies in database.")
        return

    random_title = random.choice(list(movies.keys()))
    random_info = movies[random_title]
    print(
        f"Random movie: {random_title}, "
        f"Rating: {random_info['rating']}, "
        f"Year: {random_info['year']}"
    )


def search_movie():
    """
    Searches for movies containing a user-provided substring.
    Displays all matching movies.
    """
    movies = storage.list_movies()

    if not movies:
        print("No movies in database.")
        return

    search_term = input("Enter part of movie name: ").lower()
    found_movies = [(title, info) for title, info in movies.items() if search_term in title.lower()]

    if found_movies:
        print()
        for title, info in found_movies:
            print(f"{title}, Rating: {info['rating']}, Year: {info['year']}")
    else:
        print("No movies found matching your search.")


def movies_sorted_by_rating():
    """
    Displays all movies sorted by rating from highest to lowest .
    """
    movies = storage.list_movies()

    if not movies:
        print("No movies in database.")
        return

    sorted_movies = sorted(movies.items(), key=lambda x: x[1]['rating'], reverse=True)
    print("\nMovies sorted by rating (best to worst):")
    for title, info in sorted_movies:
        print(f"{title}, Rating: {info['rating']}, Year: {info['year']}")


def generate_website():
    """
    Generate an HTML file by filling a template with movie data.
    Writes the completed page to index.html.
    """

    movies = storage.list_movies()

    with open("_static/index_template.html", "r", encoding="utf-8") as f:
        template = f.read()

    website_title = "My Movie App"

    start = template.find("<li>")
    end = template.find("</li>") + len("</li>")
    movie_item_template = template[start:end]

    movie_items = ""
    for title, info in movies.items():
        item = movie_item_template
        item = item.replace("__POSTER__", info["poster"])
        item = item.replace("__TITLE__", title)
        item = item.replace("__YEAR__", str(info["year"]))
        item = item.replace("__RATING__", str(info["rating"]))
        movie_items += item

    html_content = template.replace(template[start:end], movie_items)
    html_content = html_content.replace("__TEMPLATE_TITLE__", website_title)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("Website was generated successfully.")


def main():
    """Main menu loop for the Movie Database application."""
    while True:
        print()
        print("--- Movie Database Menu ---")
        print("0. Exit")
        print("1. List all movies")
        print("2. Add a movie")
        print("3. Delete a movie")
        print("4. Update movie rating")
        print("5. Show statistics")
        print("6. Random movie")
        print("7. Search movie")
        print("8. Movies sorted by rating")
        print("9. Generate website")

        print()

        choice = input("Choose an option (0-9): ")
        print()

        if choice == "0":
            print("Bye!")
            break
        elif choice == "1":
            list_movies()
        elif choice == "2":
            add_movie()
        elif choice == "3":
            delete_movie()
        elif choice == "4":
            update_movie()
        elif choice == "5":
            show_statistics()
        elif choice == "6":
            random_movie()
        elif choice == "7":
            search_movie()
        elif choice == "8":
            movies_sorted_by_rating()
        elif choice == "9":
            generate_website()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
