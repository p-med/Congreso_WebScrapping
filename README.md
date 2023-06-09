# Bills production and development of paraguayan congressmen

This project aims to make the data of bills or initiatives proposed by the congressmen or congresswomen of Paraguay more accessible and transparent. The data can help to evaluate and hold accountable the performance of the legislators.

The data is scraped from the official Congress API, which provides information about the projects, content, and authors of each bill. The use of this data is fair and the code is free for anyone to use, improve, or modify.

**Source: https://datos.congreso.gov.py/opendata/datos**

This project consists of a Python script that scrapes the data of bills or initiatives of the senators and deputies of Paraguay from the official website of the National Congress of Paraguay. The script uses the requests and pandas modules to make HTTP requests to the API and process the JSON data. The script outputs a CSV file with the following columns:

| Column                | Description                                                                                                                                              | Data type |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| apellidos             | Surname/s of the Senator/Deputy                                                                                                                          | string    |
| appURL                | url of the parliamentarian in the SILpy according to the corresponding Chamber                                                                           | string    |
| bancada               | Party block to which the parliamentarian belongs                                                                                                         | string    |
| camaraParlamentario   | The Chamber to which the parliamentarian belongs                                                                                                         | string    |
| cargoBancada          | Position he occupies within the party bloc                                                                                                               | string    |
| departamento          | Region that he represents in the cases of the Chamber of Deputies. In the cases of the Chamber of Senators, it is null, since it is a national election. | string    |
| emailParlamentario    | Institutional email that corresponds to each parliamentarian                                                                                             | string    |
| fotoURL               | url of the SILpy of the photo of the parliamentarian                                                                                                     | string    |
| idParlamentario       | Parliamentarian ID                                                                                                                                       | integer   |
| nombres               | Name/s of the Senator/Deputy                                                                                                                             | string    |
| partidoPolitico       | Acronym of the political party to which the parliamentarian belongs                                                                                      | string    |
| periodoLegislativo    | Constitutional period of 5 years to which the parliamentarian was elected                                                                                | string    |
| telefonoParlamentario | Legislative office phone number                                                                                                                          | string    |
| tipoParlamentario     | Quality in which the parliamentarian was elected                                                                                                         | string    |
| idProyecto            | The unique identifier of the proyecto.                                                                                                                   | string    |
| iniciativa            | The authors and if it was initiated by congress or the executive branch.                                                                                 | string    |

### How to use

To use this script, you need to have Python 3 installed on your computer. You also need to install the requests and pandas modules using pip or another package manager. You can run the script from your terminal or command prompt by typing:

`python data_scraping.py`

The script will take some time to scrape the data and save it to a CSV file named congresistas_proyectos.csv in the same directory as the script.

### Requirements and dependencies

This script requires Python 3 and the following modules:

| Module   | Description                                                                   |
| -------- | ----------------------------------------------------------------------------- |
| requests | A module that allows you to make HTTP requests in Python.                     |
| pandas   | A module that provides data structures and tools for data analysis in Python. |
| json     | A standard module that can encode and decode JSON data.                       |

**You can install these modules using pip or another package manager.**

**For example, you can type:**

`pip install requests pandas`

in your terminal or command prompt.

License
This project is licensed under the MIT License - see the LICENSE file for details.
