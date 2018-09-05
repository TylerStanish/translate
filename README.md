[![Build Status](https://travis-ci.org/TylerStanish/translate.svg?branch=master)](https://travis-ci.org/TylerStanish/translate)

Master will be the 'main' branch where we build releases and do CI. Dev is the development branch

## So what is this?
This is the backend for a translation app I'm making. I've been struggling to really memorize words that I would enter into Google translate so this is an app where you can tag certain translations and practice them later on (with flashcards? idk)

## Tests
Anybody here won't be able to test (except me) because Google Cloud requires me (at least to my knowledge) to load in application credentials before even importing their modules. So I can't even mock without loading the creds without changing my Django views just to accommodate the testing environment. But the travis url is above though
