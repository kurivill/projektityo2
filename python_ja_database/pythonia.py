class pelaaja:
    def __init__(self, nimi, aloitusmaa, aloitusairport):
        self.nimi = nimi
        self.rahat = 1000
        self.sijainti_maa = aloitusmaa
        self.sijainti_airport = aloitusairport
        self.lentokm = 0


"""Scripti tehty sql-databasen luomista varten"""
"""Eli tarvitaan ainakin metodi pelaajan siirtämiseksi uuteen paikkaan. 
    Käytönnössä siis python saa flaski-parametreinä uuden kohteen, jonne sijainti siirtyy
    Funktio sitten hakee lentokentän, joka liitetty kohteena olevaan maahan, siirtää pelaajan
    sijainnin sinne, ja vähentää rahoista sen 100. Kun tämä tehty, niin databaseen updatetaan
    uudet tiedot.
    
    Periaatteessa kaikki muu saadaan varmaan toimimaan javascriptissä. Python on vaan 
    scoreboardin ylläpitämistä varten.
    
    Flask-parametrina pitänee myös saada se, että voittiko pelaaja rahaa, vai menettikö"""


"""PItää selvittää, että kuinka ison osan pelistä voi tehdä javascriptissä. Optimaalia varmaan
    olisi, mikäli python ja sql olisi vaan pelaajan datan tallentamista varten."""




    