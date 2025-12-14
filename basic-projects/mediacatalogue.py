class Movie:
    def __init__(self, title, year, director, duration):
        if title == "" or title.strip() == "": 
            raise ValueError("Title cannot be empty")
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration
    def __str__(self):
        return f'{self.title} ({self.year}) - {self.duration} min, {self.director}'

movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
try:
    movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
except ValueError as e:
    print(f"Validation Error: {e}")
    
class MediaCatalogue:
    def __init__(self):
        self.items = []
        
    def add(self, media_item):
        self.items.append(media_item)
        
    def __str__(self):
        if not self.items:
            return ("Media Catalogue (empty)")