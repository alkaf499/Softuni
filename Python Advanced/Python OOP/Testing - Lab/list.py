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
//
from unittest import TestCase, main

# from project.list import IntegerList


class TestList(TestCase):
    def setUp(self):
        self.intlist = IntegerList(2, 4, 6)


    def test_correct_initiation(self):
        self.assertEqual([2, 4 ,6], self.intlist._IntegerList__data)


    def test_correct_get_data(self):
        self.assertEqual([2, 4 ,6], self.intlist.get_data())


    def test_add_with_error(self):
        with self.assertRaises(ValueError) as ex:
            self.intlist.add("Asd")
        self.assertEqual('Element is not Integer', str(ex.exception))


    def test_add_well_working(self):
        result = self.intlist.add(8)
        self.assertEqual(result, [2, 4 ,6, 8])
        self.assertEqual(self.intlist._IntegerList__data, [2, 4 ,6, 8])


    def test_remove_index(self):
        with self.assertRaises(IndexError) as ex:
            self.intlist.remove_index(7)
        self.assertEqual('Index is out of range', str(ex.exception))


    def test_remove_well_working(self):
        result = self.intlist.remove_index(2)
        self.assertEqual([2, 4], self.intlist._IntegerList__data)
        self.assertEqual(result, 6)


    def test_get_not_working(self):
        with self.assertRaises(IndexError) as ex:
            self.intlist.get(7)
        self.assertEqual('Index is out of range', str(ex.exception))


    def test_get_working(self):
        self.assertEqual(6, self.intlist.get(2))


    def test_insert_exception_index(self):
        with self.assertRaises(IndexError) as ex:
            self.intlist.insert(7, 2)
        self.assertEqual('Index is out of range', str(ex.exception))


    def test_insert_exception_not_int(self):
        with self.assertRaises(ValueError) as ex:
            self.intlist.insert(2, "abc")
        self.assertEqual('Element is not Integer', str(ex.exception))


    def test_insert_working(self):
        self.intlist.insert(2, 8)
        self.assertEqual([2, 4, 8, 6], self.intlist._IntegerList__data)


    def test_get_biggest(self):
        self.assertEqual(6, self.intlist.get_biggest())


    def test_get_index(self):
        self.assertEqual(0, self.intlist.get_index(2))


if __name__ == '__main__':
    main()
