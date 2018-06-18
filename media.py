import webbrowser

class Movie():

    """
    Movie class
    
    Attributes:
        title (str): Movie title.
        storyline (str): Movie story line
        poster_image_url (str): Link to the movie poster image
        trailer_youtube_url (str): Link to the youtube page for trailer

    """

    #Movie constructor. Set movie title, storyline, image url and trailer url
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    #Method to play movie trailer using movie trailer url
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
