## Data Science Template Project Folder Structure
```
├── LICENSE
├── README.md          <- The top-level README for developers using this project.
├── requirements.txt   <- Running environment settings.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── saved              <- Trained and serialized models, model predictions, or train logs
│   ├── models         
│   └── logs           
│
├── notebooks          <- Jupyter notebooks. 
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── test           <- Scripts to do unit test
│   │
│   ├── datasets       <- Scripts about data loading
│   │   ├── cifar10.py
│   │   └── mnist.py
│   │
│   ├── graph          <- Scripts to define computation graphs
│   │   ├── models   
│   │   │   ├── layers
│   │   │   │   ├── denseblock.py
│   │   │   │   └── residual.py
│   │   │   │
│   │   │   └── example_model.py
│   │   │
│   │   └── losses
│   │       ├── loss.py
│   │       └── metric.py
│   │
│   ├── utils          <- small utility functions
│   │
│   ├── experiment     <- Scripts to train models and then use trained models to make predictions
│   │   ├── train_landmark.py
│   │   └── train_meta.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── configs            <- config files with settings and hyper-parameters to run experiments ' 
```

