import webbrowser

class Movie():
    """This class is used to define any movie and its various attributes.
    """
    def __init__(self, a_title,a_storyline,a_poster_image_url,a_trailer_youtube_url):
        self.title = a_title
        self.storyline = a_storyline
        self.poster_image_url = a_poster_image_url
        self.trailer_youtube_url = a_trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


