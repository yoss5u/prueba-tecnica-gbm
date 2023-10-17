# Ejercicio #4 -- Customer Classification

Para este ejercicio es necesario contar con los siguientes requisitos:

* Python 3.10
* Ambiente ya sea con Conda u otro administrador de ambientes
* Para este ejercicio se utilizaron liberias ajenas a Python 3.10 por lo que en el archivo *requirements.txt* se especifican cuales se utilizan. 
* Ademas puedes utilizar [Google Colab](https://colab.research.google.com/) y ejecutar el codigo por celdas ya que se comprende de mejor manera y al momento de realizar el modelo permite mayor interaccion con datos y haciendo anotaciones mas claras de comprender. Por lo que se carga el archivo *ejercicio4.ipynb* y el CSV para ejecutarse correctamente.

Para este ejercicio 4 las 3 pruebas unitarias solicitadas estan en un mismo archivo que es el de *test1.py*

Ahora para ejecutar el archivo *main.py* que contiene la funcion para realizar las pruebas unitarias, en este caso es necesario tener en el mismo directorio el csv *df_combined.csv* ya que contiene los valores scalares asi como el modelo *data_customer_classification.h5*. 

Para correr el archivo *main.py* con el siguiente comando:
~~~
python main.py
~~~

Se obtendran los siguientes valores: 
~~~
1/1 [==============================] - 0s 66ms/step
Qualified customer High
~~~

Ahora para correr el test con el siguiente comando 
~~~
python test1.py
~~~

Obtenemos el siguiente resultado:
~~~
1/1 [==============================] - 0s 44ms/step
1/1 [==============================] - 0s 43ms/step
1/1 [==============================] - 0s 43ms/step
.
----------------------------------------------------------------------
Ran 3 tests in 0.403s

OK
~~~