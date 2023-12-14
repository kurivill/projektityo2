from yhteys import yhteys
from flask import Flask, request, Response, jsonify
import json
import random
from flask_cors import CORS
from geopy.distance import geodesic



class Player:
    def __init__(self):
        self.nimi = ""
        self.rahat = 1000
        self.sijaintimaa = "Finland"
        self.sijaintiairport = "Helsinki Vantaa Airport"
        self.lentokm = 0
        self.tavoitemaa = ""
        self.vihjeindeksi = 0
        self.listaindeksi = 0
        self.veikkausindeksi = 0


class Game:
    def __init__(self, listasanakirja):
        self.maat = []
        self.lentokentat = []
        self.vihjeet = listasanakirja
        self.kaydyt = []


luxembourghints = ["1. The Second richest country in the world", "2. The name of this country starts with a word from latin, which means “light”", "3. The Smallest country in Benelux"]
norwayhints = ["1. The most successful country in Winter Olympics", "2. This country has the highest standard of living in the world", "3. This country shares border with 3 other countries but it has more coastline than land border."]
polandhints = ["1. The biggest country in eastern middle-europe", "2. The flag of this country is like Pokemon ball", "3. During WWII. Germany built concentration camps in this country"]
swedenhints = ["1. Dancing queen", "2. The world leading furniture company was founded in this country", "3. This country is always one step ahead of Finland"]
latviahints = ["1. The jeans were invented in this country", "2. This country is sandwiched by other baltic countries", "3. The capital of this country is Riga"]
lithuaniahints = ["1. This country is known from its amber jewellery", "2. The biggest baltic country", "3. The capital of this country is Vilnius"]
spainhints = ["1. One of the biggest symbol of this country is a bull", "2. You can go to Africa with a ferry from this country in 1 hour", "3. The Finnish tourists have invaded this country"]
albaniahints = ["1. The flag of this country has 2 headed eagle on it", "2. This European country is one of the last ones that doesn’t have McDonalds", "3. 70% of this country is mountain area and its located opposite side of the “high heel”"]
bulgariahints = ["1. The Europes poorest country", "2. This country uses cyrillic alphabet", "3. The capital of this country is Sofia"]
icelandhints = ["1. This country is the westernmost nordic country", "2. This country is home to the artist Björk", "3. This country has hot springs"]
belgiumhints = ["1. This country's flag has the same colors as the flag of Germany", "2. This country, instead of France, invented french fries", "3. This country is often associated and mixed with France"]
germanyhints = ["1. This country's history in the World War II is very controversial", "2. This country is a major hub of the automotive industry", "3. This country is right in the middle of Europe"]
estoniahints = ["1. This country was last one to become independent from Soviet Union", "2. This country is a neighbour country of Finland", "3. This country's capital is Tallinn"]
finlandhints = ["1. This country is known for one of the most successful mobile phone businesses in the world", "2. This country is constantly ranked as one of the world's happiest countries", "3. This country has a very strong sauna culture"]
ukhints = ["1. This country is known for bands like Blur", "2. This country is not a part of the EU", "3. This country is home to fish and chips"]
irelandhints = ["1. This country is known for it’s pub culture", "2. This country is home to leprechauns", "3. This country’s capital is Dublin"]
croatiahints = ["1. Best football player of the year 2018 chosen by FIFA born here", "2. The famous dessert with bananas references to one of the biggest cities in this country", "3. One of the filming places for Game Of Thrones"]
francehints = ["1. A significant country in the world of fashion art", "2. The Disney animation about a cooking mouse is based on this country", "3. Known for its over 300 meters long tower"]
greecehints = ["1. This country has the third oldest language in the world", "2. A country known for the development of philosophy", "3. This country is the birthplace of the modern Olympics"]
italyhints = ["1. Leads UNESCO's statistics on world heritage sites", "2. Milla Magia lives on the slopes of a famous volcano in this country", "3. This country is known worldwide for its delicious pizza and pasta"]
sloveniahints = ["1. World famous 'Postojna' cave system is located in this country", "2. This country is mainly mountainous, and more than 90 percent of the country is more than 200 meters above sea level", "3. The capital of this country is a charming city named Ljubljana"]
czechrepublichints = ["1. World known ice-hockey player with a iconic mullet haircut was born here", "2. Federation which splitted into two separated countries in 1993", "3. Pilsner beer originates from this country"]
maltahints = ["1. Is known by taxfree casino licenses", "2. This country consista by many islands", "3. World's tenth-smallest country. With a total area of 316 squeare kilometers"]
hungaryhints = ["1. This country is known by its traditional spicy meat soup", "2. Local currency is known as HUF", "3. Tonava river splits this country at the middle"]
austriahints = ["1. Samuli Edelmann has drunk wine in this country", "2. Most of the landscape of this country consists of the Alps", "3. In which country was Mozart born in?"]
portugalhints = ["1. This country is known for its portwines", "2. This country is the 2016 football European champion", "3. This country is located at the tip of the Iberian peninsula"]
romaniahints = ["1. The Carpathian mountain range runs through the middle of this country.", "2. The currency used in this country is leu", "3. The famous region of Transylvania is located in this country"]
netherlandshints = ["1. This country is known for its EDM culture", "2. This country is known for its coffee shops", "3. This countrys capital is Amsterdam"]
switzerlandhints = ["1. This country is well known for their policy of neutrality", "2. This country is well known for its culture of watch-making", "3. The Red Cross was founded in this country"]
belarushints = ["1. This country's official dish is called draniki", "2. This country's president is the longest serving president in Europe", "3. This country's capital is Minsk"]
northmacedoniahints = ["1. This country changed its name as recently as 2019", "2. This country’s flag depicts a sun.", "3. This country’s capital city is Skopje"]
ukrainehints = ["1. This country is the second biggest country in Europe", "2. This country's currency is called hryvnia", "3. This country is on an ongoing war with russia"]
serbiahints = ["1. This country has the worlds oldest Orthodox church, the Sopočan monastery", "2. This country is a landlocked country, located east of Bosnia & Herzegovina", "3. This country’s capital is Belgrade"]
montenegrohints = ["1. This country’s name means The black mountain in English", "2. This country uses the euro as its currency, even thought it is not part of the Eurozone", "3. This country is located next north of Albania"]
russiahints = ["1. This country sold the region of Alaska to USA in 1867", "2. This country has the largest population in Europe", "3. This is the largest country in the world"]
slovakiahints = ["1. This country used to be a joint state with the Czech Republic.", "2. This country’s flag has a double cross ", "3. This country’s capital city is Bratislava"]
denmarkhints = ["1. This country is known for a very popular toy manufacturer", "2. This country is a nordic country", "3. This countrys capital is Copenhagen"]

