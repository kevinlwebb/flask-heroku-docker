# Flask Docker Template

This application utilizes a few tutorials:
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Stripe SDK Tutorial](https://testdriven.io/blog/flask-stripe-tutorial/)

## Want to use this project?

1. Fork/Clone

1. Create and activate a virtual environment:

    ```sh
    $ python3 -m venv flaskdemo && source flaskdemo/bin/activate
    ```

1. Install the requirements:

    ```sh
    (flaskdemo)$ pip3 install -r requirements.txt
    ```

1. Run the server:

    ```sh
    (flaskdemo)$ gunicorn start:app
    ```

    Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
