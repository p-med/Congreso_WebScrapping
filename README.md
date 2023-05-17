# Bill's production and development of paraguayan congressmen

The idea behind this is to make the projects, content and authors data more available and to improve over accountability when it comes to judge paraguyan congressmen.


This project is a Python script that scrapes the data of proyectos (bills or initiatives) of parlamentarios (congressmen or congresswomen) of Paraguay from the official website of the Congreso Nacional de Paraguay (National Congress of Paraguay). The script uses the requests and pandas modules to make HTTP requests to the API and process the JSON data. The script outputs a CSV file with the following columns:

idParlamentario: The unique identifier of the parlamentario.
nombre: The full name of the parlamentario.

Column  | Description
------------- | -------------
idProyecto  | The unique identifier of the proyecto.
iniciativa  | The authors and if it was initiated by congress or the executive branch.


### How to use
To use this script, you need to have Python 3 installed on your computer. You also need to install the requests and pandas modules using pip or another package manager. You can run the script from your terminal or command prompt by typing:

python prueba4.py

The script will take some time to scrape the data and save it to a CSV file named prueba4.csv in the same directory as the script.

Requirements and dependencies
This script requires Python 3 and the following modules:

requests: A module that allows you to make HTTP requests in Python.
pandas: A module that provides data structures and tools for data analysis in Python.
json: A standard module that can encode and decode JSON data.
You can install these modules using pip or another package manager. For example, you can type:

pip install requests pandas

in your terminal or command prompt.

License
This project is licensed under the MIT License - see the LICENSE file for details.

I hope this helps. 😊