hints = (luxembourghints, norwayhints, polandhints, swedenhints, latviahints, lithuaniahints,
         spainhints, albaniahints, bulgariahints, icelandhints, belgiumhints, germanyhints,
         estoniahints, finlandhints, ukhints, irelandhints, croatiahints, francehints,
         greecehints, italyhints, sloveniahints, czechrepublichints, maltahints, hungaryhints,
         austriahints, portugalhints, romaniahints, switzerlandhints, northmacedoniahints, serbiahints,
         montenegrohints, ukrainehints, belarushints, russiahints, slovakiahints, denmarkhints, netherlandshints)

countries = {"luxembourg":luxembourghints, "norway":norwayhints, "poland":polandhints, "sweden":swedenhints, "latvia":latviahints,
             "lithuania":lithuaniahints, "spain":spainhints, "albania":albaniahints, "bulgaria":bulgariahints, "iceland":icelandhints,
             "belgium":belgiumhints, "germany":germanyhints, "estonia":estoniahints, "finland":finlandhints, "united kingdom":ukhints,
             "ireland":irelandhints, "croatia":croatiahints, "france":francehints, "greece":greecehints, "italy":italyhints,
             "slovenia":sloveniahints, "czech republic":czechrepublichints, "malta":maltahints, "hungary":hungaryhints, "austria":austriahints, "portugal":portugalhints,
             "romania":romaniahints, "switzerland":switzerlandhints, "belarus":belarushints, "north macedonia":northmacedoniahints, "serbia":serbiahints, "ukraine":ukrainehints,
             "montenegro":montenegrohints, "russia":russiahints, "slovakia":slovakiahints, "denmark":denmarkhints, "netherlands":netherlandshints}

country_names = ["luxembourg", "norway", "poland", "sweden", "latvia", "lithuania", "spain",
                 "albania", "bulgaria", "iceland", "belgium", "germany", "estonia", "finland", "united kingdom", "uk"
                 "ireland", "croatia", "france", "greece", "italy", "slovenia", "czech republic", "malta", "hungary", "austria", "portugal", "romania"
                 "switzerland", "belarus", "serbia", "ukraine", "montenegro", "russia", "slovakia", "denmark" , "north macedonia"]




