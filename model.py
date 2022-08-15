from codecs import namereplace_errors


class Movie:
    def __init__(self, name, year, length):
        self.name = name
        self.year = year
        self.length = length

class Series:
    def __init__(self, name, year, seasons):
        self.name = name
        self.year = year
        self.seasons = seasons 
    


avengers = Movie("Avengers - Infinity War", 2018, 160)
print(f'Name: {avengers.name} - Year: {avengers.year} - Length (minutes): {avengers.length}')

atlanta = Series('Atlanta', 2018, 2)

print(f'Name: {atlanta.name} - Year: {atlanta.year} - Seasons: {atlanta.seasons}')