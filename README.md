[![Build Status](https://travis-ci.org/machariamarigi/shopping_list.svg?branch=master)](https://travis-ci.org/machariamarigi/shopping_list) [![Coverage Status](https://coveralls.io/repos/github/machariamarigi/shopping_list/badge.svg?branch=ch-tdd-setup)](https://coveralls.io/github/machariamarigi/shopping_list?branch=ch-tdd-setup)

# Shopping List

The innovative Shopping list app is an application that allows users to record and share things they want to spend money on meeting the needs of keeping track of their shopping lists.

## Intallation

1. Clone this repo into any directory in your machine

2. Ensure you have `python 3.5` and `virualenv` installed in your machine

3. Create a virtual environment for the project and activate it:
    ```
    virtualenv env
    source env/bin/activate
    ```

4. Enter the app directory
    ```
    cd shopping_list
    ```

5. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

## Testing the application
Run the following command for tests and coverage:

* `coverage run --source=app -m py.test && coverage report`
    

## Launching the Program
Set the FLASK_APP and FLASK_CONFIG variables as follows:

* `export FLASK_APP=run.py`
* `export FLASK_CONFIG=development`

You can now run the app with the following command: `flask run`

## Authors
[Macharia Marigi](https://github.com/machariamarigi)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
* Various resources on the Internet
