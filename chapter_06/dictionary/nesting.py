alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
 print(alien)


langs = []

for lang_names in range(30):
    new_lang = {
        'name': 'French', 'country': 'France'
    }
    langs.append(new_lang)

for lang in langs[:3]:
    if lang['name'] == 'French':
        lang['name'] = 'Portuguese'
        lang['country'] = 'Brazil'

for lang in langs[:5]:
    print(lang)
print('...')

#Len prints the number of values inside an object
print(f'Toal number of languages: {len(langs)}')

print('-----------------------')

favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'swift'],
 }

for name, langs in favorite_languages.items():
    print(f"\n {name.title()}'s favorite langs are:")
    for lang in langs:
        print(f'\t{lang.title()}')

