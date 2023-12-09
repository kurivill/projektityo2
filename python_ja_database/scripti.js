'use strict'

const nappi = document.getElementById('nappi');
const kentta = document.getElementById('inputField');



nappi.addEventListener('click', async function(evt) {
  const syote = document.getElementById('inputField').value;
  fetch('http://127.0.0.1:3000/start', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({'text': syote})
  })
    .then(response => response.json())
    .then(data => {
      console.log(data.nimi)
      console.log(data.rahat)
  })

    .catch(error => {
      console.error('Error', error);
      });
})




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
