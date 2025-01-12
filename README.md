Fork - 
A simple command line interface with navigation options and text-file output was created to increase efficiency via simple terminal usage. To use the simple CLI, simply download the repository and open the terminal (within the folder, or navigate to it), then run:

$ pip install tensorflow pystow rdkit
and/or 
$ pip install -r Python_requirements.txt

and then: 

$ python3 Simple_Cli.py
or
$ python Simple_Cli.py

Simply follow the prompts; if text file output was selected, the text file will be created within the main project folder. The script will output all translations, separated by comma, and with a space. You can easily edit the output to suit your needs or parse the list with simple scripts. 

[![License](https://img.shields.io/badge/License-MIT%202.0-blue.svg)](https://opensource.org/licenses/MIt)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-blue.svg)](https://github.com/Kohulan/Smiles-TO-iUpac-Translator/graphs/commit-activity)
![Workflow](https://github.com/Kohulan/Smiles-TO-iUpac-Translator/actions/workflows/ci_pytest.yml/badge.svg)
[![GitHub issues](https://img.shields.io/github/issues/Kohulan/Smiles-TO-iUpac-Translator.svg)](https://GitHub.com/Kohulan/Smiles-TO-iUpac-Translator/issues/)
[![GitHub contributors](https://img.shields.io/github/contributors/Kohulan/Smiles-TO-iUpac-Translator.svg)](https://GitHub.com/Kohulan/Smiles-TO-iUpac-Translator/graphs/contributors/)
[![GitHub release](https://img.shields.io/github/release/Kohulan/Smiles-TO-iUpac-Translator.svg)](https://GitHub.com/Kohulan/Smiles-TO-iUpac-Translator/releases/)
[![PyPI version fury.io](https://badge.fury.io/py/STOUT-pypi.svg)](https://pypi.org/project/STOUT-pypi/2.0.0/)
![versions](https://img.shields.io/pypi/pyversions/STOUT-pypi.svg)

![GitHub Logo](https://github.com/Kohulan/Smiles-TO-iUpac-Translator/blob/stout-1/important_assets/STOUT.png?raw=true)

# STOUT V2.0 - Smiles TO iUpac Translator Version 2.0
This repository contains STOUT-V2, SMILES to IUPAC name translator using transformers. STOUT-V2 can translate SMILES to IUPAC names and IUPAC names back to a valid SMILES string. STOUT-V1 is already published and for more details check [here](https://github.com/Kohulan/Smiles-TO-iUpac-Translator)

#### OS-Support: Linux, MACOS and Windows (On Windows you can run STOUT inside the Ubuntu shell). But It is highly recommended to use a Linux system.

# Usage

### We suggest to use STOUT inside a Conda environment, which makes the dependencies to install easily.
- Conda can be downloaded as part of the [Anaconda](https://www.anaconda.com/) or the [Miniconda](https://conda.io/en/latest/miniconda.html) plattforms (Python 3.7). We recommend to install miniconda3. Using Linux you can get it with:
```shell
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ bash Miniconda3-latest-Linux-x86_64.sh
```
## How to install STOUT

```shell
$ sudo apt update
$ sudo apt install unzip
$ conda create --name STOUT python=3.8.0
$ conda activate STOUT
$ conda install pip
$ python -m pip install -U pip
$ pip install git+https://github.com/Kohulan/Smiles-TO-iUpac-Translator.git
```

## Py-Pi installation instructions coming soon,
```shell
pip install STOUT-pypi==2.0.1
```


## Simple usage
```python3

from STOUT import translate_forward, translate_reverse

# SMILES to IUPAC name translation

SMILES = "CN1C=NC2=C1C(=O)N(C(=O)N2C)C"
IUPAC_name = translate_forward(SMILES)
print("IUPAC name of "+SMILES+" is: "+IUPAC_name)

# IUPAC name to SMILES translation

IUPAC_name = "1,3,7-trimethylpurine-2,6-dione"
SMILES = translate_reverse(IUPAC_name)
print("SMILES of "+IUPAC_name+" is: "+SMILES)

```

#### Happy Brewing... 🍺

## How to cite us?

Rajan, K., Zielesny, A. & Steinbeck, C. STOUT: SMILES to IUPAC names using neural machine translation. J Cheminform 13, 34 (2021). https://doi.org/10.1186/s13321-021-00512-4


# STOUT-V2 is part of DECIMER project
[![GitHub Logo](https://github.com/Kohulan/DECIMER-Image-to-SMILES/raw/master/assets/DECIMER.gif)](https://decimer.ai)

# More about Us

[![GitHub Logo](https://github.com/Kohulan/DECIMER-Image-to-SMILES/blob/master/assets/CheminfGit.png?raw=true)](https://cheminf.uni-jena.de)

![Alt](https://repobeats.axiom.co/api/embed/c66cc0ff5bc3ae91ccc8a3f7ed20eb05c735d753.svg "Repobeats analytics image")
