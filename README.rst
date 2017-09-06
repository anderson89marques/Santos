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

Santos permite a execução de funcões e métodos python periódicamente em
intervalos definidos por uma sintaxe bem simples.

Instalação
----------

.. code-block:: bash

    pip install Santos

Exemplo
--------

.. code-block:: python

    from santos import ThreadSchedule

    def func(a):
        print(a)

    schedule.add_job(func, time_of_the_day="02:16:50", id="func1", kwargs={"a": "some data"})


Características
---------------

- Uma API simples para agendamento de tarefas.
- Sem dependência externa.
- teste unitário.
- Testada no Python 2.7, 3.4+

Sobre
-----

Para fazer o agendamento alguma tarefa é preciso apenas passar a função ou método a ser executado
para o método ``add_job`` da classe ThreadSchedule. É possível pausar, reativar e também remover uma tarefa do
agendador, como mostrado na próxima seção.

Os parâmetros aceitos pelo método add_job são: ``id, seconds, minutes, hour, time_of_the_day, day_of_the_week,
day_of_the_month.``
O ``id`` é obrigatório e é usado para identificar a tarefa que será executada, permitindo que se possa pausar,
reativar ou remover a tarefa definida.

Os parâmetros ``seconds, minutes e hour`` definem que a tarefa será executada
em intervalo de segundos, minutos e hora respectivamente. Só podem ser usados um por vez.

O parâmetro ``time_of_the_day`` define que a tarefa será executada todo dia em um horário específico,
que deve ser passado no seguinte formato ``hh:mm:ss``. (hh= 0..23 ; mm= 0..59, ss= 0..59). Não pode ser combinada com seconds, minuts e hour.

O parâmetro ``day_of_the_week`` define que a tarefa será executada repetidamente no dia da semana passado como valor.
Os valores possíveis são: ``Su para Sunday/Domingo, M para Monday/Segunda, Tu para Tuesday/Terça, W para Wednesday/Quarta,
Th para Thursday/Quinta, F para Friday/Sexta, Sa para Saturday/Sábado``. Sendo que este deve ser
combinado com o parâmetro ``time_of_the_day`` para especificar a hora, minuto e segundo daquele dia da semana.


Mais exemplos
-------------

.. code-block:: python

    from santos import ThreadSchedule

    def func(a):
        print(a)

    # Será executada todo dia às 02:16:50
    schedule.add_job(func, time_of_the_day="02:16:50", id="func1", kwargs={"a": "some data"})

    # Será executada a cada 3 segundos
    schedule.add_job(func, seconds="3", id="func2", kwargs={"a": "B"})

    # Será executada toda quinta-feira às 02:16:50
    schedule.add_job(func, day_of_the_week='Tu', time_of_the_day="02:16:50", id="func3", kwargs={"a": "Time_of"})

    # Será executada a cada 3 horas
    schedule.add_job(func, hour="3", id="func4", kwargs={"a": "B"})

    ## Pausando tarefas
    
    # Pausando a tarefa com id igual a func3
    schedule.pause_job("func3")

    # Ativando novamente a tarefa com id igual a func3
    schedule.resume_job("func3")

    # Removendo uma tarefa
    schedule.remove_job(job_name)

Meta
----
Anderson Marques - andersonoanjo18@gmail.com

Distribuído sobre lincensa MIT. Veja ``LICENSE.txt`` para mais informções.

https://github.com/anderson89marques/Santos