from bs4 import BeautifulSoup
import requests
import lxml
from flask import Flask, render_template, request

app = Flask(__name__)


# Site with links to Canadian Breweries sorted by province.
url = 'http://www.beercrank.ca/p/canadian-breweries.html'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')





# Scraping the data by province and then cleaning the string.
# Here we set the indices of the different provinces
text = soup.text
alb = text.find("Alberta")
bc = text.find("British Columbia")
man = text.find("Manitoba", 500)
nb = text.find("New Brunswick")
nwf = text.find("Newfoundland & Labrador")
ns = text.find("Nova Scotia")
ont = text.find("Ontario")
pei = text.find("Prince Edward Island")
qub = text.find("Québec")
sas = text.find("Saskatchewan")
terr = text.find("Yukon, Northwest Territories and Nunvavut")
end = text.find("Updated")
# Variables will only read their related sectionso of the string
Alberta = text[alb:bc]
British_Columbia = text[bc:man]
Manitoba = text[man:nb]
New_Brunswick = text[nb:nwf]
Newfoundland_and_Labrador = text[nwf:ns]
Nova_Scotia = text[ns:ont]
Ontario = text[ont:pei]
Prince_Edward_Island = text[pei:qub]
Quebec = text[qub:sas]
Saskatchewan = text[sas:terr]
Territories = text[terr:end]

# This is a function to have the query call the appropriate variable.
def pour_the_brew(data):
    if data == "Alberta":
        brewlist = Alberta.replace("(Facebook)","")
        brewlist = brewlist.replace("(Instagram)","")
        brewlist = brewlist.replace("(Twitter)","")
        brewlist = brewlist.splitlines()
        return render_template('index.html', brewlist=brewlist)
    if data == "British_Columbia":
        brewlist = British_Columbia.replace("(Facebook)", "")
        brewlist = brewlist.replace("(Instagram)", "")
        brewlist = brewlist.replace("(Twitter)", "")
        brewlist = brewlist.splitlines()
        return render_template('index.html', brewlist=brewlist)
    if data == "Manitoba":
        brewlist = Manitoba.replace("(Facebook)", "")
        brewlist = brewlist.replace("(Instagram)", "")
        brewlist = brewlist.replace("(Twitter)", "")
        brewlist = brewlist.splitlines()
        return render_template('index.html', brewlist=brewlist)
    if data == "New_Brunswick":
        brewlist = New_Brunswick.replace("(Facebook)", "")
        brewlist = brewlist.replace("(Instagram)", "")
        brewlist = brewlist.replace("(Twitter)", "")
        brewlist = brewlist.splitlines()
        return render_template('index.html', brewlist=brewlist)
    if data == "Newfoundland":
        brewlist = Newfoundland_and_Labrador.replace("(Facebook)", "")
        brewlist = brewlist.replace("(Instagram)", "")
        brewlist = brewlist.replace("(Twitter)", "")
        brewlist = brewlist.splitlines()
        return render_template('index.html', brewlist=brewlist)
    if data == "Nova_Scotia":
        brewlist = Nova_Scotia.replace("(Facebook)", "")
        brewlist = brewlist.replace("(Instagram)", "")
        brewlist = brewlist.replace("(Twitter)", "")
        brewlist = brewlist.splitlines()
        return render_template('index.html', brewlist=brewlist)
    if data == "Ontario":
        brewlist = Ontario.replace("(Facebook)", "")
        brewlist = brewlist.replace("(Instagram)", "")
        brewlist = brewlist.replace("(Twitter)", "")
        brewlist = brewlist.splitlines()
        return render_template('index.html', brewlist=brewlist)
    if data == "Prince_Edward_Island":
        brewlist = Prince_Edward_Island.replace("(Facebook)", "")
        brewlist = brewlist.replace("(Instagram)", "")
        brewlist = brewlist.replace("(Twitter)", "")
        brewlist = brewlist.splitlines()
        return render_template('index.html', brewlist=brewlist)
    if data == "Quebec":
        brewlist = Quebec.replace("(Facebook)", "")
        brewlist = brewlist.replace("(Instagram)", "")
        brewlist = brewlist.replace("(Twitter)", "")
        brewlist = brewlist.splitlines()
        return render_template('index.html', brewlist=brewlist)
    if data == "Saskatchewan":
        brewlist = Saskatchewan.replace("(Facebook)", "")
        brewlist = brewlist.replace("(Instagram)", "")
        brewlist = brewlist.replace("(Twitter)", "")
        brewlist = brewlist.splitlines()
        return render_template('index.html', brewlist=brewlist)
    if data == "Territories":
        brewlist = Territories.replace("(Facebook)", "")
        brewlist = brewlist.replace("(Instagram)", "")
        brewlist = brewlist.replace("(Twitter)", "")
        brewlist = brewlist.splitlines()
        return render_template('index.html', brewlist=brewlist)
    else:
        print("Error in query selection")

placeholder = ["""
Hey, we found a dead mouse in our beer, eh? That means you owe us a free case.”
- Doug McKenzie, 'Strange Brew'."""]

@app.route("/",  methods = ['GET', 'POST'])
def brewery_page():
    if request.method == 'POST':
        data = request.form.to_dict()
        return pour_the_brew(data["provinces"])
    else:
        return render_template('index.html', brewlist=placeholder)






