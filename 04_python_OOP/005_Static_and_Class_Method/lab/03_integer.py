class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if type(float_value) != float:  # isinstance(value, type) -> isinstance(5, int) = True
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                 'CD': 400, 'CM': 900}
        i = 0
        num = 0
        while i < len(value):
            if i + 1 < len(value) and value[i:i + 2] in roman:
                num += roman[value[i:i + 2]]
                i += 2
            else:
                # print(i)
                num += roman[value[i]]
                i += 1
        return cls(num)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"


integer = Integer.from_float(11.5)
print(integer.value)

second_num = Integer.from_roman("IV")
print(second_num.value)


# import unittest
#
#
# class IntegerTests(unittest.TestCase):
#     def test_basic_init(self):
#         integer = Integer(1)
#         self.assertEqual(integer.value, 1)
#
#     def test_from_float_success(self):
#         integer = Integer.from_float(2.5)
#         self.assertEqual(integer.value, 2)
#
#     def test_from_float_wrong_type(self):
#         result = Integer.from_float("2.5")
#         self.assertEqual(result, "value is not a float")
#
#     def test_from_roman(self):
#         integer = Integer.from_roman("XIX")
#         self.assertEqual(integer.value, 19)
#
#     def test_from_string_success(self):
#         integer = Integer.from_string("10")
#         self.assertEqual(integer.value, 10)
#
#     def test_from_string_wrong_type(self):
#         result = Integer.from_string(1.5)
#         self.assertEqual(result, "wrong type")
#
#
# if __name__ == "__main__":
#     unittest.main()
