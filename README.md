## Ploutizo is a script created to help enrich data using `Apollo.io`'s database. 

## Installation: 

Clone the Femto-0/ploutizo repo to your computer
`git clone https://github.com/Femto-0/ploutizo.git`
<br>Follow the steps below to set up the script and get it running

## Requirements to run Ploutizo on your computer

  1. Python
     - To check if you have python in your computer, run: `python3 --version` in your terminal. If python's already installed on your computer, you will get your python's version as the response.
       If not, install the latest version of python.
  2. Ollama
     - Install `Ollama` in your computer since the script makes an API call to Llama 3.2 running locally on your computer via. Ollama.
     - You can either go to: `https://ollama.com/download` to download Ollama if you are running Windows, MacOS or Lunix OR run `curl -fsSL https://ollama.com/install.sh | sh` in your terminal if you are running Linux.

  ## How to set up Ploutizo:  

  1. Ploutizo makes use of an `env` variable to store applo's api-key. So, you will need to set an `APOLLO_API` env variable.
     - To set an env variable: add `export APOLLO_API=<yourAPIkey>` to either your `.bashrc` or `.zshrc`, whichever you are using.
    
  2. To make sure that Ollama was installed, run `ollama` and see if you get a bunch of commands listed.
     - If yes, Ollma was installed successfully. Now, run `ollama run llama`, wait until you see the model is downloaded. After the model is downloaded, we have two options:
       a. Leave it running in the background. This is suggested if you plan on enriching a lot of data since it improves the script's speed by few seconds.
       b. If you aren't going to be using Ploutizo actively, you can stop running the model. Run `ollama stop llama` to do so. To make sure, run `ollama ps` and see if any model is listed.
       
  3. Plutizo also makes use of python virtual environment:
     - To enable virtual environment for plutizo directory.
       i. go to `plutizo` directory.
       ii. run `python3 -m venv .venv` to initialize the virtual environment for this directory.
       iii. run `source .venv/bin/activate` to activate the virtual envrionment.

  4. Installing all the required libraries to run the script
     - A requirements.txt files is procvided.
     - Run `pip install -r requirements.txt`. This will install all the required libraries.
       
  5. Running the script:
     - As of version 1.0.0:
       i. Users need to assign the name of the image file manually to `image` variable in [main.py](https://github.com/Femto-0/ploutizo/blob/master/source/main.py) everytime they want to run the script for an image.
       ii. Make sure your image file is a ".PNG" image file.
       iii. Make sure your image is inside the `images` folder. `images` folder can be found in `ploutizo/source/`
       iv. After all the requirements are met, go to the `source` folder and run `python3 main.py`.
       
  6. Output:
     - As of version 1.0.0:
       i. A `json` and a `xlsx` file is created as ouput and placed in the `enrochedData` folder. `enrichedData` folder can be found in `ploutizo/source/`.

## Issues: 

Feel free to open an [issue](https://github.com/Femto-0/ploutizo/issues) if you find any bug or if the README is missing any important detail. 
