import numpy as np

class Resistor():

    @property
    def r_value(self):
        return self._r_value
    
    @r_value.setter
    def r_value(self, value):
        if value < 0:
            raise ValueError("r_value must be >= 0")
        
        self._r_value = value
    
    @property
    def r_tolerance(self):
        return self._r_tolerance
    
    @r_tolerance.setter
    def r_tolerance(self, value):
        tolerance_list = np.array([1, 2, 5, 10])
        if not np.any(tolerance_list == value):
            raise ValueError(f"value must be one of {tolerance_list}")
        else:
            self._r_tolerance = value
    
    @property
    def r_power(self):
        return self._r_power
    
    @r_power.setter
    def r_power(self, value):
        if value < 0:
            raise ValueError("r_power must be >= 0")
        
        self._r_power = value
    
    __r_std = 0
    
    def __init__(self,
                 *,
                 value: float = 0,
                 tolerance: int = 5,
                 power: float = 0.25) -> None:
        
        self.r_value = value
        self.r_tolerance = tolerance
        self.r_power = power
    
    def __str__(self) -> str:
        
        res_description = f"r_value: {self.r_value}\n"\
                          f"r_tolerance: {self.r_tolerance}\n"\
                          f"r_power: {self.r_power}\n"
        
        return res_description
    
    @classmethod
    def __E_series(cls,
                   r_value: float,
                   r_tolerance: float) -> float:
        
        e_series = {1: 96, 2: 48, 5: 24, 10: 12}
        m = e_series[r_tolerance]

        decimals = 0
        if r_tolerance >= 5:
            decimals = 1
        else:
            decimals = 2

        exp = 0
        res = r_value
        while (res >= 10.0):
            res /= 10
            exp += 1
        
        r_low = 1 * (10 ** decimals)
        r_value_adj = r_value * (10 ** (decimals - exp))
        for n in range(1, m):
            r_high = int(round(10 ** (decimals + (float(n) / float(m))), ndigits = 0))

            # Adjust for E12 and E24 quirks
            if m == 12:
                if n >=5 and n <= 8:
                    r_high += int(0.1 * (10 ** decimals))
                elif n == 11:
                    r_high -= int(0.1 * (10 ** decimals))
            elif m == 24:
                if n >=10 and n <= 16:
                    r_high += int(0.1 * (10 ** decimals))
                elif n == 22:
                    r_high -= int(0.1 * (10 ** decimals))
            

            if ((r_low <= r_value_adj) and
                r_high >= r_value_adj):
                if (r_value_adj - r_low) <= (r_high - r_value_adj):
                    return r_low * (10 ** (exp - decimals))
                else:
                    return r_high * (10 ** (exp - decimals))
            elif ((r_value_adj > r_high) and
                   n == m - 1):
                r_low = r_high
                r_high = 1 * (10 ** (decimals + 1))
                if (r_value_adj - r_low) <= (r_high - r_value_adj):
                    return r_low * (10 ** (exp - decimals))
                else:
                    return r_high * (10 ** (exp - decimals))
            else:
                r_low = r_high
        
    def get_std_value(self) -> float:
        
        self.__r_std = self.__E_series(self.r_value, self.r_tolerance)
        return self.__r_std


if __name__ == "__main__":

    resistor = Resistor()
    
    tolerances = [10, 5, 2, 1]

    for t in tolerances:
        for r in range(100, 1000):
        
            resistor.r_value = r
            resistor.r_tolerance = t
            r_std = resistor.get_std_value()

            print(f"{resistor.r_value} - {resistor.r_tolerance} -> {r_std}")

