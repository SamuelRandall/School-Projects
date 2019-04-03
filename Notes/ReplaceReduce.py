from operator  import add, sub
from unittest  import main, TestCase


class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            Reduce]

    def test_1 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(None, [],       0),  0)

    def test_2 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(add, [2],       1),  3)

    def test_3 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(add, [2, 3, 4], 0),  9)

    def test_4 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(sub, [2, 3, 4], 0), -9)

    def test_5 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(sub, [2, 3, 4], 1), -8)


## Reduce function

def Reduce(f, lst, x0):
    if f:
        for element in lst:
            x0 = f(x0, element)
        return(x0)
    else:
        return(0)

if __name__ == "__main__" :
    main()
