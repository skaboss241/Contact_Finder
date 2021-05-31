import requests
from imdb import IMDb

Credits = []

try:
    #search imdb for the movie id. For Star Wars, 0076759. Look to the url: it's https://www.imdb.com/title/tt0076759/
    def movie_search():
        ia = IMDb()
        Movie_Title = input("Input the IMDb ID: ").upper()
        Movie = ia.get_movie(Movie_Title)
        print('You chose ' + str(Movie['title']))
        Choice = input("Do you want to cross-reference just the CAST or EVERYONE in the credits? ").upper()

        if Choice == "CAST":
            print('generating cast database...')
            ia.update(Movie, 'full credits')
            for x in Movie['cast']:
                Credits.append(x['name'].upper())

        if Choice == "EVERYONE":
            print('generating database for everyone...')
            ia.update(Movie, 'full credits')
        for x in (sorted(Movie.keys())):
            if type(Movie[x]) == list:
                if len(Movie[x][0]) < 30:
                    for y in Movie[x]:
                        if type(y) != str:
                            Credits.append(y['name'].upper())


    # searches a given link for artists that you specify in the names list.
    def search():
        # user will input a URL for a convention's guests page or artist page or wherever they have their 
        # attendees listed.
        Site = input(
            [r'Please enter the site you would like to search i.e. https://iccollectorsconvention.com/artists/'])
        # This is where you list which guests you are looking for.
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/72.0.3626.119 Safari/537.36"}

        print('searching page for artists')
        counter = 0
        page = requests.get(Site, headers=headers)
        for y in Credits:
            if str(y) in page.text.upper():
                print(str(y))
                counter = counter + 1
        if counter <= 0:
            print('no matches')


    while True:
        movie_search()
        search()

except Exception as e:
    print("type error: " + str(e))
    pass
