from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album
  
  
def select_all():  
    albums = [] 

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['title'], row['genre'], artist, row['id'] )
        albums.append(album)
    return albums
    

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"  
    values = [id] 
    result = run_sql(sql, values)[0]
    
    if result is not None:
        artist = artist_repository.select(row['artist_id'])    
        album = Album(result['title'], result ['genre'], artist, result['artist_id])
    return album


# def delete_all():
#     sql = "DELETE  FROM tasks" 
#     run_sql(sql)

# def delete(id):
#     sql = "DELETE  FROM tasks WHERE id = %s" 
#     values = [id]
#     run_sql(sql, values)


# def update(task):
#     sql = "UPDATE tasks SET (description, user_id, duration, completed) = (%s, %s, %s, %s) WHERE id = %s"
#     values = [task.description, task.user_id, task.duration, task.completed, task.id]
#     run_sql(sql, values) 
    
def artist(album):
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [album.artist_id]
    result = run_sql(sql, values) [0]

    return Artist(result['first_name'], result['last_name'], result['id'])