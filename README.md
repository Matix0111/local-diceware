# local-diceware
Diceware password generator, but local.

# Usage
This generator has 3 optional command-line arguments:
- `-r` number of random words
- `-t` append words in title case
- `-s` append random symbols between words

There is no max number of rolls, however there is a minimum of 1 and the default is 5. All command-line arguments may be used concurrently.

# Examples
`python3 generator.py`
```
Chosen: irate stillness composer scruffy frown 
Password: iratestillnesscomposerscruffyfrown
Password length: 34
Entropy: 159.81 bits
```
`python3 generator.py -t -r 6`
```
Chosen: Untie Rural Glorify Splinter Nativity Crimson 
Password: UntieRuralGlorifySplinterNativityCrimson
Password length: 40
Entropy: 228.02 bits
```
`python3 generator.py -s -r 12 -t`
```
Chosen: Hatchery * Duly ` Wasting \ Womanhood % Require , Duvet / Genetics ? Reverb > Stature " Surfboard @ Cryptic > Canopener 
Password: Hatchery*Duly`Wasting\Womanhood%Require,Duvet/Genetics?Reverb>Stature"Surfboard@Cryptic>Canopener
Password length: 97
Entropy: 620.05 bits
```

# Notes
This generator uses diceware's newer and larger wordlist, which can be found [here](https://diceware.readthedocs.io/en/stable/wordlists.html).
