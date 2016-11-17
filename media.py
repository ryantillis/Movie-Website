import webbrowser

class Movie():
    
    def __init__(self, movie_title, storyline, poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        
    def show_trailer():
        webbrowser.open(self.trailer_youtube_url)
        
        
#class Tv():
#    def _init_(self,tv_title,tv_storyline,poster_image,trailor_youtube):
        
