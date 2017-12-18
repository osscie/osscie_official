# Welcome to [Osscie](https://www.google.com) ("oh-see")

This is the Open-Source, Social, Community-Inspired Experiment. Our goal is to create a website under constant improvement, a product of community driven development and democratic choices. Osscie will always be running the code found here, and you can modify it however and whenever you want. Here's how it works:

* Any user can make changes, improvements, or additions to the Osscie code.
* The Osscie community votes on the adoption of the new changes.
* If users vote in favor of the change, that code will become the newest version of the website.

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
Clone or Download the latest code (the big green one above), or use your local git commands:

```
git clone https://github.com/osscie/osscie_official.git
```

Make sure you have the latest version checked out!
```
git update
```
### Set up the Development Environment
* Install the latest version of Python 3. [https://www.python.org/downloads/]
* Install pip. 


### Make Smart Changes
The goal of Osscie is to make the process of making new changes completely independent of the need for an admin, but that only works if everyone follows some basic rules. Remember the community votes on these changes, so make it easy to review, and make changes everyone would like to see.

**Rules:**

* _Commit changes in small, manageable, chunks. Osscie may seem bare-bones, and thats ok! It's meant to be developed over time by other users. Add an app, change the color scheme, update fonts, or fix an error, but don't do it all in one commit!_

* _Don't change the databse settings or anything that requires modifying environment variables! Your changes will be updated on the server, and then we will run "migrate" then "runserver". If you need the server to do anything else, then your changes won't work!_

* _Keep it clean, nothing inappropriate or explicit._

* _Test, Test, Test! (Then Test again)! Make sure your code works, all of it. Testing is the least fun part of development, but it's the most important. When you upload your changes, everything goes through rigorous testing before the community can even begin to review it, so make sure you write tests and write clean code._


### Upload Your Changes
Make a pull request, it's as simple as that. Your code will be run through a test script, and if it passes, you can find your changes [here](https://www.google.com).
**_Note: Your pull request will be ignored if your github account isn't linked to your Osscie. We want invested Osscie community members to make changes, not randos._**

#### Travis CI
Travis CI is the continuous integration software that tests your pull-request to make sure everything is going to work out if your changes are implemented. Here's what Travis does to ensure every pull-request is vetted properly:

* **Pytest:** all tests must pass.
* **Pylint:** the code must score greater than 9.0.
* **Coveralls:** the package has to be tested well. Write tests when you add code!

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
