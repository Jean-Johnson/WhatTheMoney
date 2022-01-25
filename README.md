# WhatTheMoney
To keep track finance for lazy people like me.. and i am bored


## Create Env
```
conda env create -f environment.yml
```
Note edit the environment.yml files last line with the location of your env path

## running

Excecute run.bat in CMD shell
```
run.bat
```

or if you know how to set env in other terminals then set
Moneyconfig=dev

then execute
```
python manage.py runserver --port 5000 --host "0.0.0.0"
```