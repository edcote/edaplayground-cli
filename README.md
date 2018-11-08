# EDA Playground CLI

## Getting Stated

* Follow these [instructions](http://chromedriver.chromium.org/getting-started) to install WebDriver for Chrome on your system.
* Install Python Virtualenv using the method of your choice. Examples: `pip3 install virtualenv` or `apt install python-virtualenv`.

### Launch program

```
$ . venv/bin/activate
$ ./edaplayround-cli.py --help
```

To exit your virtualenv, simply type `deactivate` or close the terminal window.

## Development

### Steps to add dependencies

```
$ virtualenv venv
$ . venv/bin/activate
$ # install your python packages, i.e., pip3 install package_name
$ pip3 freeze > requirements.txt
```

Only revision control file `requirements.txt`.

### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
