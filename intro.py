import requests
from bs4 import  BeautifulSoup

url = "https://www.docstring.fr/api/books_to_scrape/index.html"

try:
    response = requests.get(url)
    response.raise_for_status()

    # with open("./htmls/books_to_scrape.html", "w") as file:
        # file.write(response.text) # Il est aussi possible de faire response.json pour les API

    #Lecture du fichier html par soup
    soup = BeautifulSoup(open("./htmls/books_to_scrape.html"), "html.parser")
    #ou
    #soup = BeautifulSoup(response.text, "html.parser")

    print(soup.prettify()) # Affiche le code html de la page de manière indentée


    body = soup.find_all('body') # Retourne toutes les occurences sous forme de liste
    #print(body)
    images = soup.find_all('article', class_="product_pod")
    print('Article de produit: ', images)

    aside = soup.find('aside')

    # Loop sur les enfants d'un élément trouvé
    for child in aside.children:
        if child.name: # Evite d'afficher les None générer par les retour à la ligne / tabulation
            print('Nom de balise: ', child.name)

    side_categories = aside.find('div', class_="side_categories")
    # links = side_categories.find_all('a') # Recherche soup d'une recherche
    categories_div = side_categories.find('ul').find('li').find('ul')
    categories = [child.text.strip() for child in categories_div.children if child.name]

    print('Categories: ', categories)

    images = soup.find('section').find_all('img')

    for image in images:
        print(image.get('src')) # on peut aussi utiliser ['src'] comme dans un dictionnaire, cependant si l'attribut n'existe pas cela crée une erreur dans le code

    titles = soup.find('section').find_all('h3')
    book_titles = [title.find('a').get('title') for title in titles]
    print(book_titles)
    # ou ( A savoir qu'il n'y a pas de bonne méthode saus celle qui permet d'éviter les possibles erreur lors du changement de code de la page
    titles = [a['title'] for a in soup.find_all('a', title=True)]
    print(titles)

# Exemple de gestion d'erreur
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
except requests.exceptions.RequestException as err:
    print ("OOps: Something Else",err)


