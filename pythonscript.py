from stat import FILE_ATTRIBUTE_SPARSE_FILE
from urllib.request import *
from json import *
from datetime import *
from operator import *
from bs4 import BeautifulSoup
import math
import requests
from firebase import firebase




# install parser: pip install lxml
# install requests: pip install requests
# install firebase: pip install python-firebase

# url format: urlBeggining championName urlEnding
urlBeggining = 'http://u.gg/lol/champions/'
urlEnding = '/build'

champs = {'aatrox', 'ahri', 'akali', 'akshan', 'alistar', 'alistar', 'amumu', 'anivia', 'annie', 'aphelios', 'ashe', 'aurelionsol', 'azir', 
'bard', 'blitzcrank', 'brand', 'braum', 'caitlyn', 'camille', 'cassiopeia', 'chogath', 'corki', 'darius', 'diana', 'drmundo', 'draven', 'ekko',
'elise', 'evelynn', 'ezreal', 'fiddlesticks', 'fiora', 'fizz', 'galio', 'gangplank', 'garen', 'gnar', 'gragas', 'graves', 'gwen', 'hecarim', 
'heimerdinger', 'illaoi', 'irelia', 'ivern', 'janna', 'jarvaniv', 'jax', 'jayce', 'jhin', 'jinx', 'kaisa', 'kalista', 'karma', 'karthus', 
'kassadin', 'katarina', 'kayle', 'kayn', 'kennen', 'khazix', 'kindred', 'kled', 'kogmaw', 'leblanc', 'leesin', 'leona', 'lillia', 'lissandra', 
'lucian', 'lulu', 'lux', 'malphite', 'malzahar', 'maokai', 'masteryi', 'missfortune', 'mordekaiser', 'morgana', 'nami', 'nasus', 'nautilus', 
'neeko', 'nidalee', 'nocturne', 'nunu', 'olaf', 'orianna', 'ornn', 'pantheon', 'poppy', 'pyke', 'qiyana', 'quinn', 'rakan', 'rammus', 'reksai', 
'rell', 'renata', 'renekton', 'rengar', 'riven', 'rumble', 'ryze', 'samira', 'sejuani', 'senna', 'seraphine', 'sett', 'shaco', 'shen', 'shyvana', 
'singed', 'sion', 'sivir', 'skarner', 'sona', 'soraka', 'swain', 'sylas', 'syndra', 'tahmkench', 'taliyah', 'talon', 'taric', 'teemo', 'thresh', 
'tristana', 'trundle', 'tryndamere', 'twistedfate', 'twitch', 'udyr', 'urgot', 'varus', 'vayne', 'veigar', 'velkoz', 'vex', 'vi', 'viego', 
'viktor', 'vladimir', 'volibear', 'warwick', 'wukong', 'xayah', 'xerath', 'xinzhao', 'yasuo', 'yone', 'yorick', 'yuumi', 'zac', 'zed', 'zeri', 
'ziggs', 'zilean', 'zoe', 'zyra'}

# for champ in champs:
#    fullUrl = urlBeggining + champ + urlEnding
#    source = requests.get(fullUrl).text
#    soup = BeautifulSoup(source, 'lxml')
#    name = soup.find('span', class_= 'champion-name').text
#    winRate = soup.find('div', class_= "value").text

#    print(f"{name}'s winrate is {winRate}")


db = firebase.FirebaseApplication("https://jaroniagg-default-rtdb.firebaseio.com/")

# This removes white space which allows us to 
# input "twisted fate" which will turn into "twistedfate"
# when creating the url there can't be whitespace

selectedChamp = input("Type your champion: ") 
selectedChamp = selectedChamp.replace(" ", "")         


if selectedChamp not in champs:
   print("Invalid champion.")
else: 
   fullUrl = urlBeggining + selectedChamp + urlEnding
   source = requests.get(fullUrl).text
   soup = BeautifulSoup(source, 'lxml')
   name = soup.find('span', class_= 'champion-name').text
   winRate = soup.find('div', class_= "value").text
   print(f"{name}'s winrate is {winRate}")


   result = db.put('/jaroniagg-default-rtdb/Garen', 'top', winRate)
   print(result)


# Code below is from CPE 101 Project 5. 
# This was the project where we wrote to txt files.



def read_quakes_from_file(filename):
   inFile = open(filename, "r")
   newlist = []
   for line in inFile:
      linelist = line.split()

      place = " ".join(linelist[4:])
      mag = linelist[0]
      longitude = linelist[1] 
      latitude = linelist[2]
      time = linelist[3]
      earthquake = Earthquake(place, float(mag), float(longitude), float(latitude), int(time))

      newlist.append(earthquake)
   inFile.close()

   return newlist


def get_json(url):
   with urlopen(url) as response:
      html = response.read()
   htmlstr = html.decode("utf-8")
   return loads(htmlstr)


def write_to_file(filename, set):
   out_file = open(filename, "w")

   for i in set:
      out_file.write(f"{eq.mag} {eq.longitude} {eq.latitude} {eq.time} {eq.place}\n")

   out_file.close()



   
