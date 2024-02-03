#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    const moviesWithWedgeAntilles = films.filter(film => {
      const characters = film.characters.map(url => url.split('/').slice(-2, -1)[0]);
      return characters.includes(characterId.toString());
    });
    console.log(moviesWithWedgeAntilles.length);
  }
});
