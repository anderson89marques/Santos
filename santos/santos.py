__author__ = 'anderson'
# -*- coding: utf-8 -*-

from threading import Thread
from datetime import datetime

from exceptions import TaskException


class TaskScheduling(Thread):
    """
        Os parâmetros aceitos são:
        seconds, minutes, hour, time_of_the_day, day_of_the_week, day_of_the_month

        Descrição:
        O parâmetro seconds define que a função será executada repetidamente na frequência do valor passado em segundos

            ex: seconds="20", será executado de 20 em 20 segundos

        O parâmetro minutes define que a função será executada repetidamente na frequência do valor passado em minutos

            ex: minutes="20", será executado de 20 em 20 minutos

        O parâmetro hour define que a função será executada repetidamente na frequência do valor passado em horas

            ex: hour="2", será executado de 2 em 2 horas

        obs: Esses três parâmetros não podem ser combinados, nem entre e nem com os dois abaixo.

        O parâmetro time_of_the_day define que a função será executada todo dia em um horário específico, que deve ser
        passado no seguinte formato hh:mm:ss.(hh: 0..23 ; mm: 0..59, ss: 0..59)

            ex: time_of_the_day="14:15:00", será executada todo dia às quartoze horas e quinze minutos

        O parâmetro day_of_the_week define que a função será executada no dia da semana passado como valor.
        Os valores possíveis são: Su(Sunday/Domingo), M(Monday/Segunda), Tu(Tuesday/Terça), W(Wednesday/Quarta),
        Th(Thursday/Quinta), F(Friday/Sexta), Sa(Saturday/Sábado) em maiúsculo.

        Tem que ser combinado com o parâmetro time_of_the_day para especificar a hora, minuto e segundo daquele
        dia da semana.

            ex: day_of_the_week="W"    time_of_the_day="22:00:00", Será executado toda quarta às vinte e dua horas.

        Exemplos de uso:
        Basta decorar a função ou método da classe que se queira agendar.

        @TaskScheduling(seconds="30")
        def do_something(a):
            print("Print do_something: %s" % a)
            import time
            time.sleep(6)
            print("terminou do_something")

        do_something()

        *****************************************

        class Teste(object):

            @TaskScheduling(time_of_the_day="08:30:00")
            def some_function(self, a):
                print("Print some_function: %s" % a)
                import time
                print("Função some_function")
                time.sleep(10)
                print("terminou some_function")

        obj = Teste()
        obj.some_function("b")

    """

    #recebe os parametros do decorator
    def __init__(self, *arguments, **argumentsMap):
        Thread.__init__(self)

        self.args = arguments
        self.argumentsMap = argumentsMap
        self.execute = False

    #É o decorador de verdade, recebe a função decorada, como é uma classe preciso implementar o método call
    def __call__(self, function):
        self.function = function

        #recebe os argumentos da função decorada
        def task(*functionargs, **functionArgumentsMap):
            self.functionargs = functionargs
            self.functionArgumentsMap = functionArgumentsMap
            self.start()
        return task

    def run(self):
        try:
            print("JOB RUNNING")
            import time
            self.execute = True
            while self.execute:
                interval = self.calculateInterval()
                print("Interval: %f in seconds" % interval)
                time.sleep(interval)
                self.function(*self.functionargs, **self.functionArgumentsMap)
        except TaskException as t:
            print(t)

    def _stop(self):
        print("STOP")
        self.execute = False

    def calculateInterval(self):
        """
        É responsável por determinar o tempo em segundos da próxima tarefa.
        Quando o parâmetro para determinar o tempo da pŕoxima tarefa for time_of_the_day é
        chamado o método auxCalculate para determinar tal tempo.
        :return:
        """
        try:
            if "day_of_the_week" in self.argumentsMap:
                if "time_of_the_day" in self.argumentsMap:
                    return self.calculateDayOfTheWeek(self.argumentsMap["day_of_the_week"],
                                                      self.argumentsMap["time_of_the_day"])
                else:
                    raise TaskException("Parâmetro time_of_the_day não está presente")
            elif "time_of_the_day" in self.argumentsMap:
                return self.auxCalculate(self.argumentsMap["time_of_the_day"])[0]
            elif "hour" in self.argumentsMap:
                return int(self.argumentsMap["hour"]) * 3600
            elif "minutes" in self.argumentsMap:
                return int(self.argumentsMap["minutes"]) * 60
            elif "seconds" in self.argumentsMap:
                return int(self.argumentsMap["seconds"])
            else:
                raise TaskException("Parâmetro(s): %r inválidos" % self.argumentsMap)
        except TaskException as t:
            print(t)

    def calculateDayOfTheWeek(self, day_of_the_week, time_of_the_day):
        days = {"M": 0, "Tu": 1, "W": 2, "Th": 3, "F": 4, "Sa": 5, "Su": 6}
        entrada = day_of_the_week
        weekday = datetime.now().weekday()
        dif = days[entrada] - weekday
        sleep, diference = self.auxCalculate(time_of_the_day)

        if days[entrada] == weekday:
            if diference > 0:
                return sleep
            else:
                return sleep + (6 * (24*3600)) #24 horas para segundo
        elif days[entrada] > weekday:
            if diference > 0:
                return sleep + (dif * (24*3600))
            else:
                #Se a entrada já é o dia seguinte, basta retornar o sleep pois já está calculada o tempo para o horário do outro dia.
                if dif == 1:
                    return sleep
                else:
                    return sleep + ((dif-1) * (24*3600)) #24 horas para segundo
        else:
            #numero de dias de diferença
            resp = 7 - abs(dif)

            if diference > 0:
                return sleep + (resp * (24*3600))
            else:
                #Se a entrada já é o dia seguinte, basta retornar o sleep pois já está calculada o tempo para o horário do outro dia.
                if resp == 1:
                    return sleep
                else:
                    return sleep + ((resp-1) * (24*3600)) #24 horas para segundo

    def auxCalculate(self, time_of_the_day):
        """
        Essa método retorno o tempo em segundos para que a tarefa seja sempre executada na hora escolhida.
        :param time_of_the_day:
        :return: sleep_time
        """

        try:
            times = [3600, 60, 1]

            one_day_has = '24:00:00'.split(":")
            time_day = sum([a*b for a, b in zip(times, [int(i) for i in one_day_has])])

            aux_time = time_of_the_day.split(":")
            time_want = sum([a*b for a, b in zip(times, [int(i) for i in aux_time])])

            #Transforma o tempo atual para segundos
            hjf = datetime.now().strftime("%H:%M:%S").split(":")
            now = sum([a*b for a, b in zip(times, [int(i) for i in hjf])])

            #diferença entre o tempo atual e o tempo desejado em segundos
            diference = time_want - now
            sleep_time = None

            if diference < 0:
                #só será executado no outro dia
                sleep_time = time_day - (diference * (-1))
            else:
                #ainda será executado no mesmo dia
                sleep_time = diference
        except TaskException as t:
            print(t)

        return sleep_time, diference
