def musicAlbum(musician, album_name, count_of_tracks = None):
    albumAndMusician = {'name_of_musician': musician.title(), 'album_name': album_name.title()}
    if count_of_tracks:
        albumAndMusician['countOfTracks'] = count_of_tracks
    return albumAndMusician

count = 3

while count >= 0:
    if count != 0:
        name = input("get name of musician: ")
        album = input("get name of album: ")
        print(musicAlbum(name, album))
    else:
        name = input("get name of musician: ")
        album = input("get name of album: ")
        count_of_tracks = int(input('count of tracks: '))
        print(musicAlbum(name, album, count_of_tracks))
    count -= 1





