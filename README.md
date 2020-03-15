[![Build Status](https://travis-ci.org/xegrassa/python-project-lvl2.svg?branch=master)](https://travis-ci.org/xegrassa/python-project-lvl2)

[![Maintainability](https://api.codeclimate.com/v1/badges/6a829b74e340aeec86c1/maintainability)](https://codeclimate.com/github/xegrassa/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/6a829b74e340aeec86c1/test_coverage)](https://codeclimate.com/github/xegrassa/python-project-lvl2/test_coverage)

## Description

The utility for finding differences in configuration files.

Support: json, yaml, ini

### Install

`pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ egrassa-gendiff`


### Use

`gendiff [-f FORMAT] first_file second_file`

Module:

```js
import gendiff from "gendiff-greybutton";

gendiff(path / to / file / 1, path / to / file / 2, format);
```

format: 'diff' is default, 'plain', 'json'

<a href="https://asciinema.org/a/AZTSUs8rFR8JBl7ehMLdK0KQB" target="_blank"><img src="https://asciinema.org/a/AZTSUs8rFR8JBl7ehMLdK0KQB.svg" /></a>

5-step
[![asciicast](https://asciinema.org/a/292649.svg)](https://asciinema.org/a/292649)

6-step
[![asciicast](https://asciinema.org/a/293788.svg)](https://asciinema.org/a/293788)

7-step
[![asciicast](https://asciinema.org/a/294066.svg)](https://asciinema.org/a/294066)

8-step
[![asciicast](https://asciinema.org/a/294423.svg)](https://asciinema.org/a/294423)
