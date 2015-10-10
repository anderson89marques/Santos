.. highlight:: rst

Um pouco de história
====================
Em 1904, cansado da falta de praticidade do relógio de bolso, o modelo
"portátil" mais comum de sua época,Santos Dumont reclamou para um de
seus melhores amigos, o joalheiro francês Louis Cartier (fundador da joalheira Cartier).
Esses relógios, como indica o nome, ficavam guardados no bolso e, em muitos modelos,
eram protegidos por uma tampa, o que obrigava a uma considerável manobra para se ver as
horas. Para ele, um homem que passava grande parte do tempo dirigindo máquinas voadorasou
trabalhando em projetos, isso era um problema grave.

Santos Dumont pediu para que Cartier achasse uma saída para essa limitação. Algum tempo
depois, o joalheiro presenteou o aviador com a solução que havia encontrado:
O protótipo de um dos primeiros relógios de pulso masculinos, que recebeu o nome "Santos".
Então deu o nome do relógio para esta lib.


Santos
========

Um agendador de tarefas simples e eficente.

Um agendador para tarefas que precisam ser executados de forma periodica.
Santos permite a você rodar funcões e métodos Python periodicamente em
intervalos pré-determinados usando uma sintaxe bem simples.

Características
---------------

- Uma API simples para agendamenro de tarefas.
- Sem dependência external.
- teste unitário.
- Testada no Python 2.7 and 3.4

Sobre
-----

Santos permite que você agende a execução da alguma tarefa apenas decorando a
função ou método como mostrado nos exemplos abaixo.
Os testes foram feitos nas versões 2.7 e 3.4 do Python.

Os parâmetros aceitos são: name, seconds, minutes, hour, time_of_the_day, day_of_the_week,
day_of_the_month.
O Parâmetro name é usado para identificar a thread que será executada, assim é possível dar um stop.
Os parâmetros seconds, minutes e hour definem que a função ou método será executado
repetidamente na frequência do valor passado com paramentro, em segundos, minutos e
hora respectivamente.
obs: Esses três parâmetros não podem ser combinados, nem entre e nem com os dois abaixo.

O parâmetro time_of_the_day define que a função ou método será executada todo dia em um horário específico,
que deve ser passado no seguinte formato hh:mm:ss.(hh: 0..23 ; mm: 0..59, ss: 0..59)

O parâmetro day_of_the_week define que a função será executada repetidamente no dia da semana passado como valor.
Os valores possíveis são: Su(Sunday/Domingo), M(Monday/Segunda), Tu(Tuesday/Terça), W(Wednesday/Quarta),
Th(Thursday/Quinta), F(Friday/Sexta), Sa(Saturday/Sábado) em maiúsculo. Sendo que este deve ser
combinado com o parâmetro time_of_the_day para especificar a hora, minuto e segundo daquele dia da semana.


Exemplos de uso
---------------

.. code-block:: bash

    pip install Santos

.. code-block:: python

    from santos import TaskScheduling, stopjobs

    @TaskScheduling(name="nome", seconds="30")
    def do_something(a):
        print("Print do_something: %s" % a)
        import time
        time.sleep(6)
        print("terminou do_something")

    do_something()
    stopjobs.stop("nome")

    class Teste(object):

        @TaskScheduling(name="outronome", time_of_the_day="08:30:00")
        def some_function(self, a):
            print("Print some_function: %s" % a)
            import time
            print("Função some_function")
            time.sleep(10)
            print("terminou some_function")

    obj = Teste()
    obj.some_function("b")

Veja ``exemples`` para mais exemplos

Meta
----
Anderson Marques - andersonoanjo18@gmail.com

Distribuído sobre lincensa MIT. Veja ``LICENSE.txt`` para mais informções.

https://github.com/anderson89marques/Santos
