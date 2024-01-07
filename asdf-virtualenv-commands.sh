# Get latest python version
$ asdf latest python
$ asdf latest python 3.10
$ asdf list all python 3.11

# Instlall a python version
$ asdf install python 3.10.13

# Set local python version
$ asdf local python 3.10.13

# Create a new virtualenv
$ virtualenv ~/Virtualenvs/python-practice

# Create .env files to activate/deactivate virtualenv when in directory
$ echo -e "AUTOENV_ENABLE_LEAVE=1\nsource ~/Virtualenvs/python-practice/bin/activate" > .env
$ echo deactivate > .env.leave

# Activate virtualenv manually
$ source ~/Virtualenvs/python-practice/bin/activate




# Create Git repository w/ README.md

# Git clone repository
$ cd ~/Develop
$ git clone https://github.com/Wind-River-Systems/fivetran_custom_connectors.git

# Create virtualenv and activate
$ cd ~/Develop/fivetran_custom_connectors/dbt
$ pyenv local 3.8.13
$ pyenv virtualenv fivetran-dbt-lambda
$ pyenv activate fivetran-dbt-lambda

# Install python libraries
$ pip install --upgrade requests
$ pip install --upgrade jupyter notebook
$ pip install --upgrade pip
$ pip install dbt-cloud-api-client

# Create requirements.txt file
$ pip freeze > requirements.txt

# Serverless Reference: https://medium.com/analytics-vidhya/serverless-framework-package-your-lambda-functions-easily-6c4f0351cdab
$ npm install -g serverless

$ serverless create \
 --template aws-python3 \
 --name av-fivetran-dbt \
 --path av-fivetran-dbt

# Create package.json
$ npm init

# Install serverless-python-requirements pacakge
$ npm install --save serverless-python-requirements

# Add plugins and custom sections to serverless.yml

# Start Docker

# Deploy serverless to dev
$ serverless deploy --stage dev

# Deploy serverless to prod
$ serverless deploy --stage prod --region us-west-2

# Deactivate virtualenv
$ pyenv deactivate