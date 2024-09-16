#! /bin/bash

pip install poetry
rm -r build
poetry install --no-dev
mkdir build && cd build
cp -r $(poetry env info -p)/lib/*/site-packages/* .
cp -r ../car_data_api .
cp ../app.py .
zip -r ../cr-ai-car-data-api-dev.zip .