# Movie Database App

A comprehensive Python command-line application for managing your personal movie collection with automatic data fetching from OMDb API and website generation capabilities.

## Features

- **Add Movies**: Automatically fetch movie data (title, year, rating, poster) from OMDb API
- **Movie Management**: List, delete, and update movie ratings
- **Smart Search**: Find movies by partial title matching
- **Statistics**: View average ratings, median, best and worst movies
- **Random Picker**: Get a random movie suggestion
- **Sorting**: Display movies sorted by rating
- **Website Generation**: Create a beautiful HTML website from your movie collection
- **SQL Storage**: Persistent data storage with SQLAlchemy

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Its-Marie/Movie-App.git
   cd Movie-App
   ```

2. **Install dependencies**
   ```bash
   pip install requests python-dotenv sqlalchemy
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```
   API_KEY=your_omdb_api_key_here
   ```
   Get your free API key from [OMDb API](http://www.omdbapi.com/apikey.aspx)

## Usage

Run the application:
```bash
python movies.py
```

### Menu Options:
- **0**: Exit
- **1**: List all movies
- **2**: Add a movie (fetches data automatically)
- **3**: Delete a movie
- **4**: Update movie rating
- **5**: Show statistics
- **6**: Get random movie suggestion
- **7**: Search movies
- **8**: Movies sorted by rating
- **9**: Generate website

## 🏗Project Structure

```
Movie-App/
├── movies.py              # Main application
├── movie_storage_sql.py   # Database operations
├── test_movies.py         # Test suite
├── _static/               # Static files for website
│   ├── index_template.html
│   └── style.css
├── .env                   # Environment variables
├── .gitignore
└── README.md
```

## Technical Details

- **Language**: Python 3.x
- **Database**: SQLAlchemy ORM
- **API**: OMDb API for movie data
- **Web Generation**: HTML templating system
- **Environment**: python-dotenv for configuration

## Statistics Features

The app provides comprehensive movie analytics:
- Average rating across all movies
- Median rating calculation
- Best rated movies identification
- Worst rated movies tracking

## Website Generation

Generate a static HTML website showcasing your movie collection:
- Responsive design with poster images
- Movie ratings and release years
- Automatic template processing
- Ready-to-deploy HTML output

## Error Handling

- API connection error management
- Duplicate movie prevention
- Input validation for ratings (1-10 scale)
- Graceful handling of missing movie data

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- [OMDb API](http://www.omdbapi.com/) for providing movie data
- SQLAlchemy for database management
- All contributors and users of this project

---

⭐ **Star this repo if you found it helpful!**
