'use strict';

const btn = document.querySelector('.btn-country');
const countriesContainer = document.querySelector('.countries');

///////////////////////////////////////
function CreateCountryCard(countryName) {
  const request = new XMLHttpRequest();
  request.open(
    'GET',
    'https://countries-api-836d.onrender.com/countries/name/' + countryName
  );
  request.send();
  console.log(request.responseText);
  request.addEventListener('load', function () {
    const [data] = JSON.parse(this.responseText);
    console.log(data);

    const html = `<article class="country">
  <img class="country__img" src="${data.flag}" />
  <div class="country__data">
  <h3 class="country__name">${data.name}</h3>
  <h4 class="country__region">${data.region}</h4>
  <p class="country__row"><span>${(+data.population / 1000000).toFixed(
    1
  )}</span>million people</p>
      <p class="country__row"><span>${data.languages[0].name}</span>LANG</p>
        <p class="country__row"><span>${data.currencies[0].name} ${
      data.currencies[0].symbol
    }</span>CUR</p>
        </div>
        </article>`;
    console.log(html);
    countriesContainer.insertAdjacentHTML('beforeend', html);
  });
}

const countriesList = [
  'bharat',
  'italy',
  'germany',
  'france',
  'spain',
  'portugal',
  'norway',
  'sweden',
  'finland',
  'denmark',
  'switzerland',
  'shrilanka',
  'japan',
];
for (const x of countriesList) {
  CreateCountryCard(x);
}
