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

champs = {'aatrox':'top', 'ahri':'mid', 'akali':'mid', 'akshan':'mid', 'alistar':'sup', 'amumu': 'jg', 'anivia':'mid', 'annie':'mid', 'aphelios':'bot', 'ashe':'bot', 'aurelionsol':'mid', 'azir':'mid', 
'bard':'sup', 'blitzcrank':'sup', 'brand':'sup', 'braum':'sup', 'caitlyn':'bot', 'camille':'top', 'cassiopeia':'mid', 'chogath':'top', 'corki':'mid', 'darius':'top', 'diana':'jg', 'drmundo':'top', 'draven':'bot', 'ekko':'jg',
'elise':'jg', 'evelynn':'jg', 'ezreal':'bot', 'fiddlesticks':'jg', 'fiora':'top', 'fizz':'mid', 'galio':'mid', 'gangplank':'top', 'garen':'top', 'gnar':'top', 'gragas':'top', 'graves':'jg', 'gwen':'top', 'hecarim':'jg', 
'heimerdinger':'top', 'illaoi':'top', 'irelia':'top', 'ivern':'jg', 'janna':'sup', 'jarvaniv':'jg', 'jax':'top', 'jayce':'top', 'jhin':'bot', 'jinx':'bot', 'kaisa':'bot', 'kalista':'bot', 'karma':'sup', 'karthus':'jg', 
'kassadin':'mid', 'katarina':'mid', 'kayle':'top', 'kayn':'jg', 'kennen':'top', 'khazix':'jg', 'kindred':'jg', 'kled':'top', 'kogmaw':'bot', 'leblanc':'mid', 'leesin':'jg', 'leona':'sup', 'lillia':'jg', 'lissandra':'mid', 
'lucian':'bot', 'lulu':'sup', 'lux':'sup', 'malphite':'top', 'malzahar':'mid', 'maokai':'sup', 'masteryi':'jg', 'missfortune':'bot', 'mordekaiser':'top', 'morgana':'sup', 'nami':'sup', 'nasus':'top', 'nautilus':'sup', 
'neeko':'mid', 'nidalee':'jg', 'nocturne':'jg', 'nunu':'jg', 'olaf':'jg','orianna':'mid', 'ornn':'top', 'pantheon':'sup', 'poppy':'jg', 'pyke':'sup', 'qiyana':'mid', 'quinn':'top', 'rakan':'sup', 'rammus':'jg', 'reksai':'jg', 
'rell':'sup', 'renata':'sup', 'renekton':'top', 'rengar':'jg', 'riven':'top', 'rumble':'top', 'ryze':'mid', 'samira':'bot', 'sejuani':'jg', 'senna':'sup', 'seraphine':'sup', 'sett':'top', 'shaco':'jg', 'shen':'top', 'shyvana':'jg', 
'singed':'top', 'sion':'top', 'sivir':'bot', 'skarner':'jg', 'sona':'sup', 'soraka':'sup', 'swain':'sup', 'sylas':'mid', 'syndra':'mid', 'tahmkench':'top', 'taliyah':'mid', 'talon':'mid', 'taric':'sup', 'teemo':'top', 'thresh':'sup', 
'tristana':'bot', 'trundle':'jg', 'tryndamere':'top', 'twistedfate':'mid', 'twitch':'bot', 'udyr':'jg', 'urgot':'top', 'varus':'bot', 'vayne':'bot', 'veigar':'mid', 'velkoz':'mid', 'vex':'mid', 'vi':'jg', 'viego':'jg', 
'viktor':'mid', 'vladimir':'mid', 'volibear':'jg', 'warwick':'jg', 'wukong':'jg', 'xayah':'bot', 'xerath':'mid', 'xinzhao':'jg', 'yasuo':'mid', 'yone':'mid', 'yorick':'top', 'yuumi':'sup', 'zac':'jg', 'zed':'mid', 'zeri':'bot', 
'ziggs':'mid', 'zilean':'sup', 'zoe':'mid', 'zyra':'sup'}

# for champ in champs:
#    fullUrl = urlBeggining + champ + urlEnding
#    source = requests.get(fullUrl).text
#    soup = BeautifulSoup(source, 'lxml')
#    name = soup.find('span', class_= 'champion-name').text
#    winRate = soup.find('div', class_= "value").text

#    print(f"{name}'s winrate is {winRate}")


db = firebase.FirebaseApplication("https://jaroniagg-default-rtdb.firebaseio.com/")
dbChampUrl = '/jaroniagg-default-rtdb/'

for champ in champs:
   role = champs[champ]
   fullUrl = urlBeggining + champ + urlEnding
   source = requests.get(fullUrl).text
   soup = BeautifulSoup(source, 'lxml')
   name = soup.find('span', class_= 'champion-name').text
   winRate = soup.find('div', class_= "value").text
   print(f"{name}'s winrate is {winRate}")


   result = db.put('/jaroniagg-default-rtdb/' + champ, role, winRate)
   

# This removes white space which allows us to 
# input "twisted fate" which will turn into "twistedfate"
# when creating the url there can't be whitespace

# selectedChamp = input("Type your champion: ") 
# selectedChamp = selectedChamp.replace(" ", "")         


# if selectedChamp not in champs:
#    print("Invalid champion.")
# else: 
#    fullUrl = urlBeggining + selectedChamp + urlEnding
#    source = requests.get(fullUrl).text
#    soup = BeautifulSoup(source, 'lxml')
#    name = soup.find('span', class_= 'champion-name').text
#    winRate = soup.find('div', class_= "value").text
#    print(f"{name}'s winrate is {winRate}")


#    result = db.put('/jaroniagg-default-rtdb/Aatrox', 'top', winRate)
#    print(result)


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



   
