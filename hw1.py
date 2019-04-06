import re
import datetime

#Following 6 line simply for the purpose of getting the whole IMDB website link into a text file to parse it later on
u = urllib.request.urlopen('https://www.imdb.com/movies-coming-soon/2019-04/') #You need to put specific month of the upcoming movies to get the info's
x = u.read().decode('UTF-8')
soup = BeautifulSoup(x,'html.parser')
f = open('april_coming.txt','w') #this line will create a new txt file and write all the given link infos inside the text file
f.write(soup.text)
f.close()

# Basic object to hold every movie in it
class movie:
    def __init__(Movie, movieName, year, releaseDate, genre, synopsis, director, stars):
        Movie.movieName = movieName
        Movie.year = year
        Movie.releaseDate = releaseDate
        Movie.genre = genre
        Movie.synopsis = synopsis
        Movie.director = director
        Movie.stars = stars

    # movieInfo function is basically for printing all the info for the movie
    def movieInfo(self):
        commaCounter = self.director.count(',')
        print(self.movieName, '\nProduction year:', self.year, '\nRelease date:', self.releaseDate, '\nGenre:',
              self.genre[:-2], '\nSynopsis:', self.synopsis)
        if commaCounter == 1:
            print('Director:', self.director[:-2], '\nStars:', end=' ')
            if 'Empty' in self.stars:
                print('')
            else:
                print(self.stars)
        elif commaCounter > 1:
            print('Directors:', self.director[:-2], '\nStars:', end=' ')
            if 'Empty' in self.stars:
                print('')
            else:
                print(self.stars)


pass


# date_Converter function is for converting release dates which are in string form into a date object with using datetime package(which is recommended in the homework's PDF folder as a hint)
def date_Converter(datetext):
    dateSplitted = datetext.split()
    if dateSplitted[0] == 'January':
        time = datetime.date(2019, 1, int(dateSplitted[1]))
        return time
    elif dateSplitted[0] == 'February':
        time = datetime.date(2019, 2, int(dateSplitted[1]))
        return time
    elif dateSplitted[0] == 'March':
        time = datetime.date(2019, 3, int(dateSplitted[1]))
        return time
    elif dateSplitted[0] == 'April':
        time = datetime.date(2019, 4, int(dateSplitted[1]))
        return time
    elif dateSplitted[0] == 'May':
        time = datetime.date(2019, 5, int(dateSplitted[1]))
        return time
    elif dateSplitted[0] == 'June':
        time = datetime.date(2019, 6, int(dateSplitted[1]))
        return time
    elif dateSplitted[0] == 'July':
        time = datetime.date(2019, 7, int(dateSplitted[1]))
        return time
    elif dateSplitted[0] == 'August':
        time = datetime.date(2019, 8, int(dateSplitted[1]))
        return time
    elif dateSplitted[0] == 'September':
        time = datetime.date(2019, 9, int(dateSplitted[1]))
        return time
    elif dateSplitted[0] == 'October':
        time = datetime.date(2019, 10, int(dateSplitted[1]))
        return time
    elif dateSplitted[0] == 'November':
        time = datetime.date(2019, 11, int(dateSplitted[1]))
        return time
    elif dateSplitted[0] == 'December':
        time = datetime.date(2019, 12, int(dateSplitted[1]))
        return time


