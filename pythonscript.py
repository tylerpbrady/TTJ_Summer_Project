from urllib.request import *
from json import *
from datetime import *
from operator import *
from bs4 import BeautifulSoup
import math

with open("index.html") as fp:
   soup = BeautifulSoup(fp, 'html.parser')

soup = BeautifulSoup("<html>https://na.op.gg/champions/aatrox/top/build?region=na&tier=all</html>", 'html.parser')



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



   
