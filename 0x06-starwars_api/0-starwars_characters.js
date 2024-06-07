#!/usr/bin/node
/* Print all character of a Star Wars movie */

const path = require('path');
const args = process.argv;
const util = require('util');
const request = util.promisify(require('request'));

async function makeRequest () {
  try {
    const filmId = parseInt(args[2]);
    const filmUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;
    const filmResponse = await request(filmUrl);
    const film = JSON.parse(filmResponse.body);

    const characterNames = await Promise.all(film.characters.map(
      async characterUrl => {
        const characterResponse = await request(characterUrl);
        const character = JSON.parse(characterResponse.body);
        return character.name;
      }));

    characterNames.forEach(name => {
      console.log(name);
    });
  } catch (error) {
    console.error(error);
  }
}

if (args.length === 3) {
  makeRequest();
} else {
  console.log(`Usage ./${path.basename(args[1])} <Film Id>`);
}