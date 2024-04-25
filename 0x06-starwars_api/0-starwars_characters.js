#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Define the base URL for the Star Wars API
const API_URL = 'https://swapi-api.hbtn.io/api';

// Check if the correct number of command-line arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Extract the movie ID from the command-line arguments
const movieId = process.argv[2];
const movieUrl = `${API_URL}/films/${movieId}/`;

// Make an HTTP GET request to fetch movie information
request(movieUrl, (err, _, body) => {
  // Handle errors from the request
  if (err) {
    console.error(err);
    process.exit(1);
  }

  // Check for unexpected status codes
  if (_.statusCode !== 200) {
    console.error(`Unexpected status code: ${_.statusCode}`);
    process.exit(1);
  }

  // Parse the response body to extract character URLs
  const filmData = JSON.parse(body);
  const charactersURL = filmData.characters;
  
  // Map character URLs to Promises for fetching character names asynchronously
  const charactersName = charactersURL.map(url =>
    new Promise((resolve, reject) => {
      // Make an HTTP GET request to fetch character information
      request(url, (promiseErr, __, charactersReqBody) => {
        // Handle errors from the request
        if (promiseErr) {
          reject(promiseErr);
        }
        // Resolve the Promise with the character name
        resolve(JSON.parse(charactersReqBody).name);
      });
    }));

  // Wait for all Promises to be resolved and print the character names
  Promise.all(charactersName)
    .then(names => console.log(names.join('\n')))
    .catch(allErr => console.error(allErr));
});
