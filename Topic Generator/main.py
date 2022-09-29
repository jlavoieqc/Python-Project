import random
import urllib.request

#here is the list of books that will be generated
#url
movies_url = "https://raw.githubusercontent.com/jlavoieqc/Python-Project/main/Topic%20Generator/movies.txt"
books_url = "https://raw.githubusercontent.com/jlavoieqc/Python-Project/main/Topic%20Generator/books.txt"
tv_url = "https://raw.githubusercontent.com/jlavoieqc/Python-Project/main/Topic%20Generator/tv.txt"
vg_url = "https://raw.githubusercontent.com/jlavoieqc/Python-Project/main/Topic%20Generator/vg.txt"
music_url = "https://raw.githubusercontent.com/jlavoieqc/Python-Project/main/Topic%20Generator/music.txt"
food_url = "https://raw.githubusercontent.com/jlavoieqc/Python-Project/main/Topic%20Generator/food.txt"
animals_url = "https://raw.githubusercontent.com/jlavoieqc/Python-Project/main/Topic%20Generator/animals.txt"

def main():
    #movies
    response = urllib.request.urlopen(movies_url)
    long_txt = response.read().decode()
    movies_list = long_txt.splitlines()
    #books
    response = urllib.request.urlopen(books_url)
    long_txt = response.read().decode()
    books_list = long_txt.splitlines()
    #tv
    response = urllib.request.urlopen(tv_url)
    long_txt = response.read().decode()
    tv_list = long_txt.splitlines()
    #vg
    response = urllib.request.urlopen(vg_url)
    long_txt = response.read().decode()
    vg_list = long_txt.splitlines()
    #music
    response = urllib.request.urlopen(music_url)
    long_txt = response.read().decode()
    music_list = long_txt.splitlines()
    #food
    response = urllib.request.urlopen(food_url)
    long_txt = response.read().decode()
    food_list = long_txt.splitlines()
    #animals
    response = urllib.request.urlopen(animals_url)
    long_txt = response.read().decode()
    animals_list = long_txt.splitlines()
    
    
    #choose a category
    category = input('Choisit Une Catégorie: (1) Films, (2) Livres, (3) TV Shows, (4) Jeux Vidéos, (5) Musique, (6) Sport, (7) Nourriture, (8) Animaux, (9) Pays: ')
    #choose a word
    if category == '1':
        print(random.choice(movies_list))
    elif category == '2':
        print(random.choice(books_list))
    elif category == '3':
        print(random.choice(tv_list))
    elif category == '4':
        print(random.choice(vg_list))
    elif category == '5':
        print(random.choice(music_list))
    elif category == '6':
        print(random.choice(food_list))
    elif category == '7':
        print(random.choice(animals_list))
    else:
        print('Choisit une catégorie valide')
        main()
main()