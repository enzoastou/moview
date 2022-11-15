# moview
Final work in API section of Data Sources class in EPF Montpellier. Started on the 15th of november 2022 by Driss Bensaid and Enzo Fragale.



# Final Work

To sum up all the knowledge learnt in this course, i want you to create a package in order to easily work with an API, following all the best practices seen.

If you have any questions, do not hesitate to contact me.


## Context

You want to build a service that will be easily be pluggable to a message app, an email app, or other in order to integrate Movie ratings. (like Giphy, but for Movies)

You're on the road to create yout first MVP, but as you only want (for the moment) to spend time on the service, you decide to delegate the movies information for the moment.

You find the following API that could satisfy your needs for movies information:

https://imdb-api.com/API

You're now ready to start your business !

## Roadmap

You should be able, through you app, to search a movie by name and get its review !

What are the keys for easily reach you objective ?
- What data should i want for my final Python object ? (and so for the final user)
- What level of data the api provide ?
- How my package should work ? (definition, parameters, call, ...)

## Expectations

Using the knowledge and the best practices seen in this course, i want you to create a movie package that will be used to generate Movie(s) as a Python Object.

The rating will consider :
- The quality of the code (Pep8 conventions)
- The global modules and packages structure
- The correct behavior of your code
- The correct usage of a versionning system (git for example on github or gitlab)

If you feel comfy with the previous points, you can also try to :
- Implement a UI for your package
- Writing tests to your current package (using pytest for example)
https://docs.pytest.org/en/6.2.x/
- Create a private package for your project (usable with pip for example)
- Use CI/CD tools like github actions


## Deliverable

You will send me link to the repositorie of your project (host on github, gitlab, ...) with a detailed README in order show me how to install and launch your application.

Your application could just be a "main.py"

I will also value :
- A small video teaser for your project
- A recorderd demo
- A recorded ppt presentation (like i was a investor for your app)
- Anything that will present your work from a business point of view instead of a technical one.

## Submission

As discuss with you, you'll have 2 weeks to submit your job from the last Practical course :

- DE : Before sunday 13/11 at 23h59
- DS1 & DS2 : Before sunday 04/12 at 23h59

I expecte a link to your private (or not) repository, if it's private, do not forget to add me as reviewer:
https://github.com/Clement-Roque


## Tips

As you will be limited by the number of request you can make on the api, save a dump of a response in order to use it "offline" as seen in the first Notebook.

Do not store your key directly in your code, use .env variable instead

## Other ressources

Here is a collection of usefull link for python programmer :

https://docs.python-guide.org/

https://www.python.org/dev/peps/pep-0020/

https://pep8.org/