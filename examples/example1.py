__author__ = 'anderson'
# -*- coding: utf-8 -*-

from santos import ThreadSchedule
import time


def f(schedule, job_name):
    time.sleep(10)
    schedule.pause_job(job_name)
    print("//a//")


def f1(schedule, job_name):
    time.sleep(20)
    schedule.resume_job(job_name)
    print("//b//")


def f2(schedule, job_name):
    time.sleep(25)
    schedule.remove_job(job_name)
    print("//c//")
    print("len: {}".format(len(schedule)))


def funcao(a):
    print(a)


def func(a):
    print(a)

schedule = ThreadSchedule()
schedule.add_job(funcao, seconds="3", id="func1", kwargs={"a": "A"})
print("len1: {}".format(len(schedule)))
schedule.add_job(funcao, seconds="3", id="func2", kwargs={"a": "B"})
print("len2: {}".format(len(schedule)))
schedule.add_job(func, day_of_the_week='Tu', time_of_the_day="02:16:50", id="func3", kwargs={"a": "Time_of"})
print("len3: {}".format(len(schedule)))


f(schedule, "func1")
f1(schedule, "func1")
f2(schedule, "func2")

