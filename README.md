## guitarists and bands 


In this repository there is a main.py that take the name of a band or a guitarist, if it was given a band name it will return the guitarist of it and if it was given a guitarist name it will return what band that guitarist plays in,

## how to:

Authentication is required when using the main file, for registration see point below.
the application by defualt accept guitarists name if you wanted to check for bands you have to add -b to your request. 

positional arguments:
*  n: insert the name of the guitarist or the band you would like to check

optional arguments:
* -h, --help: show this help message and exit
* -b: check for bands
* -v: Decide the level of verbosity
* -p: password
* -u: usernamename(requires -p)


```
~/guitarists$ python main.py 'Slipknot' -b -v -u sayna -p 12345
User is present, password is valid
The guitar hero of Slipknot is Jim Root
```

## how to register:

to add a new user, you have to insert a username and a password to dbmanager as fallow:

* -h, --help: tells you the possible arguments you can insert
* -a: username
* -p: password

```
$ python dbmanager.py -a username -p password
Username username successfully added
```

## Check the validity:
To check if your credentials are valid, please insert in ```dbmanager.py```:
* -h, --help: tells you the possible arguments you can insert
* -c: username
* -p: password

```
$ python dbmanager.py -c username -p password
User is present, password is valid
```
## verbosity:
there is two level of verbosity in this application:
if you add the argument -v it return a sentence like:
```
The guitar hero of Slipknot is Jim Root
```
without the argument -v the result is as fallow:

```
Slipknot:Jim Root
```

## test:
to check the correct  creation of the csv file the test_csv in test folder was used the result of the test was as fallow:

```
~/guitarists$ python3 -m unittest -v -b test_csv.py
test_empty_datafile (test_csv.TestMain)
Check the presence of data inside the csv file. ... ok
test_no_datafile (test_csv.TestMain)
Check if there is a csv file. ... ok
test_valid_extension (test_csv.TestMain)
Check the extension of the file. ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.005s

OK
```
## Author:
Sayna Eghbalpour

## License:
http://www.apache.org/licenses/

