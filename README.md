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

## Launching the Program
Set the FLASK_APP and FLASK_CONFIG variables as follows:

* `export FLASK_APP=run.py`
* `export FLASK_CONFIG=development`

You can now run the app with the following command: `flask run`