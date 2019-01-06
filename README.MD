# Billy Booksearch

Search the Google Books API using Python 📚🐍
Named after the world's most recognisable bookcase 🇸🇪

## Installation

[You can view the site on Heroku](https://billybooksearch.herokuapp.com/) or follow the below (I recommend [pyenv](https://github.com/pyenv/pyenv) for Python virtualenv management and version management, but you can replace with an alternate solution if you prefer) for a local installation:

Here's the steps to get pyenv up and running on a Ubuntu distribution with Bash:

```bash
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
$ git clone https://github.com/pyenv/pyenv-virtualenv.git $HOME/.pyenv/plugins/pyenv-virtualenv
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
$ exec "$SHELL"
```

And the app itself:

```bash
$ git clone https://github.com/martingaston/billy-search.git
$ pyenv install 3.7.1
$ pyenv virtualenv 3.7.1 billy-search
$ cd billy-search
$ pyenv local billy-search
$ pip install -r requirements.txt
$ pip install -e . # let the app be used as a Python module (useful for testing)
$ pytest # for tests
$ flask run
```

## User Stories

1. As someone visiting the site, I should be able to type in a query and display a list of books matching that query.
2. As someone who has searched for a book, I should get a list of books with each item in the list including:

- The book's author
- The book's title
- The book's publishing company
- A picture of the book.

3. As someone who is searching for a book, each item in the list should have allow you to navigate to additional information about the book.

## The Stack

- Python 3.7.1
- Flask 1.0.2
- Pytest 4.0.1
- [Tachyons](https://tachyons.io/) 4.10
- And, of course, [the Google Books API](https://developers.google.com/books/)

## Considerations & Assumptions

- Previous/Next buttons weren't part of the original user journey - but I decided to add them in as I saw this as a natural extension of the 'list of books' format. Originally I calculated the total number of books from the API's `totalItems` response for pagination, but after reading the [Google Product Forums](https://productforums.google.com/d/msg/books-api/Y_uEJhohJCc/laWnDMgotN8J) I saw that this would not be able to achieve that. I originally sent data with a `POST` request too, but refactored to `GET` as it made introducting pagination and features like the `placeholder` search term bar at the top of the `search.html`.
- I chose to render the app with the `Jinja2` templating engine in conjunction with `Flask` as I felt they combined to make an effective system to effectively spin up a project catering towards these user stories - I would reserve something like, say, `Django` for a more feature-rich application. I opted to use the frameworks as the extra level of abstraction would allow me to focus on the parts of the application rather than the density of the syntax, although in the past I have created HTTP servers from scratch in other languages (notably `Node`) to get a real sense of the fundementals of the protocol.
- It would have been possible to simply use the `requests` library to forward the entire JSON response to the templating engine, however I wanted to setup some helper functions - `google_book_search()` and `parse_search()` - for a few reasons. Firstly, I wanted to have more control over the data that was being sent to the templating engine - making sure it existed, for example, or that it always had an image for the book cover - which required ensuring that the data would always be cleaned before going to the template. I also wanted to make sure that only necessary data was being sent around the application, and by decoupling the code into various helper functions they remained small, readable and testable.
- I used `Pytest` as my test runner as I find the syntax straightforward and readable, which is really handy for building up functions using TDD.
- I used `Tachyons` for the CSS on the frontend, which can an atomic CSS framework that's a little challenging to read for people to read if they've not come across it before. The idea is that it links the CSS closer to the HTML by creating small, reusable single-purpose classes. I wanted something that was small, readable and allowed for an effective mobile-first/responsive design.
- I wanted to keep the code closely aligned with the intended user stories, using the YAGNI and DRY principles to create an application that was a simple as it needed to be.
- I considered a mobile-first design something to design for from the ground up - this wasn't an explicit user story, however I would argue it is likely best practice in most instances.

## Refactoring & Feedback

- Structure the project in a way that can support better testing and future potential growth. I followed the [recommended approach by the Flask](http://flask.pocoo.org/docs/1.0/patterns/appfactories/) framework for restructuring the project, which should allow the code to be more easily digested for users of the framework.
- Abstract the various `parse` functions from the API call into their own class.
- Follow the single responsibility principle and separate the `helpers` function into individual files that serve individual purposes. These now sit in a `utils` folder and are clearly named as to their purpose.
- Fix the HTTP mixed content warning on thumbnail images - Heroku defaults to `https` but the API returned `http` images by default. I had the app redirect `http` users to `https` by default and used a function to adjust images to `https`.
- Look into adding integration tests to the `pytest` tests. I have created some simple integration tests which check that the various components of the layout are correctly rendering by ID.
- Consider the amount of comments being used and look into creating self-documenting code by focusing on sharp function and variable naming along with readable code.
- See how you can use Tachyons (an atomic CSS framework) to continue the theme of coding by intention. This was a little tricky due to the explicit nature of the framework, but I looked to create consistency across the `class` definitions (e.g. starting with high-level flex/layout classes first and then progressing down through to individual fonts)
- Ensure the structure of the Python `import`s maintained consistency across the whole project. I couldn't find consensus on this outside of a PEP recommendation to keep imports at the top of a file, so my imports start with direct `imports` and then `import from` below.
- Add detailed instructions to install the project and run the tests, for anyone who might not be totally familiar with the tooling used in this project.

## Wishlist

- The next steps for the project, in my opinion, would be to create a `page.html` template that gives more in-depth information about the book when selected from the search results - such as various retailers and links out to Wikipedia and other resources so that users can get a more holistic view of the books. Currently the app is tied closely into Google's ecosystem, and while there's nothing wrong with that it would be nice to be able to offer up a few alternatives. I chose not to include this at this stage as I felt it was straying too far from the initial user stories, although it would certainly be a nice to have feature in a subsequent sprint.
- A nice UX feature to add would be to replace the pagination with the site auto-loading the next 20 items when the user scrolls to the bottom of the page. This would likely require incorporating some code on the front-end and exposing an API endpoint on the server to feed the code in with a JavaScript `fetch()` request.
- The bookshelf icon was [lovingly made by Freepik](https://www.flaticon.com/free-icon/bookcase_677239#term=bookshelf&page=1&position=91) but with more time and resource I'd love to work with a designer to create my own icon.

Thanks for reading & I hope you enjoy the app!
