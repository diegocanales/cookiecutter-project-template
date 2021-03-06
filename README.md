# Cookiecutter Data Science

A logical, reasonably standardized, but flexible project structure for doing and sharing data science work.

## [Project homepage](http://drivendata.github.io/cookiecutter-data-science/)

### Requirements to use the cookiecutter template

- Python 3.6+
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
pip install cookiecutter
```

or

``` bash
conda install -c conda-forge cookiecutter
```

### To start a new project, run

```bash
cookiecutter https://github.com/diegocanales/cookiecutter-project-template.git
```

### The resulting directory structure

The directory structure of your new project looks like this:

```text
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── examples       <- Few data examples to try the inference model without download the entire dataset.
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- Extra file for docs
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │   ├── train          <- Intermediate models training files
    │   ├── metrics        <- Trained models metrics files
    │   ├── compiled       <- Compiled/binary model files
    │   └── quantized      <- Quantized model files
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── Dockerfile         <- Dockerfile for development/production
```

## Contributing

We welcome contributions! [See the docs for guidelines](https://drivendata.github.io/cookiecutter-data-science/#contributing).

## Installing development requirements

```bash
pip install -r requirements.txt
```

## Running the tests

```bash
py.test tests
```