def maat():
    sql = "SELECT LOWER(country.name), airport.name FROM country, airport"
    sql += " WHERE airport.iso_country = country.iso_country AND country.iso_country != 'FI' AND country.continent = 'EU' AND airport.type = 'large_airport' GROUP BY country.name"
    kursori = yhteys.cursor(buffered=True)
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

def haevihje(pelaaja, peli):
    tuloste = "" # Tyhjä tuloste
    for a in peli.maat: # Käydään lista maista läpi. TÄhän on varmaan parempi tapa olemassa.
        if a == pelaaja.tavoitemaa: # Jos maa on tavoitemaa, siirrytään suoritukseen
            # tuloste = (countries[päämäärä][vihjeindeksi])
            tuloste = peli.vihjeet[pelaaja.tavoitemaa][pelaaja.vihjeindeksi] # Tallettaa vihjeen tuloste-muuttujaan
            pelaaja.vihjeindeksi += 1 # Vihjeindeksi kasvaa, kun oikea vihje tallessa
            pelaaja.rahat -= 100 # Rahaa lähtee
            print(pelaaja.rahat)
    return tuloste # Palauttaa vihjeen stringinä

def calculateDistance(pelaaja, peli):
    search1 = f"SELECT latitude_deg, longitude_deg FROM airport"
    search1 += f" WHERE name = '{pelaaja.sijaintiairport}' AND type = 'large_airport';"
    search2 = f"SELECT latitude_deg, longitude_deg FROM airport"
    search2 += f" WHERE name = '{peli.lentokentat[pelaaja.listaindeksi+1]}' AND type = 'large_airport';"
    kursori = yhteys.cursor()
    kursori.execute(search1)
    tulos1 = kursori.fetchone()
    kursori.execute(search2)
    tulos2 = kursori.fetchone()
    distance = geodesic(tulos1, tulos2).km
    return distance

def nykyinenSijainti(pelaaja):
    haku = f"SELECT latitude_deg, longitude_deg FROM airport WHERE name = '{pelaaja.sijaintiairport}';"
    kursori = yhteys.cursor()
    kursori.execute(haku)
    koordinaatit = kursori.fetchone()
    print(koordinaatit)
    return koordinaatit

def peliOhi(pelaaja):
    if pelaaja.rahat <= 0:
        print("Peli päättyy")
        raise SystemExit
    return

def tallennus(pelaaja, peli):
    kursori = yhteys.cursor()
    sql1 = f"DELETE FROM player;" # Tyhjentää tietokannan
    kursori.execute(sql1)
    sql2 = f"DELETE FROM listat;"
    kursori.execute(sql2)
    kursori.execute("ALTER TABLE listat AUTO_INCREMENT = 1;") # resetoi listat-taulun indeksin
    # Allaoleva syöttää pelaajan tiedot tietokantaan. Tulee siis 1 rivi.
    sql3 = f"INSERT INTO player(name, money, country_name, airport_name, lentokm, vihjeindeksi, listaindeksi, veikkausindeksi)"
    sql3 += f" VALUES('{pelaaja.nimi}', {pelaaja.rahat}, '{pelaaja.sijaintimaa}', '{pelaaja.sijaintiairport}', {pelaaja.lentokm}, {pelaaja.vihjeindeksi}, {pelaaja.listaindeksi}, {pelaaja.veikkausindeksi});"
    kursori.execute(sql3)
    indeksi = 0 # Indeksi maat ja lentokentat-sarakkeiden täyttämistä varten
    kaydytindeksi = 1 # Indeksi kaydyt-listan ja kaydyt-sarakkeen täyttämistä varten.
    kursori.execute(f"INSERT INTO listat(maat, lentokentat, kaydyt) VALUES ('Finland', 'Helsinki Vantaa Airport', 'Finland');")
    # Syötetään ylläolevalla lauseella ekaksi riviksi suomen tiedot sinne tietokantaan
    while indeksi < len(peli.maat):
    # Allaoleva rivi syöttää listat-tauluun ne maat ja lentokentät. Tulee siis 37 riviä tietoa
        kursori.execute(f"INSERT INTO listat(maat, lentokentat, kaydyt) VALUES('{peli.maat[indeksi]}', '{peli.lentokentat[indeksi]}', 'ei');")
        indeksi += 1
        if kaydytindeksi < len(peli.kaydyt): # Kaydyt-listassa on siis suomi, kun käynnistetään peli. Se ei tule sinne listaan, jos vaan jatkaa
            kursori.execute(f"UPDATE listat SET kaydyt = '{peli.kaydyt[kaydytindeksi]}' WHERE  id = {kaydytindeksi+1};")
            kaydytindeksi += 1

    """
    for y in peli.lentokentat:
        kursori.execute(f"INSERT INTO listat(lentokentat) VALUES('{y}');")
    for x in peli.maat:
        kursori.execute(f"INSERT INTO listat(maat) VALUES('{x}');")
    for z in peli.kaydyt:
        kursori.execute(f"INSERT INTO listat(kaydyt) VALUES('{z}');")"""
    yhteys.commit()
    return


