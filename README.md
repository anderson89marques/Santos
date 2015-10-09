# Santos
	Um agendador de tarefas para aplicações Python

# Um pouco de história
	Em 1904, cansado da falta de praticidade do relógio de bolso, o modelo "portátil" mais comum de sua época, Santos Dumont reclamou para um de seus melhores amigos, o joalheiro francês Louis Cartier (fundador da joalheira Cartier). Esses relógios, como indica o nome, ficavam guardados no bolso e, em muitos modelos, eram protegidos por uma tampa, o que obrigava a uma considerável manobra para se ver as horas. Para ele, um homem que passava grande parte do tempo dirigindo máquinas voadoras ou trabalhando em projetos, isso era um problema grave. 

	Santos Dumont pediu para que Cartier achasse uma saída para essa limitação. Algum tempo depois, o joalheiro presenteou o aviador com a solução que havia encontrado: O protótipo de um dos primeiros relógios de pulso masculinos, que recebeu o nome "Santos". Então deu o nome do relógio para esta lib. 

#Sobre
	Santos permite que você agende a execução da alguma tarefa apenas decorando a função ou método como mostrado nos exemplos abaixo. Os testes foram feitos nas versões 2.7 e 3.4 do Python.

	Os parâmetros aceitos são: seconds, minutes, hour, time_of_the_day, day_of_the_week, day_of_the_month
Descrição:
	O parâmetro seconds define que a função será executada repetidamente na frequência do valor passado em segundos.
   ex: seconds="20", será executado de 20 em 20 segundos
   	O parâmetro minutes define que a função será executada repetidamente na frequência do valor passado em minutos.
   ex: minutes="20", será executado de 20 em 20 minutos
 	O parâmetro hour define que a função será executada repetidamente na frequência do valor passado em horas
   ex: hour="2", será executado de 2 em 2 horas
obs: Esses três parâmetros não podem ser combinados, nem entre e nem com os dois abaixo.
	O parâmetro time_of_the_day define que a função será executada todo dia em um horário específico, que deve ser passado no seguinte formato hh:mm:ss.(hh: 0..23 ; mm: 0..59, ss: 0..59)
   ex: time_of_the_day="14:15:00", será executada todo dia às quartoze horas e quinze minutos
 	O parâmetro day_of_the_week define que a função será executada repetidamente no dia da semana passado como valor.
	Os valores possíveis são: Su(Sunday/Domingo), M(Monday/Segunda), Tu(Tuesday/Terça), W(Wednesday/Quarta), Th(Thursday/Quinta), F(Friday/Sexta), Sa(Saturday/Sábado) em maiúsculo.
	Tem que ser combinado com o parâmetro time_of_the_day para especificar a hora, minuto e segundo daquele dia da semana.
   ex: day_of_the_week="W"    time_of_the_day="22:00:00", Será executado toda quarta às vinte e dua horas.
    
    Exemplos de uso:
    Basta decorar a função eou método que se queira agendar.
        
        from santos import TaskScheduling
      
        @TaskScheduling(seconds="30")
        def do_something(a):
            print("Print do_something: %s" % a)
            import time
            time.sleep(6)
            print("terminou do_something")
        
        do_something()
        
        *****************************************
        
        from santos import TaskScheduling
        
        class Teste(object):
            
            @TaskScheduling(time_of_the_day="08:30:00")
            def some_function(self, b):
                print("Print some_function: %s" % b)
                import time
                time.sleep(10)
                print("terminou some_function")
        
        obj = Teste()
        obj.some_function("b")

Em test/exemple.py tem outros exemplos de uso.

#Contribuição
Se identificarem algum erro ou pensarem alguma melhoria fiquem a vontade para contribuir.
