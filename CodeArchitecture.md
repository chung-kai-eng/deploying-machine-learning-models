```
deploying-machine-learning-models
├─ .circleci
│  └─ config.yml
├─ .dockerignore
├─ .git
│  ├─ config
│  ├─ description
│  ├─ FETCH_HEAD
│  ├─ HEAD
│  ├─ hooks
│  │  ├─ applypatch-msg.sample
│  │  ├─ commit-msg.sample
│  │  ├─ fsmonitor-watchman.sample
│  │  ├─ post-update.sample
│  │  ├─ pre-applypatch.sample
│  │  ├─ pre-commit.sample
│  │  ├─ pre-merge-commit.sample
│  │  ├─ pre-push.sample
│  │  ├─ pre-rebase.sample
│  │  ├─ pre-receive.sample
│  │  ├─ prepare-commit-msg.sample
│  │  ├─ push-to-checkout.sample
│  │  └─ update.sample
│  ├─ index
│  ├─ info
│  │  └─ exclude
│  ├─ objects
│  │  ├─ info
│  │  └─ pack
│  │     ├─ pack-db7dcbf0afbd75dc5e451f0c858ba0259168ffd6.idx
│  │     └─ pack-db7dcbf0afbd75dc5e451f0c858ba0259168ffd6.pack
│  ├─ packed-refs
│  └─ refs
│     ├─ heads
│     │  └─ master
│     ├─ remotes
│     │  ├─ origin
│     │  │  └─ HEAD
│     │  └─ upstream
│     │     ├─ 2020-update-pt2
│     │     ├─ api-fix
│     │     ├─ dependabot
│     │     │  └─ pip
│     │     │     ├─ packages
│     │     │     │  └─ neural_network_model
│     │     │     │     ├─ numpy-1.21.0
│     │     │     │     └─ opencv-python-4.2.0.32
│     │     │     └─ section-04-research-and-development
│     │     │        └─ numpy-1.21.0
│     │     ├─ fix-publish-step
│     │     ├─ master
│     │     ├─ section-07
│     │     ├─ section-08
│     │     ├─ section-5.2-initial-setup
│     │     ├─ section-5.3-hook-up-basic-training-pipeline
│     │     ├─ section-6.2-initial-setup
│     │     ├─ section-6.3-connecting-the-pipeline
│     │     ├─ test
│     │     ├─ update
│     │     ├─ update-regression-model
│     │     └─ update-section-09
│     └─ tags
├─ .gitignore
├─ assignment-section-05
│  ├─ classification_model
│  │  ├─ config
│  │  │  ├─ core.py
│  │  │  └─ __init__.py
│  │  ├─ config.yml
│  │  ├─ datasets
│  │  │  └─ __init__.py
│  │  ├─ pipeline.py
│  │  ├─ predict.py
│  │  ├─ processing
│  │  │  ├─ data_manager.py
│  │  │  ├─ features.py
│  │  │  ├─ validation.py
│  │  │  └─ __init__.py
│  │  ├─ trained_models
│  │  │  └─ __init__.py
│  │  ├─ train_pipeline.py
│  │  ├─ VERSION
│  │  └─ __init__.py
│  ├─ mypy.ini
│  ├─ pyproject.toml
│  ├─ README.md
│  ├─ requirements
│  │  ├─ requirements.txt
│  │  └─ test_requirements.txt
│  ├─ setup.py
│  ├─ tests
│  │  ├─ conftest.py
│  │  ├─ test_features.py
│  │  ├─ test_prediction.py
│  │  └─ __init__.py
│  └─ tox.ini
├─ Dockerfile
├─ LICENSE
├─ Makefile
├─ packages
│  ├─ ml_api
│  │  ├─ api
│  │  │  ├─ app.py
│  │  │  ├─ config.py
│  │  │  ├─ controller.py
│  │  │  ├─ validation.py
│  │  │  └─ __init__.py
│  │  ├─ diff_test_requirements.txt
│  │  ├─ requirements.txt
│  │  ├─ run.py
│  │  ├─ run.sh
│  │  ├─ tests
│  │  │  ├─ capture_model_predictions.py
│  │  │  ├─ conftest.py
│  │  │  ├─ differential_tests
│  │  │  │  ├─ test_differential.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ test_controller.py
│  │  │  ├─ test_validation.py
│  │  │  └─ __init__.py
│  │  ├─ tox.ini
│  │  └─ VERSION
│  ├─ neural_network_model
│  │  ├─ config.yml
│  │  ├─ neural_network_model
│  │  │  ├─ config
│  │  │  │  ├─ config.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ datasets
│  │  │  │  ├─ test_data
│  │  │  │  │  ├─ Black-grass
│  │  │  │  │  │  └─ 1.png
│  │  │  │  │  ├─ Charlock
│  │  │  │  │  │  └─ 1.png
│  │  │  │  │  └─ __init__.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ model.py
│  │  │  ├─ pipeline.py
│  │  │  ├─ predict.py
│  │  │  ├─ processing
│  │  │  │  ├─ data_management.py
│  │  │  │  ├─ errors.py
│  │  │  │  ├─ preprocessors.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ trained_models
│  │  │  │  └─ __init__.py
│  │  │  ├─ train_pipeline.py
│  │  │  ├─ VERSION
│  │  │  └─ __init__.py
│  │  ├─ requirements.txt
│  │  ├─ setup.py
│  │  └─ tests
│  │     ├─ conftest.py
│  │     ├─ test_predict.py
│  │     └─ __init__.py
│  └─ regression_model
│     ├─ regression_model
│     │  ├─ config
│     │  │  ├─ config.py
│     │  │  ├─ logging_config.py
│     │  │  └─ __init__.py
│     │  ├─ datasets
│     │  │  └─ __init__.py
│     │  ├─ pipeline.py
│     │  ├─ predict.py
│     │  ├─ processing
│     │  │  ├─ data_management.py
│     │  │  ├─ errors.py
│     │  │  ├─ features.py
│     │  │  ├─ preprocessors.py
│     │  │  ├─ validation.py
│     │  │  └─ __init__.py
│     │  ├─ trained_models
│     │  │  └─ __init__.py
│     │  ├─ train_pipeline.py
│     │  ├─ VERSION
│     │  └─ __init__.py
│     ├─ requirements.txt
│     ├─ setup.py
│     ├─ tests
│     │  ├─ test_predict.py
│     │  └─ __init__.py
│     └─ tox.ini
├─ README.md
├─ scripts
│  ├─ fetch_kaggle_dataset.sh
│  ├─ fetch_kaggle_large_dataset.sh
│  ├─ input_test.json
│  └─ publish_model.sh
├─ section-04-research-and-development
│  ├─ 01-machine-learning-pipeline-data-analysis.ipynb
│  ├─ 02-machine-learning-pipeline-feature-engineering.ipynb
│  ├─ 03-machine-learning-pipeline-feature-selection.ipynb
│  ├─ 04-machine-learning-pipeline-model-training.ipynb
│  ├─ 05-machine-learning-pPipeline-scoring-new-data.ipynb
│  ├─ 06-feature-engineering-with-open-source.ipynb
│  ├─ 07-feature-engineering-pipeline.ipynb
│  ├─ 08-final-machine-learning-pipeline.ipynb
│  ├─ preprocessors.py
│  ├─ preprocessors_bonus.py
│  ├─ requirements.txt
│  └─ titanic-assignment
│     ├─ 01-predicting-survival-titanic-assignement.ipynb
│     ├─ 02-predicting-survival-titanic-solution.ipynb
│     ├─ 03-titanic-survival-pipeline-assignment.ipynb
│     └─ 04-titanic-survival-pipeline-solution.ipynb
├─ section-05-production-model-package
│  ├─ mypy.ini
│  ├─ pyproject.toml
│  ├─ regression_model
│  │  ├─ config
│  │  │  ├─ core.py
│  │  │  └─ __init__.py
│  │  ├─ config.yml
│  │  ├─ datasets
│  │  │  └─ __init__.py
│  │  ├─ pipeline.py
│  │  ├─ predict.py
│  │  ├─ processing
│  │  │  ├─ data_manager.py
│  │  │  ├─ features.py
│  │  │  ├─ validation.py
│  │  │  └─ __init__.py
│  │  ├─ trained_models
│  │  │  └─ __init__.py
│  │  ├─ train_pipeline.py
│  │  ├─ VERSION
│  │  ├─ view_yml_file.py
│  │  └─ __init__.py
│  ├─ requirements
│  │  ├─ requirements.txt
│  │  └─ test_requirements.txt
│  ├─ setup.py
│  ├─ tests
│  │  ├─ conftest.py
│  │  ├─ test_features.py
│  │  ├─ test_prediction.py
│  │  └─ __init__.py
│  └─ tox.ini
├─ section-06-model-serving-api
│  └─ house-prices-api
│     ├─ app
│     │  ├─ api.py
│     │  ├─ config.py
│     │  ├─ main.py
│     │  ├─ schemas
│     │  │  ├─ health.py
│     │  │  ├─ predict.py
│     │  │  └─ __init__.py
│     │  ├─ tests
│     │  │  ├─ conftest.py
│     │  │  ├─ test_api.py
│     │  │  └─ __init__.py
│     │  └─ __init__.py
│     ├─ mypy.ini
│     ├─ Procfile
│     ├─ requirements.txt
│     ├─ runtime.txt
│     ├─ test_requirements.txt
│     └─ tox.ini
├─ section-07-ci-and-publishing
│  ├─ house-prices-api
│  │  ├─ app
│  │  │  ├─ api.py
│  │  │  ├─ config.py
│  │  │  ├─ main.py
│  │  │  ├─ schemas
│  │  │  │  ├─ health.py
│  │  │  │  ├─ predict.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ tests
│  │  │  │  ├─ conftest.py
│  │  │  │  ├─ test_api.py
│  │  │  │  └─ __init__.py
│  │  │  └─ __init__.py
│  │  ├─ mypy.ini
│  │  ├─ Procfile
│  │  ├─ requirements.txt
│  │  ├─ runtime.txt
│  │  ├─ test_requirements.txt
│  │  └─ tox.ini
│  └─ model-package
│     ├─ mypy.ini
│     ├─ publish_model.sh
│     ├─ pyproject.toml
│     ├─ regression_model
│     │  ├─ config
│     │  │  ├─ core.py
│     │  │  └─ __init__.py
│     │  ├─ config.yml
│     │  ├─ datasets
│     │  │  └─ __init__.py
│     │  ├─ pipeline.py
│     │  ├─ predict.py
│     │  ├─ processing
│     │  │  ├─ data_manager.py
│     │  │  ├─ features.py
│     │  │  ├─ validation.py
│     │  │  └─ __init__.py
│     │  ├─ trained_models
│     │  │  └─ __init__.py
│     │  ├─ train_pipeline.py
│     │  ├─ VERSION
│     │  └─ __init__.py
│     ├─ requirements
│     │  ├─ requirements.txt
│     │  └─ test_requirements.txt
│     ├─ setup.py
│     ├─ tests
│     │  ├─ conftest.py
│     │  ├─ test_features.py
│     │  ├─ test_prediction.py
│     │  └─ __init__.py
│     └─ tox.ini
└─ section-08-deploying-with-containers
   ├─ .dockerignore
   ├─ Dockerfile
   ├─ house-prices-api
   │  ├─ app
   │  │  ├─ api.py
   │  │  ├─ config.py
   │  │  ├─ main.py
   │  │  ├─ schemas
   │  │  │  ├─ health.py
   │  │  │  ├─ predict.py
   │  │  │  └─ __init__.py
   │  │  ├─ tests
   │  │  │  ├─ conftest.py
   │  │  │  ├─ test_api.py
   │  │  │  └─ __init__.py
   │  │  └─ __init__.py
   │  ├─ mypy.ini
   │  ├─ Procfile
   │  ├─ requirements.txt
   │  ├─ run.sh
   │  ├─ runtime.txt
   │  ├─ test_requirements.txt
   │  └─ tox.ini
   └─ Makefile

```
