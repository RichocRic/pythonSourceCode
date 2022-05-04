import requests
from bs4 import BeautifulSoup
import os.path
import csv


url_base = 'https://books.toscrape.com/'

def recupLienspage():
    """_summary_
get all bookslinks for all webpages
    Returns:
        _type_: _description_
    """ 
    
    livresLiens = []
    for x in range(1,51):
        lienspages = url_base+'catalogue/page-{}.html'.format(x) #création des l'URL sur lequel on va récupérer les liens des livres
        response = requests.get(lienspages)
        soup = BeautifulSoup(response.content, 'lxml')
        lstlivres = soup.find_all('h3')#Récupération du contenu de tt les tags H3 sur chaque page 'LiensPages'
        for book in lstlivres:
            for lien in book.find_all('a'):
                livresLiens.append(url_base+'catalogue/' + lien['href'])
                
    return livresLiens

liens = recupLienspage()

notation = {'One':'1/5','Two':'2/5','Three':'3/5','Four':'4/5','Five':'5/5'}
dico = {}

listeliensvide = []
entetCsv = ['product_page_url', 'universal_product_code(upc)', 'title', 'price_including_tax', \
                             'price_excluding_tax', 'number-available', 'product_description', 'category', \
                             'review_rating', 'image_url'] 

chemin = os.getcwd() 

if not os.path.exists(chemin+'/'+'IMGS'): #Création du répertoire IMGS si celui -ci n'existe pas
    os.makedirs(chemin+'/'+'IMGS')
            
if not os.path.exists(chemin+'/'+'CSV'):#Création du répertoire CSV si celui -ci n'existe pas
    os.makedirs(chemin+'/'+'CSV') 
    
    
def creationCSVImgs():
    """_summary_
    récupération des liens, création des CSV et download des images
    """
    
    for link in liens:
        
        response = requests.get(link)
        if response.ok:
            
            soup2 = BeautifulSoup(response.text, 'lxml')#

            data = soup2.find_all('td')
            for row_item in data:
                
                if not row_item:
                    
                    listeliensvide.append(link)
                       
                else:
                    #remplissage du dictionnaire pour alimenter les C.S.V et la créations des vignettes
                    #TO DO SOLUTION pour les replaces
                    note = soup2.find("p", attrs={"class": "star-rating"}).attrs
                    note = str(note).replace("{'class': ['star-rating', '","").replace("']}","").strip()
                    dico["product_page_url"] = link
                    dico["universal_product_code(upc)"] = soup2.find("table", attrs={"class": "table table-striped"}).findAll('td')[0].text
                    dico["title"] = soup2.title.text.replace(' | Books to Scrape - Sandbox','').strip()
                    dico["price_including_tax"] = soup2.find("table", attrs={"class": "table table-striped"}).findAll('td')[3].text.replace('Â','')
                    dico["price_excluding_tax"] = soup2.find("table", attrs={"class": "table table-striped"}).findAll('td')[2].text.replace('Â','')
                    dico["number-available"] = soup2.find("p", attrs={"class": "instock availability"}).text.replace('In stock (','').replace(' available)','').strip()
                    dico["product_description"] = soup2.select("meta")[2]["content"].replace('     ', '')
                    dico["category"] = soup2.find("ul", attrs={"class": "breadcrumb"}).findAll('li')[2].text.strip()
                    dico["review_rating"] = notation[note]
                    imgUrl = soup2.findAll('img')[0].get('src').replace("../../","")
                    totalUrlImgs = url_base+imgUrl
                    dico["image_url"] = totalUrlImgs
                    saveUrlimgs = soup2.findAll('img')[0].get('src').replace("../../media/cache/2c/d2/","")  
            print("le dico : ",dico) 
            #print(listeliensvide)  
    
            nomFichier = dico["category"]+'.csv'# definition du nom du fichier un C.S.V/catégorie
            exists = os.path.isfile(chemin+"/"+'CSV'+'/'+nomFichier)
            with open(chemin+"/"+'CSV'+'/'+nomFichier,'a',newline='', encoding='utf-8') as f:
                
                videCsv = os.stat(chemin+"/"+'CSV'+'/'+nomFichier).st_size == 0# vérification de la taille du fichier évite de réecrire l'entete.
                writer = csv.DictWriter(f, delimiter=',',fieldnames=entetCsv)
                if videCsv:
                    writer.writeheader()#écriture entete du csv
                    writer.writerow(dico)    
                else:
                    writer.writerow(dico)#ajout d'une nouvelle ligne
                    rep = chemin+'/'+'IMGS'+'/'+dico["category"]+'/'
                    #print('le répertoire complet de image est: ',rep)
                    os.system('wget -P {0} {1}'.format(rep,totalUrlImgs)) #Enregistrement de la vignette.
                                          
creationCSVImgs()        
        

    
    