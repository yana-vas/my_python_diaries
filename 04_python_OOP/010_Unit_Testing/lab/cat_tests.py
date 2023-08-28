class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')

    self.sleepy = False


from unittest import TestCase, main


class CatTests(TestCase):
    def test_size_is_increased_after_eating(self):
        cat = Cat('Test')
        self.assertEqual(0, cat.size)

        cat.eat()
        self.assertEqual(1, cat.size)

    def test_is_fed_after_eating(self):
        cat = Cat('Test')
        self.assertEqual(False, cat.fed)

        cat.eat()
        self.assertEqual(True, cat.fed)

    def test_cannot_eat_if_already_fed(self):
        cat = Cat("Test")
        self.assertEqual(False, cat.fed)

        cat.eat()
        self.assertEqual(True, cat.fed)

        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual("Already fed.", str(ex.exception))

    def test_cannot_fall_asleep_if_not_fed(self):
        cat = Cat("Test")
        self.assertEqual(False, cat.fed)

        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

        self.assertEqual(False, cat.sleepy)

    def test_is_not_sleepy_after_sleeping(self):
        cat = Cat("Test")
        self.assertEqual(False, cat.sleepy)

        cat.eat()
        self.assertEqual(True, cat.sleepy)

        cat.sleep()
        self.assertEqual(False, cat.sleepy)


if __name__ =="__main__":
    main()