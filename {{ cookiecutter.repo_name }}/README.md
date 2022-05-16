# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Getting Started

### Project Organization

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
    ├── {{ cookiecutter.package_name }}   <- Source code for use in this project.
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
    ├── .here              <- pyprojroot's file to find the root working directory for your project
    │                         as a pathlib object and easily manage data paths.
    └── Dockerfile         <- Dockerfile
```

### Environment

1. [Install](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) and activate Conda.
2. Create the conda development environment:

    ```bash
    conda env create -f environment.yaml
    ```

3. Activate the conda environment:

    ```bash
    conda activate {{ cookiecutter.conda_env }}
    ```

<p><small>Project based on the <a target="_blank" href="https://github.com/diegocanales/cookiecutter-project-template/">cookiecutter project template</a>. #cookiecutterdatascience</small></p>
