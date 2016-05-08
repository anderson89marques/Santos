__author__ = 'anderson'
# -*- coding: utf-8 -*-
from santos import ThreadSchecule
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

schedule = ThreadSchecule()
schedule.add_job(funcao, seconds="3", id="func1", kwargs={"a": "a"})
print("len1: {}".format(len(schedule)))
schedule.add_job(funcao, seconds="3", id="func2", kwargs={"a": "b"})
print("len2: {}".format(len(schedule)))
f(schedule, "func1")
f1(schedule, "func1")
f2(schedule, "func2")

