'use strict'

/* Kaikki allaoleva on tehty yksinkertaiselle nettisivulle, jossa on vaan
formi, johon syötetään nimi ja formin nappia painamalla asioita tapahtuu.

Yhteys backin ja frontin välillä joka tapauksessa toimii, eli flaskiongelmat on
ainakin jossain määrin selätetty.
 */
const nappi = document.getElementById('nappi');
const kentta = document.getElementById('inputField');



nappi.addEventListener('click', async function(evt) {
  const syote = document.getElementById('inputField').value; // Eli tämä ottaa sen kentän syötteen
  fetch('http://127.0.0.1:3000/start', { //TÄtä voi käyttää pohjana kaikkiin muihin nappeihin
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({'text': syote}) //
  })
      /* Eli ylläoleva on se boilerplate, mitä tarvitaan, jotta backendiin lähtee
      jotain järkevää. body: on se varsinainen asia, mikä lähtee sinne json-muodossa.
       */
    .then(response => response.json()) // tämä rivi ottaa vastaan backendin lähettämän datan
    .then(data => {
      console.log(data.nimi) // Data tulee takaisin json-muodossa, eli siihen pitää viitata oikein
      console.log(data.rahat)
      console.log(data.sijaintimaa)
      console.log(data.lentokm)
      document.getElementById("pelaajanimi").textContent = data.nimi
  })

    .catch(error => {
      console.error('Error', error);
      });
})

vihjenappi.addEventListener('click', async function(evt) {
  const vihjenappi = document.getElementById("vihjenappi")
  const kohde = document.getElementById("vihje")
  fetch('http://127.0.0.1:3000/vihje',  {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    }


  })
      .then(response => response.json())
      .then(data => kohde.textContent = data.vihje)

      .catch(error => {
      console.error('Error', error);
      });
})


veikkausnappi.addEventListener('click', async function(evt) {
  const maaveikkaus = document.getElementById("veikattumaa").value
  const veikkaustulos = document.getElementById("onkooikein")
  const statsit = document.getElementById("statsit")
  fetch('http://127.0.0.1:3000/veikkaa', { //TÄtä voi käyttää pohjana kaikkiin muihin nappeihin
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({'text': maaveikkaus})

  })
      .then(response => response.json())

      .then(data => {
        document.getElementById("rahat").textContent = data.rahat
        document.getElementById("lentokm").textContent = data.lentokilometrit
        document.getElementById("sijainti").textContent = data.sijainti
        document.getElementById("tavoitemaa").textContent = data.tavoitemaa
        document.getElementById("nykyvihje").textContent = data.vihje
        console.log(data.sijainti)
        console.log(data.tavoitemaa)
        veikkaustulos.textContent = data.vastaus
        statsit.textContent = data.rahat + ' ' + data.sijainti
      }
        )
      .catch(error => {
        console.error('Error', error);
      });

})

tallenna.addEventListener('click', async function(evt) {
  const tallennusnappi = document.getElementById("tallenna")
  const vahvistus = document.getElementById("vahvistus")
  console.log('nyt lähtee käsky')
  fetch('http://127.0.0.1:3000/tallenna', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    }
  })
      .then(response => response.json())
      .then(data => vahvistus.textContent = data.vahvistus)

})





// ALla olevat on epätoivoisia yrityksiä saada homma toimimaaan. Jätetty muistomerkiksi


/*
nappi.addEventListener('click', async function(evt) {
  evt.preventDefault();
  const syote = document.getElementById('inputField').value;
  try {
    const response = await fetch(`http://127.0.0.1:3000/start`);
    const vastaus = await response.json();
    const nimi = vastaus.nimi
    const rahat = vastaus.rahat
    console.log(`nimi: ${nimi}, rahat: ${rahat}`)

  } catch (error) {
    console.log(error.message)
  }

})*/
/*
nappi.addEventListener('click', async function (evt) {
    const syote = kentta.value
    fetch('http://127.0.0.1:3000/start', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: syote })
    })
        .then(response => response.json())
        .then(data => {
            console.log(data.result);
        })
        .catch(error => {
            console.error('Error', error);
        });
})
*/
