#8-6
from chapter_05.exercises.if_boolen import artist


def city_country(name, country):
    print(f'{name.title()}, {country.title}')

city_country('Nayeon', 'South Korea')
city_country('Jame, s', 'Iceland')
city_country('Pedro', 'Brazil')

print("---------------")
#8-7

def make_album(artist, album, songs=None):
    dictionary = {'Artist': artist.title(), 'Album': album.title(), 'Songs': songs}
    if songs:
        dictionary['songs'] = songs
    return dictionary

album1 = make_album('Weyes Blood', 'Sunflower')
print(album1)
albums2 = make_album('Weyes Blood', 'Sunflower', songs=10)
print(albums2)

print("---------------")
#8-8

while True:
    print("\nPlease enter an artist and album title. (enter 'q' to quit)")

    artist_input = input("Artist: ")
    if artist_input == 'q':
        break

    album_imput = input('Album: ')
    if album_imput == 'q':
        break

    album = make_album(artist_input, album_imput)

    print(album)

print('Finishing program')