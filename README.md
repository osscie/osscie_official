# Welcome to [Osscie](https://www.google.com) ("oh-see")

This is the Open-Source Social Continuous-Integration Experiment. Our goal is to make a social website under constant improvement, a product of community driven development and democratic choices. Our website runs the code shown here, and anyone can modify it. Here's how it works:

* Any user can make changes, improvements, or additions to our code (pull-requests).
* The Osscie community discusses and votes on any changes proposed.
* If users vote in favor of a change, it is automatically pushed into the head, and the website is updated.

## Join Osscie

Become a part of the community, join [here](https://www.google.com) for free.


## Want to Make Changes?
### About our Code

Osscie is built using Django, a popular web framework written in Python. Don't know it? That's ok, we picked the one of the easiest web frameworks to learn:

  [Get Started with Django](https://www.djangoproject.com/start/)

### Link Osscie to Github
1. [Sign in](https://github.com/login) to or [Join](https://github.com/join) github for free. 
2. [Link](https://www.google.com) your Osscie profile to your github account.

### Checkout the Code
Clone or Download out latest code (the big green one above), or use your local git commands:

```
git clone https://github.com/osscie/osscie_official.git
```

Make sure you have the latest version checked out!
```
git update
```
### Set up the Development Environment
*Install the latest version of Python 3. [https://www.python.org/downloads/]()
*Install pip. 


### Make Smart Changes
The goal of Osscie is to make the process of making new changes completely independent of the need for an admin, but that only works if the community follows some basic rules. Remember the community votes on these changes, so make it easy to review, and beneficial for everyone involved.

*Commit changes in small, manageable, chunks. Osscie started as a barebones site with the intent of many additions to come by the community. Add an app, change the color scheme, update fonts, or fix an error, but don't do it all in one commit!

*Don't change the databse settings or anything that requires modifying environment variables! Your changes will be updated on the server, and then we will run "migrate" then "runserver". If you need the server to do anything else, then your changes won't work!

*Keep it clean.

*Test, Test, Test. If your code is broken or poorly written, the community and our testing environment won't let it pass. Make sure your new and improved Osscie website works.


### Upload Your Changes
Make a pull request, it's as simple as that. Your pull request will be ignored if your github account isn't linked to your Osscie. We want invested community members to make changes, not randos.

#### Travis CI
Travis CI is the continuous integration software that builds and your pull-request to make sure everything is going to work out if your changes are implemented. Here's what Travis does to ensure every pull-request is vetted properly:

* Pytest: all tests must pass.
* Pylint: the code must score greater than 9.0.
* Coveralls: the package has to be tested well. Write tests when you add code!

If your pull-request doesn't pass the above criteria, the pull-request won't be voted on to integrate into Osscie.

### Let Democracy Happen
If all is well, the Osscie community can find pull-requests [here](https://www.google.com) and approve or downvote them. If you want your changes to be the new version of Osscie, you must get a majority of all active members within the last two weeks to approve your changes.


## TODO

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **The OSSCIE Team** - *Initial work* - [PurpleBooth](https://github.com/osscie)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Django
