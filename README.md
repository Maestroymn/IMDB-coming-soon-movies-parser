# IMDB-coming-soon-movies-parser
  The main purpose for this project is to parse all the information from the given IMDB link into an understandable and more clear way.
# "How to use the BeautifulSoup?"
__An example case:__
>>> u = urllib.request.urlopen(’https://www.imdb.com/movies-coming-soon/2019-04/’)

>>> x = u.read().decode(’UTF-8’)

>>> soup = BeautifulSoup(x,’html.parser’)

>>> f = open(’april_coming.txt’,’w’)

>>> f.write(soup.text)

>>> f.close()

  So to use the code with correct way you just need to go through www.imdb.com/movies-coming-soon/ and set your month to  get the data from (For example: you want to get the whole movie informations that will come within April then you just need to get the link of this site; "https://www.imdb.com/movies-coming-soon/2019-04/" and paste it into the line 5 in the code.) Also, don't forget to set the name of the txt file that you want to write the all data inside. (For example; in the given code you can see in line 8 the name of the file is set to "april_coming.txt") 
  
  You can work with several months. All you need to do is keep all the coming soon month data in different text files. So, you just need to copy and paste the first 6 line and change the links according to your purpose.
# Commands
  ___1) INPUT:___
  The main purpose of the command is to ensure that the specific month(s) that you will input with, will be parsed into a usable way. To use the "INPUT" command you need to make sure that you have created your coming soon movie month text file which is currently in unclear status. For example, let's assume that you have created your upcoming april month movies text file as "april_coming.txt". You will use the INPUT command like this: _INPUT april_coming.txt_ A sample run:
  
	INPUT data/april_coming.txt
	Loading data/april_coming.txt ...
	INPUT data/may_coming.txt
	Loading data/may_coming.txt ...
	
Again, you are free to INPUT several files into the code as long as there is such txt file containing souped IMDB movie site link.
 
 ___2) LIST:___
 The main purpose of this command is to list all the movie names of the month(s) that you inputted txt files with using INPUT command. A sample run:
 
 	LIST
	Listing ...
	Shazam!
	Pet Sematary
	The Best of Enemies
	...

 ___3) LIST from:YYYY-MM-DD:___
 The main purpose of this command is to list all the movie names that will come after that specific time that you specify within your input. A sample run:
	
	LIST from:2019-04-10
	Listing from:2019-04-10 ...
	Hellboy
	Missing Link
	...
	
 ___4) LIST from:YYYY-MM-DD: to:YYYY-MM-DD___
	 The main purpose of this command is to list all the movie names that within the dates that you specify within your input. A sample run: 
	 
	LIST from:2019-04-05 to:2019-04-10
	Listing from:2019-04-10 to:2019-04-10 ...
	Shazam!
	Pet Sematary
	The Best of Enemies
	Peterloo
	The Biggest Little Farm
	Teen Spirit
 ___5) LIST genre:genrename___
 	The main purpose of this command is to list the movies that includes the genres that you specify withing your input. A sample run: 
	
	LIST genre:Action,Sci-Fi
	Listing genre:Action,Sci-Fi ...
	Shazam!
	Hellboy
	...
 
 ___6) INFO moviename___
 	The main purpose of this command is to list all the detailed information(production year, release date, genre, synopsis, director(s) and star(s)) about the movie that you specify within your input. A sample run:
	
	INFO Shazam!
	Info ...
	Shazam!
	Production year: 2019
	Release date: 2019-04-05
	Genre: Action, Advanture, Fantasy, Sci-Fi
	Synopsis: We all have a superhero inside us, it just takes a bit of magic to
	bring it out. In Billy Batson’s case, by shouting out one word - SHAZAM! - this
	streetwise 14-year-old foster kid can turn into the adult superhero Shazam.
	Director: David F. Sandberg
	Stars: Zachary Levi, Mark Strong, Djimon Hounsou, Michelle Borth


