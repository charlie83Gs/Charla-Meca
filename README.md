# Python 101

https://colab.research.google.com/drive/14m9Xl2cWPqA_Zkdlrle7M9juhd21Js8M?usp=sharing

# Using virtualenv

## Install Virtual Env

Run the command

```
pip install virtualenv
```

## Create a New Environment

```
virtualenv <env name>
```

in our case to create a environment called meca_env we use the command

```
virtualenv meca_env
```

## Activate the virtual environment

To activate the environment run the activate script located at the environment folder in our case the _meca_env_ folder.

```
<env name>\scripts\activate
```

In the case of meca_env the command is

```
meca_env\scripts\activate
```

## Install any dependecy required in the environment

In our case install argparse, matplotlib and networkx

```
pip install argparse matplotlib networkx
```

## Freeze the requirements to store them on the repository

Run the command to store a list of the installed dependencies.
We do not upload the meca_env folder as it contains files that are not been maintained by us.

```
pip freeze > requirements.txt
```

## Deactivate the virtual environment

To deactivate the environment run the deactivate script located at the environment folder in our case the _meca_env_ folder.

```
<env name>\scripts\deactivate
```

In the case of meca_env the command is

```
meca_env\scripts\deactivate
```
