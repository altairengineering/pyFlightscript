## pyFlightscript
!Compatible with FlightStream 2025.1.

A python API for generating native FlightStream scripts.
This is an open source project, but is sponsored in part by Altair. Development is on-going.

pyFlightscript contains all of the traditional scripting functions found in FlightStream. The functions are nested within
submodules categorized by function. for example `pyFlighscript.initialize_solver() `


## [Full Documentation is available here.](https://altairengineering.github.io/pyFlightscript/)

## Installation
Download the repo
`git clone https://github.com/altairengineering/pyFlightscript.git`
NOTE: you may have to install git first.

Install dependencies. 
`pip install -r requirements.txt`

Simply download the repo and install with within the directory:

`pip install .`

Can also install directly from the git repo:
`pip install git+https://github.com/altairengineering/pyFlightscript.git`

## Features

- Generates FlightStream scripts with a user-friendly Pythonic interface
- Modules broken into categories for ease of search.

## Example code

See example code folder for more detailed examples.
The general flow for a pyFlightscript based script is:

```
   import pyFlightscript as pyfs

   fsexe_path = r'C:\filepath\FlightStream.exe' #specify file path to FS exe
   pyfs.script.hard_reset() # (optional) clear lines from local memory, delete existing script.txt

    ### Enter FlightStream macro commands ###
    ### Example code ####
    pyfs.open_fsm(fsm_filepath=f)
    pyfs.close_flightstream
    ################################

    # all macro commands done
    pyfs.write_to_file() # now write script_out.txt
    # execute the script in headless mode
    pyfs.execute_fsm_script(fsexe_path=fsexe_path, hidden=True) 
    pyfs.display_lines()
    # clear the lines from local memory and delete the script.txt file
    pyfs.hard_reset()  

```


### on Windows

within \sphinx directory
simply run `generate_docs.bat` in a cmd terminal

### on other systems

within \sphinx directory
remove \_build directory
run 'sphinx-apidoc -o . ../pyFlightscript/'
rename pyFlighscript.rst to index.rst
run 'make.bat html'
docs are in '.\_build\html\index.html'

## Contribution

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
    - Ensure any function changes are properly documented in the code. 
    - Create a new test if applicable.
4. Submit a pull request.

Please post bugs to the 'issues' section. Feel free to create a branch and submit a pull request. An admin will be notified.

## License

GNU AFFERO GENERAL PUBLIC LICENSE
