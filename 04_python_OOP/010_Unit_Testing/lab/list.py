class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)



from unittest import TestCase, main


class TestIntegerList(TestCase):
    def test_is_initialized_correctly_without_data(self):
        intger = IntegerList()
        self.assertEqual([], intger._IntegerList__data)

    def test_is_initialized_correctly_with_wrong_data(self):
        intger = IntegerList('asd', 5.6, 7.8)
        self.assertEqual([], intger._IntegerList__data)

    def test_is_initialized_correctly_with_integers_data(self):
        intger = IntegerList(5, 'asd', 3)
        self.assertEqual([5, 3], intger._IntegerList__data)

    def test_get_data(self):
        intger = IntegerList(5, 'asd')
        self.assertEqual([5], intger._IntegerList__data)

        result = intger.get_data()
        self.assertEqual([5], result)

    def test_add_method_incorect_data_raises(self):
        integer = IntegerList(5, 'asd')
        self.assertEqual([5], integer._IntegerList__data)

        with self.assertRaises(ValueError) as ex:
            integer.add("5")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_correct_data_adds_element(self):
        integer = IntegerList(5)
        self.assertEqual([5], integer._IntegerList__data)

        integer.add(10)
        self.assertEqual([5, 10], integer._IntegerList__data)

    def test_remove_el_removes_the_element(self):
        integer = IntegerList(5)
        integer.remove_index(0)
        self.assertEqual([], integer._IntegerList__data)
        self.assertEqual(0, len(integer._IntegerList__data))

    def test_remove_invalid_index_raises(self):
        integer = IntegerList(5)

        with self.assertRaises(IndexError) as ex:
            integer.remove_index(2)
        self.assertEqual("Index is out of range", str(ex.exception))




if __name__ == "__main__":
    main()