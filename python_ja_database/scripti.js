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
  })

    .catch(error => {
      console.error('Error', error);
      });
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
