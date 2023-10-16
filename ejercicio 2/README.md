## Ejercicio 2 -- The Formula 1 

Para este ejercicio es necesario contar con los siguientes requisitos:

* Python 3.10
* Ambiente ya sea con Conda u otro administrador de ambientes
* Para este ejercicio no se utilizo ninguna libreria ajena de Python 3.10

En el archivo *ejercicio12.py* esta el codigo fuente para la solucion del ejercicio, en los archivos *test1.py*, *test2.py*, *test3.py*, y *test4.py* se encuentran las pruebas unitarias que se realizaron para la comprobacion del ejercicio, cada prueba se realizo a una funcion en especifico. Con los siguientes comando se puede ejecutar:

~~~
python test1.py
~~~

En consola te estara pidiendo que ingreses los datos necesarios para calcular al campeon de la formula 1. Como se ve a continuacion:

~~~
Enter Grand Prix number and number of runners: 1 3
Enter result of the races: 3 2 1
Enter number of scoring systems: 3
Enter the scoring: 3 5 3 2
Enter the scoring: 3 5 3 1
Enter the scoring: 3 1 1 1
~~~

A continuacion obtendras los campeones de cada sistema segun su puntaje, Como se ve a continuacion:
~~~
3
3
1 2 3
~~~

Para salir del programa debe enviar '0 0', como a continuacion.
~~~
Enter Grand Prix number and number of runners: 0 0
~~~

Ahora para los tests, se pueden ejecutar con el siguiente comando:

~~~
python test1.py
~~~

Dentro de cada archivo de test se especifica que datos se envian.