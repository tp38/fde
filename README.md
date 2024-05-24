# FDE in Python

The goal of the application is to save Nat's activity for FDE. 
It was written in Python.

## Installation

1. Create a virtualenv in ~/fde (or wherever you want) with :
    > $ virtualenv ~/fde
2. Just download this project on local (ie : ~/fde/prod/ ).
3. Activate the virtual env with 
    > $ source ~/fde/bin/activate
4. Install required modules with :
    > (fde)$ pip install --upgrade pip
    > (fde)$ pip install -r requirements.txt
    > (fde)$ deactivate
5. In this directory, copy fildeclair.sq3.example in fildeclair.sq3
    > cp fildeclair.sq3.example fildeclair.sq3
6. Copy the config.py.example in config.py
    > cp config.py.example config.py

## Configuration

There's two files to configure : 
1. config.py : set up the value according your needs :   
    SERVER : the web server to store the report files   
    LOGIN  : the account use to connect to SERVER   
    PASSWORD : the password use to connect to SERVER    
    S_PATH : path to store files   
2. in/period.json. This file must contain the years and months to be taken into account.   
    Format is { "yyyy1": ["mm8", "mm9", .... "mm12" ], "yyyy2": [ "mm1", "mm2"] } with :   
    - yyyy1 and yyyy2 : years on 4 digits
    - mm1, mm2, ...mm12 : months on 2digits

## Usage

### input a day result

1. Activate your virtual env :
    > $ source ~/fde/bin/activate
2. start the DayResult python module :
    > (fde) $ python DayResult.py
3. answer to the questions like this example :   
    (FdE) $ python DayResult.py   
    Entrer la date concernée : **23/05/2024**   
    ( 2024-05-23 :    0 / 0.0 (0.0) [] )   
    Voulez-vous modifier [m] / sauvegarder [s] / supprimer [d] cet enregistrement ou quitter [q] ?    
    **m**   
        Entrer le chiffre d'affaire (0) : **153**   
        Entrer le nombre d'heure (0.0) : **8**    
        Entrer le nombre d'heure sup (0.0) : **1**    
        Entrer un commentaire éventuel (None): **il ne fait pas beau**   
    ( 2024-05-23 :  153 / 8.0 (1.0) [il ne fait pas beau] )
    Voulez-vous modifier [m] / sauvegarder [s] / supprimer [d] cet enregistrement ou quitter [q] ? **s**
    ( 2024-05-23 :  153 / 8.0 (1.0) [il ne fait pas beau] )
    Voulez-vous modifier [m] / sauvegarder [s] / supprimer [d] cet enregistrement ou quitter [q] ? **q**
    (FdE) $ 


### display month result

1. Activate your virtual env :
    > $ source ~/fde/bin/activate
2. start the MonthResult python module :
    > (fde) $ python MonthResult.py [date=dd/mm/yyyy]

    (FdE) $ python MonthResult.py date=23/05/2024
    2024-05 : 153€ / 8.0h (1.0) [prime : -3268.15]
        ( 2024-05-23 :  153 / 8.0 (1.0) = 19.1€/h [il ne fait pas beau] )
    (FdE) $

### send report to web server

for this module, web server (SERVER) must be accessible and LOGIN/PASSWORD account must have write access on S_PATH (SERVER, LOGIN, PASSWORD and S_PATH are setup in config.py file)
1. Activate your virtual env :
    > $ source ~/fde/bin/activate
2. start the Report python module :
    > (fde) $ python Report.py

