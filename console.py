import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

# album_repository.delete_all()
# artist_repository.delete_all()

artist1 = Artist("Jarvis", "Cocker")
artist_repository.save(artist1)

# artist2


pdb.set_trace()