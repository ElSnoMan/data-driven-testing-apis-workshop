# Data-Driven Testing with APIs Workshop

> Please contact me if you'd like me to present this Workshop at your Conference or with your group.
> Twitter: @CarlosKidman

## Setup Project

I am using `pipenv` as my Package Manager and you should too. This manages your Virtual Environments and tracks your packages and dependencies within the Project as well.

```bash
pip install pipenv
```

1. Clone or Fork this repo

    ```bash
    git clone https://github.com/ElSnoMan/data-driven-testing-apis-workshop.git
    ```

2. Install the dependencies (from Pipfile)

    * [Pylenium](https://elsnoman.gitbook.io/pylenium/) - Selenium wrapper by Carlos Kidman
    * [FastAPI](https://fastapi.tiangolo.com/) - Amazing API Builder for Python by @tiangolo
    * [Uvicorn](https://www.uvicorn.org/) - Powerful and lightweight Web Server

    ```bash
    pipenv install
    ```

3. Configure your IDE to use Pytest as the Testing Framework

    You can follow this doc (start at Step 3) if you need help:
    https://elsnoman.gitbook.io/pylenium/getting-started/setup-pytest
    

## Spin up Uvicorn

This project is using FastAPI along with a Uvicorn Web Server. FastAPI is awesome and I highly recommend you check it out:
https://fastapi.tiangolo.com/
 
1. Spin up the Uvicorn Web Server

    ```bash
    uvicorn app.main:app --reload
    ```
2. Then you can view the API docs by visiting http://127.0.0.1:8000/docs


## Run the Tests

Run all Tests
 
```bash
pipenv run pytest
```

Or you can run a subset of them. For example, to run all BookStore UI Tests:

```bash
pipenv run pytest tests/bookstore/ui
```

## Workshop

There is a lot of missing context if all you do is look at the files in here. Going through the Workshop will be a lot more valuable and insightful! Seriously, hit me up if you're interested!
