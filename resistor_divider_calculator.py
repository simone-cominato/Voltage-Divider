""" Copyright (C) <2023>  <Simone Cominato>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>"""

from resistor_divider import Resistor_Divider

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find the correct resistors values to get the desired divide ratio.")
    parser.add_argument("input_voltage", metavar="Input Voltage", type=float, help="The voltage applied to the resistor divider")
    parser.add_argument("output_voltage", metavar="Output Voltage", type=float, help="The desired voltage to the resistor divider output")
    parser.add_argument("divider_current", metavar="Divider Current", type=float, help="The current flowing into the divider's resistors")
    parser.add_argument("resistors_tolerance", metavar="Resistors Tolerance", choices=[1, 2, 5, 10], type=int, help="The tolerance to use for the resistors")
    args = parser.parse_args()

    resistor_divider = Resistor_Divider(input_voltage = args.input_voltage,
                                        output_voltage = args.output_voltage,
                                        resistors_tolerance = args.resistors_tolerance,
                                        divider_current = args.divider_current)
    
    print(resistor_divider)
    
    resistor_divider.calc_divider()
    resistor_divider.print_divider_info()