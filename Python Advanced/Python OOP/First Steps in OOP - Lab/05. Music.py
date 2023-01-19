class Music():

    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics
 
///
import unittest

class Tests(unittest.TestCase):
    def test_initialization(self):
        music = Music("Whiplash", "Metallica", "Late at night, all systems go")
        self.assertEqual(music.title, "Whiplash")
        self.assertEqual(music.artist, "Metallica")
        self.assertEqual(music.lyrics, "Late at night, all systems go")

    def test_print_info(self):
        music = Music("Whiplash", "Metallica", "Late at night, all systems go")
        self.assertEqual(music.print_info(), 'This is "Whiplash" from "Metallica"')
        
        
    def test_play(self):
        music = Music("Whiplash", "Metallica", "Late at night, all systems go")
        self.assertEqual(music.play(), "Late at night, all systems go")
        
        
if __name__ == "__main__":
   unittest.main()
   
   
