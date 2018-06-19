# News-Highlight
The News Highlight App allows a user to view news highlights from various sources and articles

**By Immanuel Mugambi**

## Description
News Highlight is a web application that displays a list of news sources from around the world. A user is able to go the source page to view the news sources and onwards views articles of that news source. The application makes use of the the news api, a free api that allows one to fetch api data.

## Behaviour of the application
+ The user visits the app url in any browser and interacts with the application
+ The user can view the news sources and click on the news sources to view the news articles

## Development and SetUp
### Development cycle of the app
+ First install and setup the virtual environment.
``` pip3 install virtualenv
    virtualenv <name of the environment>
    source <name of virtualenv>/bin/activate

```
+ Once the environment has been activated, the additional packages can be installed using pip3.
```example
   pip3 install flask
```
+ A requirements file can be created by running this command.
```pip3 freeze -> requirements.txt```
Then afterwards, packages can be installed by running this commmand
```pip3 install -r requirements.txt```
+ Then setup the structure of the flask application,so that the flask application becomes a package, and not a single file application.
+ Then visit the news site and generate an API key.
+ Then set the SECRET_KEY and API_KEY in the environs of the virtual environment.
``` run these commands on the terminal
    (virtual)</path/to/project/$export SECRET_KEY="<the secret key"
    (virtual)</path/to/project/$export API_KEY="<the api key"
```
+ Then create tests for the classes.
+ To run tests run this command
```pip3 manager.py test```
+ To start the app, run this code on the terminal
```(virtual) <path>$./start.sh ```
+ Then open the browser at the specified url.
``` example
localhost:5000 
```


## Technology Used
Python3.5

## Test Driven Development
Testing was done using python inbuild test tool called **unittest**

## Known Bugs
No known bugs.

## Further help
To get Further help you can visit the official [python](https://www.python.org/) and [flask](http://flask.pocoo.org/ ) documentation.

## License 
This project is licensed under the MIT Open Source license, (c) **Immanuel Mugambi**

