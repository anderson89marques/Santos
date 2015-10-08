__author__ = 'anderson'
# -*- coding: utf-8 -*-

from santos import TaskScheduling

def time_this(original_function):
    def new_function(*args, **kwargs):
        import datetime
        before = datetime.datetime.now()
        x = original_function(*args, **kwargs)
        after = datetime.datetime.now()
        print("Tempo de processamento {0}".format(after-before))
        return x
    return new_function

@TaskScheduling(seconds="10")
def function(timein):
    print("Time: %r" % timein)
    #time.sleep(timein)
    #a = []
    #for x in range(timein):
    #    a.append(x)
    a = [x for x in range(timein)]
    print("Fim")

#@TaskScheduling(hour="8", seconds="30", minutes="", day_of_the_week="S", time_of_the_day="hh:mm:ss", day_of_month="S")
def do_something(a):
    print("Print do_something: %s" % a)
    import time
    print("Função do_something")
    time.sleep(6)
    print("terminou do_something")


class Teste(object):

    @TaskScheduling(day_of_the_week="Th", time_of_the_day="00:16:00")
    def some_function(self, a):
        print("Print some_function: %s" % a)
        import time
        print("Função some_function")
        time.sleep(10)
        print("terminou some_function")


#do_something("a")
obj = Teste()
obj.some_function("b")
print("HEHEHEHEH")
#function(100000000)

