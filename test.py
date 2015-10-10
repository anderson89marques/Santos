__author__ = 'anderson'
import unittest

from santos import TaskScheduling
from exceptions import TaskException


class SantosTest(unittest.TestCase):
    def setUp(self):
        self.taskScheduling = TaskScheduling(name="task", hour="1")

    def test_hour(self):
        print("Teste hour")
        self.assertEqual(self.taskScheduling.calculateInterval(), 3600)

    def test_minute(self):
        print("Teste minute")
        self.taskScheduling = TaskScheduling(name="task2", minutes="1")
        self.assertEqual(self.taskScheduling.calculateInterval(), 60)

    def test_day_of_week_raise(self):
        print("Teste day_of_the_week")
        self.taskScheduling = TaskScheduling(name="task3", day_of_the_week="Sa")
        with self.assertRaises(TaskException):
            self.taskScheduling.calculateInterval()

    def test_params_not_combined(self):
        self.taskScheduling = TaskScheduling(name="task4", seconds="2", hour="2")
        with self.assertRaises(TaskException):
            self.taskScheduling.calculateInterval()