def jatka(pelaaja, peli):
    kursori = yhteys.cursor()
    sql1 = "SELECT * from player;"
    kursori.execute(sql1)
    pelaajanstatsit = kursori.fetchall()
    pelaaja.nimi = pelaajanstatsit[0][0]
    pelaaja.rahat = pelaajanstatsit[0][1]
    pelaaja.sijaintimaa = pelaajanstatsit[0][2]
    pelaaja.sijaintiairport = pelaajanstatsit[0][3]
    pelaaja.lentokm = pelaajanstatsit[0][4]
    pelaaja.vihjeindeksi = pelaajanstatsit[0][5]
    pelaaja.listaindeksi = pelaajanstatsit[0][6]
    pelaaja.veikkausindeksi = pelaajanstatsit[0][7]
    sql2 = "SELECT * from listat;"
    kursori.execute(sql2)
    pelinstatsit = kursori.fetchall()
    indeksi = 1 # TÄmä sitä varten, että skipataan suomi, kun tehdään maa- ja lentokentat-listat
    jatkuukaydyt = 0 # TÄllä voidaan sitten viitata niin, että saadaan suomi kaydyt-listaan

    while indeksi < 37:
        peli.maat.append(pelinstatsit[indeksi][1])
        peli.lentokentat.append(pelinstatsit[indeksi][2])

        if pelinstatsit[indeksi][3] != 'ei':
            peli.kaydyt.append(pelinstatsit[jatkuukaydyt][3])
            jatkuukaydyt += 1

        indeksi += 1
    return



pelaaja = Player()
peli = Game(countries)

def testiupdate(pelaaja, peli):
    sql = f"UPDATE"
# Alla testattu ja toimiva flask-funktio, joka päivittää pelaaja-olion nimeksi nettisivun syötteeksi

app = Flask(__name__)
CORS(app) # Huom! Tämä on tärkeä rivi, jotta homma toimii. Flask-cors pitää olla asennettuna

@app.route('/start', methods=['POST']) #methods pitää muistaa, muuten ei toimi
def startti():
    sqlhaku = maat()
    random.shuffle(sqlhaku)
    for x in sqlhaku:
        peli.maat.append(x[0])
    for y in sqlhaku:
        peli.lentokentat.append(y[1])

    print(peli.maat[0])
    pelaaja.tavoitemaa = peli.maat[pelaaja.listaindeksi]
    peli.kaydyt.append(pelaaja.sijaintimaa)
    print(pelaaja.rahat) # testausta varten printattu oliosta jotain.
    data = request.get_json() # varastoidaan frontista saatu json data-muuttujaan
    print(data) # printataan saatu data, jotta tiedetään, että frontista tulee jotain
    pelaaja.nimi = data.get('text') # Tällä saadaan haluttu osa vastausta pythoniin.
    print(pelaaja.nimi)
    vastaus = {
        'nimi': f"{pelaaja.nimi}",
        'rahat': f"{pelaaja.rahat}",
        'sijaintimaa': f"{pelaaja.sijaintimaa}",
        'lentokm': f"{pelaaja.lentokm}"
    }
    response = jsonify(vastaus) # Tämä rivi muuttaa sanakirjamuodossa olevan vastauksen jsoniksi
    return response # palautetaan json-vastaus


@app.route('/vihje', methods=['GET'])
def vihje():
    print("vihjeen osto havaittu")
    peliOhi(pelaaja)
    vihje = haevihje(pelaaja, peli)
    vihjevastaus = {
        "vihje": f"{vihje}",
        "rahat": f"{pelaaja.rahat}"
    }
    vihjeresponse = jsonify(vihjevastaus)
    return vihjeresponse

@app.route('/tallenna', methods=['GET'])
def save():
    print("tallennuskäsky saatu")
    print(f"{peli.kaydyt[0]}")
    tallennus(pelaaja, peli)
    tallennusvastaus = {
        "vahvistus": "OK"
    }
    tallennusresponse = jsonify(tallennusvastaus)
    return tallennusresponse

