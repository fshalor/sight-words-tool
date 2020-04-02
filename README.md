# Sight Words

## What Is This? 

The concept of sight words in learning is a strong one. I remember flashcards in elementry school, and Spanish classes. Since everyone is stuck at home, things can get less-fun for the little ones. Why not add a teaching tool to our home-schooling process which integrates those sight-word lists with the keyboard and the mouse!

This application pulls a random word from several sight-word lists, and then asks the user to type in that word into a form field. Submit of the form passed the typed word, and the sight word to get checked. If they pass, they get a green light. If the typing isn't correct; they can try again until they choose to move on. 

The choice of making a "get a new word" button as a standard a href link is to support learning about how to click weblinks. 

More features are to come!


## Building the app

This is a simple Python3 + Flask application, which is configured to run as a docker container. 

1. Make sure you have a good docker setup. Don't forget the port mapping bits. 
2. App is set to debug mode. Turn it off if you wish. 
3. Don't forget to change the session key if you actually use it.
4. docker build -t flask-sight-words:1.0 .
5. docker run -d -p 0.0.0.0:5000:5000 --name sightwords flask-sight-words:1.0
6. docker logs $containerid

## Working Demo

To see a running example of this project, send your little ones to https://sight-words.org !


## Future

If this project gains some traction and utility, I may move it to a fargate launch system behind an ALB. (It runs well there, but I'm on a budget!) 


See "issues" for future features and thoughts. Happy Typing. 
