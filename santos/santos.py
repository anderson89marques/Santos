__author__ = 'anderson'
# -*- coding: utf-8 -*-

from threading import Thread, Condition
from datetime import datetime
from exceptions import TaskException
import logging

log = logging.getLogger(__name__)


class ThreadSchedule:
    __jobs = []  # jobs que serão executados

    def pause_job(self, job_name):
        log.debug("Job name %s" % job_name)
        log.debug(self.__jobs)
        for j in self.__jobs:
            if job_name == j.name:
                j.pause()  # job é bloqueado e fica esperando ser notificado
                #del self.__jobs[idx]
                break

    def remove_job(self, job_name):
        log.debug("Job name %s" % job_name)
        for idx, job in enumerate(self.__jobs):
            if job_name == job.name:
                job._stop()
                del self.__jobs[idx]
                break

    def resume_job(self, job_name):
        for job in self.__jobs:
            if job_name == job.name:
                job.paused = False
                break

    def add_job(self, func, id, **kwargs):
        """No kwargs estará todos os parâmetros para a função que será executada"""
        # é bom fazer um teste pra ver se de fato o id foi colocando, pois acho melhor esse parâmetro ser obrigatório
        job = Job(func, id, dargs=kwargs)
        self.__jobs.append(job)
        job.start()

    def __len__(self):
        return len(self.__jobs)


class Job(Thread):
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

        *****************************************

    """

    days = {"M": 0, "Tu": 1, "W": 2, "Th": 3, "F": 4, "Sa": 5, "Su": 6}

    def __init__(self, func, id, **arguments_map):
        Thread.__init__(self)
        try:
            self.name = id or ""
            self.args_function = arguments_map.get("dargs").get("kwargs")  # argumentos para a função a ser executada
            if self.args_function:
                del arguments_map["dargs"]["kwargs"]  # removendo os parâmetros da função a ser executada
            self.arguments_map = arguments_map["dargs"]   # parâmetros de tempo
            self.function = func
            self.condict = Condition()  # controlará o bloqueio/desbloqueio do job

        except Exception as e:
            log.debug("Erro {}".format(e.__str__()))

        log.debug("name:{}, args_functio:{},args_map:{}, func:{}".format(self.name, self.args_function, self.arguments_map, self.function))

    def run(self):
        try:
            log.debug("JOB RUNNING")
            import time
            self.execute = True
            self.paused = False

            while self.execute:
                if not self.paused:
                    interval = self.calculateInterval()
                    time.sleep(interval)
                    self.function(**self.args_function)
        except TaskException as t:
            log.debug(t)

    def pause(self):
        log.debug("PAUSE")
        self.paused = True

    def _stop(self):
        log.debug("STOP")
        self.execute = False

    def calculateInterval(self):
        """
        É responsável por determinar o tempo em segundos da próxima tarefa.
        Quando o parâmetro para determinar o tempo da pŕoxima tarefa for time_of_the_day é
        chamado o método auxCalculate para determinar tal tempo.
        :return:
        """

        if "day_of_the_week" in self.arguments_map:
            if "hour" in self.arguments_map or "minutes" in self.arguments_map or "seconds" in self.arguments_map:
                raise TaskException("Parametros extras que não combinam")

            if "time_of_the_day" in self.arguments_map:
                return self.calculateDayOfTheWeek(self.arguments_map["day_of_the_week"],
                                                  self.arguments_map["time_of_the_day"])
            else:
                raise TaskException("Parâmetro time_of_the_day não está presente")

        elif "time_of_the_day" in self.arguments_map:
            if "hour" in self.arguments_map or "minutes" in self.arguments_map or "seconds" in self.arguments_map:
                raise TaskException("Parametros extras que não combinam")
            return self.auxCalculate(self.arguments_map["time_of_the_day"])[0]

        elif "hour" in self.arguments_map:
            if "seconds" in self.arguments_map or "minutes" in self.arguments_map:
                raise TaskException("Parametros extras que não combinam")
            return int(self.arguments_map["hour"]) * 3600

        elif "minutes" in self.arguments_map:
            if "seconds" in self.arguments_map:
                raise TaskException("Parametros extras que não combinam")
            else:
                return int(self.arguments_map["minutes"]) * 60

        elif "seconds" in self.arguments_map:
            log.debug("seconds")
            return int(self.arguments_map["seconds"])

        else:
            raise TaskException("Parâmetro(s): %r inválidos" % self.arguments_map)

    def calculateDayOfTheWeek(self, day_of_the_week, time_of_the_day):
        entrada = day_of_the_week
        weekday = datetime.now().weekday()
        dif = self.days[entrada] - weekday
        sleep, diference = self.auxCalculate(time_of_the_day)

        if self.days[entrada] == weekday:
            if diference > 0:
                return sleep
            else:
                return sleep + (6 * (24*3600)) #24 horas para segundo
        elif self.days[entrada] > weekday:
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

            if diference <= 0:
                #só será executado no outro dia
                sleep_time = time_day - (diference * (-1))
            else:
                #ainda será executado no mesmo dia
                sleep_time = diference
        except TaskException as t:
            log.debug(t)

        return sleep_time, diference