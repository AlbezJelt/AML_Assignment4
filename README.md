# AML_Assignment4
Federico Alberici, matricola 808058

## Requisiti
1. Utilizzare [Poetry](https://python-poetry.org/docs/) per creare un nuovo ambiente virtuale:
    ```shell
    $ poetry shell
    ```
2. Installare tutte le dipendenze necessarie:
    ```shell
    $ poetry install
    ```
Oppure fare riferimento al file *requirements.txt*

## Dataset
Il dataset utilizzato è reperibile al seguente link: https://data.mendeley.com/datasets/4drtyfjtfy/1
Ajayi, Gbeminiyi (2018), “Multi-class Weather Dataset for Image Classification”, Mendeley Data, V1, doi: 10.17632/4drtyfjtfy.1

Il dataset contiene 1125 immagini rappresentanti condizioni atmosferiche, classificabili in 4 classi: *[cloudy, rain, shine, sunrise]*.

## Pipeline
Il flusso di lavoro si suddivide nei tre notebook nella repository. 
1. **extraction.ipynb**
Fase di preprocessing in cui il dataset viene codificato utilizzando tre diversi "tagli" di VGG16 allenata su imagenet.
2. **training.ipynb**
Per ciascun dataset preprocessato viene definito e allenato un classificatore XGBoost (https://xgboost.readthedocs.io/en/latest/).
3. **evaluation.ipynb**
Viene valutata accuracy per ogni modello rispetto a train/validation/test set.

Dettagli implementativi e descrizioni approfondite sono presenti all'interno dei notebook stessi. 