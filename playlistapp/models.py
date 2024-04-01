"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    # ADD THE NECESSARY CODE HERE
    __tablename__='playlists'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(120), nullable=False)
    songs=db.relationship('Song', secondary='playlist_songs', back_populates='playlists')



class Song(db.Model):
    """Song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__='songs'
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String, nullable=False)
    artist=db.Column(db.String, nullable=False)
    playlists=db.relationship('Playlist', secondary='playlist_songs', back_populates='songs')


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__='playlist_songs'
    song_id=db.Column(db.Integer, db.ForeignKey('songs.id'), primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'), primary_key=True)



# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
