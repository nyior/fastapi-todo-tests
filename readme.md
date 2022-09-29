Learn how to setup a CI/CD Pipeline with FastAPI, AWS, and Semaphore in this tutorial :)


# Running this project

- Run `python3 -m venv env-name` on Unix and macOS or `python -m venv env-name` on Windows to create a virtual environment. Replace `env-name` with whatever name you chose for your virtual environment.
- Run `source env-name/bin/activate` on Unix and macOS or `.\env-name\Scripts\activate` on Windows to activate the virtual environment.
- Run `pip install -r requirements.txt` to install project dependencies
- Navigate into your project's root directory in the terminal and run `pytest` to run the test cases


# Accessing the documentation page

- Run `uvicorn app.main:app --reload` to fire up your development server.
- Point your browser to `localhost:8000/docs` to test things out in your browser
