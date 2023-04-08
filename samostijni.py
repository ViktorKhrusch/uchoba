def make_album(musician, album_name, num_song=None):
    album_info = {'mus': musician, 'a_name': album_name}
    if num_song:
        album_info = {'mus': musician, 'a_name': album_name, 'song': num_song}
    return album_info

full_info = make_album('ramstein', 'fire', num_song=25)
print(full_info)
