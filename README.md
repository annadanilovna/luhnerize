# Luhnerize
Simple Python tool to use the Luhn algorithm to generate valid 16 digit numbers.

## Install

    $ git clone https://github.com/annadanilovna/luhnerize.git
    $ cd luhnerize
    $ pipenv install

## Usage

    $ cd luhnerize
    $ pipenv shell
    $ python luhnerize 123412341234
    1234123412340008
    1234123412340016
    ...
    1234123412349983
    1234123412349991
