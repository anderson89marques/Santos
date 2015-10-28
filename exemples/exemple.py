__author__ = 'anderson'
# -*- coding: utf-8 -*-

from santos import TaskScheduling, stopjobs
import time

@TaskScheduling(name="function", seconds="10")
def function(timein):
    print("Time: %r" % timein)
    a = [x for x in range(timein)]
    print("Fim")

@TaskScheduling(name="do", seconds="15")
def do_something(a):
    print("Print do_something: %s" % a)
    import time
    print("Função do_something")
    time.sleep(6)
    print("terminou do_something")


class Teste(object):

    @TaskScheduling(name="some", day_of_the_week="Th", time_of_the_day="00:16:00")
    def some_function(self, a):
        print("Print some_function: %s" % a)
        import time
        print("Função some_function")
        time.sleep(10)
        print("terminou some_function")

#Descomente e execute o módulo para testar.

do_something("a")
#obj = Teste()
#obj.some_function("b")
#function(100000000)
#do_something("a")