@app.route('/jatka', methods=['GET'])
def jatkuu():
    print("jatkamiskäsky saatu")
    jatka(pelaaja, peli)
    print(pelaaja.nimi)
    print(peli.kaydyt[0])
    print(peli.kaydyt[1])
    palautettavatvihjeet = []
    indeksi = 0
    while pelaaja.vihjeindeksi > indeksi:
        palautettavatvihjeet.append(peli.vihjeet[pelaaja.tavoitemaa][indeksi])
        indeksi += 1
    jatkamisvahvistus = {
        "vahvistus": "OK",
        "nimi": f"{pelaaja.nimi}",
        "rahat": f"{pelaaja.rahat}",
        "lentokm": f"{pelaaja.lentokm}",
        "sijaintimaa": f"{pelaaja.sijaintimaa}",
        "vihjeet": f"{palautettavatvihjeet}"
    }
    jatkamisresponse = jsonify(jatkamisvahvistus)
    return jatkamisresponse



@app.route('/veikkaa', methods=['POST'])
def veikkaus():
    print("saatu funktiokutsu")
    data = request.get_json()
    veikkaus = data.get('text')
    for o in peli.kaydyt:
        print(o)
    if pelaaja.tavoitemaa == veikkaus:
        print("veikkaus oikein")
        peli.kaydyt.append(pelaaja.tavoitemaa)
        print(len(peli.kaydyt))
        for p in peli.kaydyt:
            print(p)
        pelaaja.rahat += 100
        pelaaja.vihjeindeksi = 0
        pelaaja.sijaintiairport = peli.lentokentat[pelaaja.listaindeksi]
        pelaaja.sijaintimaa = pelaaja.tavoitemaa # Pelaajan sijainti vaihtuu tavoitemaaksi
        lentomatka = calculateDistance(pelaaja, peli) # Pelaajan lentomatka lasketaan.
        koordinaatit = nykyinenSijainti(pelaaja)
        pelaaja.listaindeksi += 1
        pelaaja.lentokm += lentomatka # pelaajan lentokilometreihin lisätään lentomatka
        pelaaja.tavoitemaa = peli.maat[pelaaja.listaindeksi]

        print(f"Rahat. Pitäisi olla 1000, jos ekalla oikein: {pelaaja.rahat}"
              f" sijainti. Pitäisi vaihtua suomesta: {pelaaja.sijaintimaa}"
              f" pelaajan vihjeindeksi. 0? : {pelaaja.vihjeindeksi}"
              f" pelin listaindeksi ekan siirtymän jälkeen. 1? : {pelaaja.listaindeksi}"
              f" lentokilsat? : {pelaaja.lentokm}")


        vastaus = {

            "rahat": f"{pelaaja.rahat}",
            "sijainti": f"{pelaaja.sijaintimaa}",
            "lentokm": f"{pelaaja.lentokm}",
            "koordinaatit_lat": f"{koordinaatit}"
            }
        veikkausresponse = jsonify(vastaus)
        return veikkausresponse

    else:
        if pelaaja.vihjeindeksi == 2:
            print("vastaus väärin, vihjeet käytetty")
            pelaaja.sijaintimaa = pelaaja.tavoitemaa
            lentomatka = calculateDistance(pelaaja, peli)
            pelaaja.sijaintiairport = peli.lentokentat[pelaaja.listaindeksi]
            pelaaja.listaindeksi += 1
            pelaaja.lentokm += lentomatka
            pelaaja.rahat -= 100
            pelaaja.vihjeindeksi = 0

            pelaaja.tavoitemaa = peli.maat[pelaaja.listaindeksi]

            print(f"Rahojen pitäisi olla -100 alkuperäisestä: {pelaaja.rahat}")
            print(f"Lentokilometrit: {pelaaja.lentokm}")

            vastaus = {

                "rahat": f"{pelaaja.rahat}",
                "sijainti": f"{pelaaja.sijaintimaa}",
                "lentokm": f"{pelaaja.lentokm}"

            }
            veikkausresponse = jsonify(vastaus)
            return veikkausresponse

        else:
            print("vastaus väärin, vihjeitä jäljellä")
            vihje = haevihje(pelaaja, peli)
            print(f"Vihjeindeksi: {pelaaja.vihjeindeksi}"
                  f" rahat: {pelaaja.rahat}")
            vastaus = {
                "rahat": f"{pelaaja.rahat}",
                "vihje": f"{vihje}",
                "sijainti": f"{pelaaja.sijaintimaa}",
                "lentokm": f"{pelaaja.lentokm}"
            }

            veikkausresponse = jsonify(vastaus)
            return veikkausresponse







if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

