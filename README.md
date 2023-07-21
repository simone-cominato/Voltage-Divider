# Python Resistor Divider Calculator

This is a Python application to calculate the standard resistors values needed in a resistor divider to get the desired output voltage given the input voltage, the current flowing into the two resistors and the resistors tolerance.

## Table of Contents

- [Python Resistor Divider Calculator](#project-title)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## About

Python Resistor Divider Calculator (PRDC) calculate the standard resistors values needed in a resistor divider to get the desired output voltage given the input voltage, the current flowing into the two resistors and the resistors tolerance. Based on the resistors tolerance specified the resitors values will follow the standard "E series" values the following way:
- 10 % -> E12
- 5 % -> E24
- 2 % -> E48
- 1 % -> E96

The program iteratively search for the resistors pair that minimizes the error on the output voltage with the constraint that the sum of the two resistors do not drain more current than specified.

It was made as an exercise to learn Python's OOP programming.

## Getting Started

### Prerequisites

PRDC is written in [Python](https://www.python.org/) and uses [numpy](https://numpy.org/) and [argparse](https://docs.python.org/3/library/argparse.html), so to be able to run the program you need to first install Python and then type the usual pip commands:
```console
pip install numpy
pip install argparse
```

### Installation

Clone the project
```console
git clone https://github.com/simone-cominato/Resistor-Divider.git
```
And if you didn't already, install Python and the dependencies listed in [Prerequisites](#prerequisites)

## Usage

To learn how to use it type -h or --help
```console
python ./resistor_divider_calculator.py --help
usage: resistor_divider_calculator.py [-h] Input Voltage Output Voltage Divider Current Resistors Tolerance

Find the correct resistors values to get the desired divide ratio.

positional arguments:
  Input Voltage        The voltage applied to the resistor divider
  Output Voltage       The desired voltage to the resistor divider output
  Divider Current      The current flowing into the divider's resistors
  Resistors Tolerance  The tolerance to use for the resistors

options:
  -h, --help           show this help message and exit
```

## Contributing

If you wanto to contribute to this project please create an issue. Since it's a side project started for learning purpose issues will be fixed on a best effort basis.

## License

Python Resistor Divider Calculator is licensed under the terms and conditions of the GPL-V3 license.
