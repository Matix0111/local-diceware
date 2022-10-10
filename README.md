# local-diceware
Diceware password generator, but local.

# Usage
This generator has 3 optional command-line arguments:
- `-r` number of random words
- `-t` append words in title case
- `-s` append random symbols between words

There is no max number of rolls, however there is a minimum of 1. All command-line arguments may be used concurrently.

# Examples
`python3 generator.py`
```
Chosen: hut unenvied germless suitably ripening 
Password: hutunenviedgermlesssuitablyripening
Password length: 35
Entropy: 188.02 bits
```
`python3 generator.py -t -r 6`
```
Chosen: Jokingly Shudder Pointy Hybrid Gaffe Mystify 
Password: JokinglyShudderPointyHybridGaffeMystify
Password length: 39
Entropy: 256.52 bits
```
`python3 generator.py -s -r 12 -t`
```
Chosen: Remarry / Panning " Spouse " Operating . Immobile $ Urethane < Revenge * Apprehend ] Diffusion | Payday { Septum : Parole 
Password: Remarry/Panning"Spouse"Operating.Immobile$Urethane<Revenge*Apprehend]Diffusion|Payday{Septum:Parole
Password length: 99
Entropy: 779.86 bits
```

# Notes
This generator uses diceware's newer and larger wordlist, which can be found [here](https://diceware.readthedocs.io/en/stable/wordlists.html).
