from project.song import Song

class Album():
    def __init__(self, name: str, *songs):
        self.name = name
        self.published = False
        self.song = [x for x in songs]


    def add_song(self, song: Song):

        if self.published:
            return f"Cannot add songs. Album is published."
        elif song.single:
            return f"Cannot add {song.name}. It's a single"

        if song.name not in [x.name for x in self.song]:
            self.song.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

        return f"Song is already in the album."

    def remove_song(self, song_name: str):

        if song_name not in [x.name for x in self.song]:
            return "Song is not in the album."
        elif self.published:
            return f"Cannot remove songs. Album is published."

        for show in self.song:
            if show.name == song_name:
                del show
                return f"Removed song {song_name} from album {self.name}."

    def publish(self):

        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        text = [f"Album {self.name}"]
        for song in self.song:
            text.append(f"== {song}")
        return "\n".join(text)

