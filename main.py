import random
import datetime
from faker import Faker
fake = Faker()

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
    
    def count_episodes(self):
        '''
        Counts no of episodes of provided series.
        '''
        filter_series = [x for x in Film.instances if x.title == self.title]
        return len(filter_series)

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

def top_titles(how_many, type):
    '''
    Returns movies with most views.

	Parameters:
		how_many (int): number of the most viewd movies to be presented on the final list
		type (int): 1 - films only, 2 - series only, 3 - all types of movies

	Returns:
		by_views (list): movies with most views according to set parameters
    '''
    if type == 1:
        filter_movies = [x for x in Film.instances if not isinstance(x, Series)]
        by_views = sorted(filter_movies, key=lambda movie: movie.plays, reverse=True)
        return by_views[0:how_many]
    
    if type == 2:
        filter_series = [x for x in Film.instances if isinstance(x, Series)]
        by_views = sorted(filter_series, key=lambda movie: movie.plays, reverse=True)
        return by_views[0:how_many]

    if type ==3:
        by_views = sorted(Film.instances, key=lambda movie: movie.plays, reverse=True)
        return by_views[0:how_many]
    
    else:
        return "Wrong type: 1 - films only, 2 - series only, 3 - all types of movies"

def add_full_season(series_title, year_aired, genre, season_no, how_many_episodes):
    list = []
    for i in range(1,how_many_episodes+1):
        list.append(i)
        list[i-1] = Series(i, season_no, series_title, year_aired, genre, 0)

if __name__ == "__main__":
    print("Biblioteka filmów")
    list_of_films = []
    for i in range(1,11):
        list_of_films.append(i)
        list_of_films[i-1] = Film(fake.word(), random.randint(1955, 2023), fake.word(), 0)
    add_full_season(fake.word(), random.randint(1955, 2023), fake.word(), random.randint(1, 10), random.randint(1, 20))
    add_full_season(fake.word(), random.randint(1955, 2023), fake.word(), random.randint(1, 10), random.randint(1, 20))
    for i in range(30):
        generate_views_x10()
    now = datetime.datetime.now()
    print("Najpopularniejsze filmy i seriale dnia", now.strftime("%d-%m-%Y"))
    print(top_titles(3,3))

