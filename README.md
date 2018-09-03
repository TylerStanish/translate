[![Build Status](https://travis-ci.org/TylerStanish/translate.svg?branch=master)](https://travis-ci.org/TylerStanish/translate)

Master will be the 'main' branch where we build releases and do CI. Dev is the development branch

## So what is this?
This is the backend for a translation app I'm making. I've been struggling to really memorize words that I would enter into Google translate so this is an app where you can tag certain translations and practice them later on (with flashcards? idk)

## Tests
Run the tests by ensuring the settings point to the dev settings file:
```
python manage.py test --settings=translate_practice.settings.dev
```
