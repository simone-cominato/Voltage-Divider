from resistor import Resistor

class Resistor_Divider():
    
    @property
    def input_voltage(self):
        return self._input_voltage
    
    @input_voltage.setter
    def input_voltage(self, value):
        if value == 0:
            raise ValueError(f"input_voltage must be != 0")

        self._input_voltage = value
    
    @property
    def output_voltage(self):
        return self._output_voltage
    
    @output_voltage.setter
    def output_voltage(self, value):
        if value == 0:
            raise ValueError(f"output_voltage must be != 0")

        self._output_voltage = value

    @property
    def resistors_tolerance(self):
        return self._resistors_tolerance
    
    @resistors_tolerance.setter
    def resistors_tolerance(self, value):
        if value <= 0 or value > 100:
            raise ValueError(f"resistors_tolerance must be > 0 and <= 100")

        self._resistors_tolerance = value
    
    @property
    def divider_current(self):
        return self._divider_current
    
    @divider_current.setter
    def divider_current(self, value):
        if value <= 0:
            raise ValueError(f"divider_current must be > 0")

        self._divider_current = value

    __r_up = 0
    __r_down = 0
    __div_current = 0
    __out_voltage = 0

    def calc_divider(self) -> None:
        
        rs = self.input_voltage / self.divider_current
        
        actual_vout = 0
        iterations = 0

        while abs(self.output_voltage - actual_vout) > 0.01 and iterations < 100:
            r_down = (self.output_voltage / self.input_voltage) * rs
            r_down_std = Resistor(value = r_down,
                                tolerance = self.resistors_tolerance).get_std_value()
            r_up = rs - r_down_std
            r_up_std = Resistor(value = r_up,
                                tolerance = self.resistors_tolerance).get_std_value()
            rs = r_up_std + r_down_std
            actual_vout = self.input_voltage * (r_down_std / rs)

            iterations += 1
        
            self.__r_up = r_up_std
            self.__r_down = r_down_std
            self.__div_current = self.input_voltage / rs
            self.__out_voltage = actual_vout
    
    def __get_divider(self) -> tuple[float, float]:

        return (self.__r_up, self.__r_down)

    def __get_div_current(self) -> float:

        return self.__div_current
    
    def __get_output_voltage(self) -> float:

        return self.__out_voltage

    def print_divider_info(self) -> None:

        print(f"Upper resistor: {self.__r_up} Ohm")
        print(f"Lower resistor: {self.__r_down} Ohm")
        print(f"Divider current: {self.__div_current} A")
        print(f"Output voltage: {self.__out_voltage} V")
    
    def __init__(self,
                 *,
                 input_voltage: float,
                 output_voltage: float,
                 resistors_tolerance: int,
                 divider_current: float) -> None:
        
        self.input_voltage = input_voltage
        self.output_voltage = output_voltage
        self.resistors_tolerance = resistors_tolerance
        self.divider_current = divider_current
    
    def __str__(self) -> str:
        
        rd_properties = f"input_voltage: {self.input_voltage} V\n"\
                        f"output_voltage: {self.output_voltage} V\n"\
                        f"resistors_tolerance: {self.resistors_tolerance} %\n"\
                        f"divider_current: {self.divider_current} A\n"
        
        return rd_properties

if __name__ == "__main__":

    resistor_divider = Resistor_Divider(input_voltage = 12,
                                        output_voltage = 3,
                                        resistors_tolerance = 1,
                                        divider_current = 0.00017)
    
    print(resistor_divider)
    
    resistor_divider.calc_divider()
    resistor_divider.print_divider_info()