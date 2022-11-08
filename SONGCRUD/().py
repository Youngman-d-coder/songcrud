# coding: utf-8
from musicapp.models import Artiste, Song, Lyric
artist_1 = Artiste.objects.create(first_name="asake",last_name="ololademi",age=28)
song_1 = Song.objects.create(title="ototo", date_released=27/11/2021, artiste_id="artist_1")
song_1 = Song.objects.create(title="ototo", date_released=27/11/2021, artiste_id=artist_id)
song_1 = Song.objects.create(title="ototo", date_released=27/11/2021, artiste_id="Artiste")
song_1 = Song.objects.create(title="ototo", date_released=27/11/2021, artiste_id="Song.artiste_id")
song_1 = Song.objects.create(title="ototo", date_released=27/11/2021)
song_1 = Song.objects.create(title="ototo", date_released=datetime.today)
import datetime
song_1 = Song.objects.create(title="ototo", date_released=datetime.today)
from datetime import datetime
song_1 = Song.objects.create(title="ototo", date_released=datetime.today)
song_1 = Song.objects.create(title="ototo", date_released="datetime.today")
song_1 = Song.objects.create(title="ototo", date_released="2021-11-27")
song_1 = Song.objects.create(title="ototo", date_released="2021-11-27", artiste_id="full_name")
song_1 = Song.objects.create(title="ototo", date_released="2021-11-27", artiste_id=artist_1)
lyric_1 = Lyric.objects.create(content="carry your load i no get stamina", song_id=song_1)
