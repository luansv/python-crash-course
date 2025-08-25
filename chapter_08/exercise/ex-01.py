#8-1
from hmac import digest_size


def display_message(subject):
    print(f'Im learning about {subject} ')

display_message('functions')

print("-----------------")
#8-2

def favbook(title):
    print(f'My favorite book is {title.title()}')

favbook('Battle Royale')

print("-----------------")
#8-3

def make_shirt(size, logo):
    print(f'Shirt´s size: {size} \n Logo: {logo.title()}')

make_shirt('M', 'Computer Science')

print("-----------------")
#8-4

make_shirt(size='large', logo='I love python')

print("-----------------")
#8-5

def describe_city(name, country='Brazil'):
    print(f'{name.title()} is in {country.title()}')

describe_city('Nayeon', 'South Korea')
describe_city('James', 'Iceland')
describe_city('Pedro')