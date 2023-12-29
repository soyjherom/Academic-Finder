Academic Finder by Jherom Chacon

Academic Finder is a simple Web Scrapper designed to search different research Journals in Costa Rica Univerisities to simplify the process of finding white papers for research purposes. 

Motivation

Currently, search for information into the different research journals is a slow process that implies to have multiple browser taps open and provide the search bars of every single one of the journals with the keywords and date ranges to search for a specific topic. Taking into consideration that computer science tends to be a very multi-disciplinary field, is important to be able to search for papers into different journals from a wide range of disciplines.

Search for papers into multiple journals is a very slow and painful process. Due to this, I created this tool to search in multiple journals in one single shot. Also, me as an old school software developer from the early 2000, I enjoy a lot working with tools from the Terminal. So this is a Terminal tool that I tested in a MacOS environment using MyZsh and Bash.

Dependencies

1. pip install requests
2. pip install beautifulsoup4 lxml

Forking development steps

1. Install Homebrew
2. Install python3
3. Install pip3
4. Add pip3 to the path if needed
5. Add python3 to the path if needed
6. run the script using python from the project root folder for testing purposes

Usage:

This is a Terminal tool, so you should call the executable file from Terminal. As an interactive program you should send some parameters for it to be executed correctly. Nevertheless if you found yourself lost somehow, you always can use --help to take a look on the three parameters that this tool uses.

Example:

academic_finder "Artificial Intelligence Applied to Education" --from-year 2020 --to-year 2022

--from-year and --to-year parameters are optional
The search criteria should be added inside of double quotation marks, if not provided the tool is going to show you an error and then close.
