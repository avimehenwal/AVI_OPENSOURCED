import pprint
import unittest
import datetime
import AlarmsImplementation

"""
list    -                           list of alarms
clear   -                           -
get     id                          dict

add     title, fire_time, repeat    id
update  id,title,fire_time,repeat   -
removes id                          -
"""

def add_date(AlarmObject):
    t1 = "Smaple Title 1"
    t2 = "Smaple Title 2"
    t3 = "Smaple Title 3"
    t4 = "Smaple Title 4"
    t5 = "Smaple Title 5"
    f1 = datetime.datetime(2015, 3, 10, 15, 55, 32, 158405)
    f2 = datetime.datetime(2015, 3, 11, 16, 55, 32, 158405)
    f3 = datetime.datetime(2015, 3, 12, 17, 55, 32, 158405)
    f4 = datetime.datetime(2015, 3, 13, 18, 55, 32, 158405)
    f5 = datetime.datetime(2015, 3, 14, 19, 55, 32, 158405)
    AlarmObject.add(t1, f1)
    AlarmObject.add(t2, f2)
    AlarmObject.add(t3, f3)
    AlarmObject.add(t4, f4)
    AlarmObject.add(t5, f5)
    return AlarmObject


class TestAlarmImplementation(unittest.TestCase):
    """ Alarms Class Functional Test cases """

    def setUp(self):
        self.a = AlarmsImplementation.Alarm()

    def test_get_empty_list(self):
        actual = self.a.list()
        expected = str({})  # empty dict in string format
        self.assertEqual(actual, expected, '%s %s Not Equal' % (actual, expected))

    def test_clear_empty_alarms(self):
        actual = self.a.clear()
        expected = None         # Could be improved if there are no items to clear
        self.assertEqual(actual, expected)

    def test_get_unregistered_alarm_by_id(self):
        try:
            actual = self.a.get(5)
        except Exception as e:
            print(e)
            self.assertIsInstance(e, AlarmsImplementation.AlarmNotFound)
        else:
            self.assertFalse(True)

    def test_remove_invalid_id(self):
        try:
            actual = self.a.remove(4)
        except Exception as e:
            print(e)
            self.assertIsInstance(e, AlarmsImplementation.AlarmNotFound)
        else:
            self.assertFalse(True)

    # def test_add_alarm_no_params(self):
        # actual = self.a.add()
        # TypeError: add() missing 2 required positional arguments: 'title' and 'fire_time'

    # def test_add_alarm_title(self):     # Positional Argument Error
    #     title = 'Sample Data'
    #     fire_time = datetime.datetime.now()
    #     actual = self.a.add(title)
    #     expected = 0
    #     self.assertEqual(actual, expected)

    def test_add_alarm_title_firetime(self):
        title = 'Sample Data'
        fire_time = datetime.datetime.now()
        actual = self.a.add(title, fire_time)
        expected = 0
        self.assertEqual(actual, expected)

    def test_get_registered_alarm_by_id(self):
        new = add_date(self.a)
        actual = new.get(4)
        expected = {'repeat': False, 'title': 'Smaple Title 5', 'fire_time': datetime.datetime(2015, 3, 14, 19, 55, 32, 158405)}
        print(actual)
        self.assertEqual(actual, expected)

    # def test_remove_alarm_without_id(self):     # Positional Argument Error could be handles
    #     new = add_date(self.a)
    #     actual = self.a.remove()
    #     print(actual)
    #     self.assertEqual(1, 2)

    def test_remove_alarm_invalid_id(self):
        new = add_date(self.a)
        try:
            actual = new.remove(8)
        except Exception as e:
            print(e)
            self.assertIsInstance(e, AlarmsImplementation.AlarmNotFound)
        else:
            self.assertFalse(True)

    def test_remove_alarm_valid_id(self):
        new = add_date(self.a)
        before = new.list()
        new.remove(2)
        after = new.list()
        print(type(dict(befself.assertNotEqual(before, after)
        # self.assertEqual(len(dict(before).keys()) - len(dict(after).keys()), 1)       # Returned object by list() should be dict

    def test_update_alarm_no_params(self):
        pass

    def test_update_alarm_existing_id(self):
        pass

    def test_update_alarm_new_id(self):     # BUG
        pass

    def test_update_alarm_only_id(self):
        pass

    def test_list_get_clear_after_add(self):
        pass

    def test_list_get_clear_after_update(self):
        pass

    def test_list_get_clear_after_remove(self):
        pass


if __name__ == '__main__':
    unittest.main()


