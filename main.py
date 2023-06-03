import random

class Film:
    instances = []
    titles = []
    def __init__(self, title, year, genre, plays):
        self.title = title
        self.year = year
        self.genre = genre
        self.plays = plays
        self.__class__.instances.append(self)
        self.__class__.titles.append(self.title)
    
    def __repr__(self):
        return f'{self.title} ({self.year})'
    
    def play(self, step=1):
        self.plays += step

class Series(Film):
    def __init__(self, episode_no, season_no, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_no = episode_no
        self.season_no = season_no
    def __repr__(self):
        return f'{self.title} S{"{:02d}".format(self.season_no)}E{"{:02d}".format(self.episode_no)}' 

F1 = Film('title', '1555', 'genre', 1)
F2 = Film('atitle2', '15552', 'genre2', 1)
S1 = Series(2, 4, 'titles', '1444', 'genres', 1,)
S2 = Series(14, 101, 'atitles2', '14442', 'genres2', 1,)

def get_movies():
    filter_movies = [x for x in Film.instances if not isinstance(x, Series)]
    by_name = sorted(filter_movies, key=lambda movie: movie.title)
    return by_name

def get_series():
    filter_series = [x for x in Film.instances if isinstance(x, Series)]
    by_name = sorted(filter_series, key=lambda movie: movie.title)
    return by_name

def search(query):
    found = False
    for movie in Film.titles:
        if query in str(movie):
            found = True
            print(str(movie))
    if not found:
        print(f"{query} not found in the list")
        
def generate_views():
    random.choice(Film.instances).play(random.randint(1,100))

def generate_views_x10():
    for i in range(10):
        generate_views()

def top_titles():
    by_views = sorted(Film.instances, key=lambda movie: movie.plays)
    return by_views

generate_views_x10()
#S1.play(10)
#print(Film.titles)
print(S1.plays)
print(S2.plays)
print(F1.plays)
print(F2.plays)

print(top_titles())


"""
    Napisz funkcję top_titles(), która zwróci wybraną ilość najpopularniejszych tytułów z biblioteki. 
    Dla chętnych: dodaj do funkcji parametr content_type, którym wybierzesz czy mają zostać pokazane filmy, czy seriale.

"""