if __name__ == '__main__':
    text = []
    synopsisList = []
    directorList = []
    starList = []
    genreList = []
    yearsList = []
    mainDateList = []
    mainGenreList = []
    mainDirectorList = []
    mainStarList = []
    MovieList = []
    start = False
    direcBool = False
    starBool = False
    dateBool = False
    while True:
        heyo = []
        dateList = []
        action = input('What do you want to do?')
        inputs = action.split()
        if inputs[0] == 'INPUT':
            print('Loading', inputs[1], '...')
            fr = open(inputs[1], "r")
            data = fr.read()

            for line in data.splitlines():  # This loop is basically decomposing the lines from unnecesary ones(like: if statements and etc.) to reach movie data except synopsis info of the movies
                if line.strip().istitle():
                    heyo.append(line.strip())
                elif re.match(r'.*\(\d{4}\)', line) and '.' not in line:
                    heyo.append(line.strip())

            for each in heyo:  # This loop is searching for the lines which contains release dates of the movies and adding them into a list
                if re.match(r'[A-Z][a-z]*\s\d{1,2}', each):
                    date = re.match(r'[A-Z][a-z]*\s\d{1,2}', each)
                    if re.match(r'.*\s\(\d{4}\)', each):
                        dateList.append(date.string)
                else:
                    if re.match(r'.*\s\(\d{4}\)', each):
                        dateList.append(date.string)

            for eachDate in dateList:  # This loop is converting each string date into a datetime object and adding them into a list
                mainDateList.append(date_Converter(eachDate))

            for eachLine in heyo:  # This loop is searching for the director(s) in the data and adding them into a list
                if re.match(r'Director:', eachLine) or re.match(r'Directors:', eachLine):
                    direcBool = True
                    continue
                elif re.match('Stars:', eachLine) or re.match('Watch Trailer', eachLine):
                    directorList.append('//')
                    direcBool = False
                elif re.match(r'[A-Z][a-z]*\s\d', eachLine) and direcBool:
                    directorList.append('//')
                    direcBool = False
                    continue
                if direcBool:
                    directorList.append(eachLine)

            emptyChecker = False
            movieStart = False
            insertStars = False

            for eachLine in heyo:  # This loop is searching for the stars in the data if there are no stars for a movie then it adds 'Empty', if there are data for stars for a movie then it adds them into a list
                if movieStart is False and re.match(r'.+\s\(\d{4}\)', eachLine):
                    movieStart = True
                    insertStars = False
                elif re.match('Stars:', eachLine):
                    insertStars = True
                    continue
                elif movieStart is True and insertStars is False and (re.match('Watch Trailer', eachLine) or re.match(r'[A-Z][a-z]+\s\d{1,2}', eachLine) or re.match(r'.+\s\(\d{4}\)', eachLine)):
                    starList.append('Empty/')
                    insertStars = False
                    movieStart = False
                elif movieStart is True and insertStars is True and re.match(r'.+\s\(\d{4}\)', eachLine):
                    movieStart = True
                    insertStars = False
                    starList.append('/')
                elif insertStars and (
                        re.match(r'.+\s\(\d{4}\)', eachLine) or re.match(r'[A-Z][a-z]+\s\d{1,2}', eachLine)
                        or re.match('Watch Trailer', eachLine)):
                    insertStars = False
                    movieStart = False
                    starList.append('/')
                if insertStars:
                    starList.append(eachLine)

            for eachLine in heyo: # This loop is searching for genre data for each movie and adds them into a list
                if re.match(r'.*\s\(\d{4}\)', eachLine):
                    start = True
                    continue
                elif re.match(r'Director:', eachLine) or re.match(r'Directors:', eachLine):
                    genreList.append('/')
                    start = False
                if start:
                    genreList.append(eachLine)

            lines = data.strip().splitlines()

            for info in lines: # This loop is searching for movie names and synopsis data for each movie and adding them into a list
                movieName = re.match(r'\s\S.*\s\(\d{4}\)', info)
                synopsis = re.match(r'\s\s\s\s.?[A-Z].*.\Z', info)
                numericSynopsis = re.match(r'\s\s\s\s\d{1,2}.*.\Z', info)
                if movieName:
                    text.append(movieName.string[1:-7])
                    yearsList.append(movieName.string[-5:-1])
                if numericSynopsis:
                    synopsisList.append(numericSynopsis.string.strip())
                if synopsis:
                    if 'Coming Soon' not in synopsis.string:
                        synopsisList.append(synopsis.string.strip())

            directors = ''
            stars = ''
            genres = ''

            for e in genreList: # This loop is basically converting the genres list into a string to work on them more easily
                if '/' in e:
                    genres = genres + '\n'
                else:
                    genres = genres + e + ', '

            genres = genres.replace('Metascore,', ' ') # Decomposing some unnecesary things which may occur in our data
            mainGenreList = genres.splitlines()

            for d in starList: # This loop is basically converting the stars list into a string to work on them more easily
                if '/' in d:
                    stars = stars + '\n'
                else:
                    stars = stars + d
            stars = stars.replace(',', ', ')
            mainStarList = stars.splitlines()

            for c in directorList: # This loop is basically converting the directors list into a string to work on them more easily
                directors = directors + c + ', '

            # These all replacements are shaping the directors string into a meaningful one with using the markings('//') that I putted into the list
            directors = directors.replace('//, //, //, //, //, //,', '')
            directors = directors.replace('//, //, //, //,', '\n-\n')
            directors = directors.replace('//, //, //,', '\n')
            directors = directors.replace('//, //,', '\n')
            directors = directors.replace('//,', '\n')
            mainDirectorList = directors.splitlines()
            del mainDirectorList[-1] # An empty element occurs at the end of the list it removes it to prevent bugs

            for index in range(len(text)): # This loop is creating new movie object with all decomped data and adds the objects into a list
                newMovie = movie(text[index], yearsList[index], mainDateList[index], mainGenreList[index],
                                 synopsisList[index], mainDirectorList[index], mainStarList[index])
                MovieList.append(newMovie)
            MovieList.sort()
        elif action == 'LIST':
            print('Listing...')
            for movies in text: # This loop is listing the movie names which is currently in data
                print(movies)
        elif re.match(r'.+to:\d{4}.\d{2}.\d{2}', action):
            print('Listing from', inputs[1], inputs[2], '...')
            listedMovies = [] # A list to add movie names into it
            month = inputs[1][10:-3]
            day = inputs[1][13:]
            startingDate = datetime.date(2019, int(month), int(day)) # creating start date object for searching data
            month = inputs[2][8:-3]
            day = inputs[2][11:]
            endDate = datetime.date(2019, int(month), int(day)) # creating end date object for searching data
            for index in MovieList:
                if startingDate <= index.releaseDate <= endDate:
                    listedMovies.append(index.movieName)
            if len(listedMovies)==0:
                print('No such movie found on the data.')
            else:
                listedMovies = list(dict.fromkeys(listedMovies)) # This line basically removes duplicates from the list to prevent bugs
            for each in listedMovies: # Listing the names of the movies which is on the range of the given dates
                print(each)
        elif re.match(r'.+from:\d{4}.\d{2}.\d{2}', action):
            print("Listing", inputs[1], '...')
            month = inputs[1][10:-3]
            day = inputs[1][13:]
            startingDate = datetime.date(2019, int(month), int(day)) # creating start date object for searching data
            listedMovies = [] # A list to add movie names into it
            for index in MovieList:
                if index.releaseDate >= startingDate:
                    listedMovies.append(index.movieName)
            if len(listedMovies) == 0:
                print('No such movie found on the data.')
            else:
                listedMovies = list(dict.fromkeys(listedMovies)) # This line basically removes duplicates from the list to prevent bugs
            for each in listedMovies: # Listing the names of the movies which is on the range of the given dates
                print(each)
        elif re.match(r'genre:.+', inputs[1]):
            print('Listing', inputs[1], '...')
            genre = inputs[1][6:]
            genre = genre.replace(',', ', ')
            listedMovies = [] # A list to add movie names into it
            for index in MovieList:
                for each in genre.split(', '): # splitting the given genres to search for into solo elements to search them properly
                    if each in index.genre:
                        listedMovies.append(index.movieName)
            if len(listedMovies) == 0:
                print('No such movie found on the data with that genre.')
            else:
                listedMovies = list(dict.fromkeys(listedMovies)) # This line basically removes duplicates from the list to prevent bugs
            for each in listedMovies: # Listing the names of the movies which is on the range of the given dates
                print(each)
        elif re.match(r'INFO.+', action):
            print('Info ...')
            moviename = re.match(r'INFO.+', action)
            moviename = moviename.string[5:] # Substring's only the movie name from the input
            for index in MovieList:
                if moviename in index.movieName:
                    index.movieInfo() # Listing the detailed info of the movie that the user is searching for
    fr.close()
