# Práctica 02. - Exchange API 

Para gestionar la conexión a la api y la conversión de divisas esta la
clase ExchangeClient. Consta de los siguientes métodos. getDate, getRates,
convert y convertDate. Me he fijado que en la api aparece la fecha en la
cual se han actualizado las divisas, asi que la fecha que aparece en el
fichero de salida la obtengo de aqui.

También he decidido que la clase ExchangeClient se inizializa con la
moneda que se quiere obtener. De tal manera que si se quiere otra moneda
distinta del euro, se pone aquí.