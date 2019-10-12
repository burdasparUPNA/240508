
# Práctica 03.- Database explorer (Flask API)

Primero antes de comentar nada, decir que al empezar a realizar
la práctica comenzé creando el proyecto en PyCharm dentro del
repositorio Git junto a los otros proyectos y en ese momentento
no me dejo instalar Flask en el proyecto. Así que lo creé en otro
directorio y luego lo añadi al repositorio. Espero que no haya
ningún problema.

Ahora comentare el proyecto.

Para poder gestionar todo lo relacionado con la base de datos
he creado la calse Database.py que recibe el nombre de la base
como parámetro y desde aquí se puede ejecutar las consultas y demás.

En la parte que devuelve JSON, he usado Jsonify, viene en la
librería de Flask. He decidido usar Jsonify en vez de
json.dumps() porque los datos al sacarlos, el navegador los
interpreta como cuando haces una llamada a una API normal. Es
decir, mejora la presentación.

También he desarrollado la versión en HTML como indicaba el
guión. Aparte de usar Jinja2, he decidido usar el framework
de Boostrap para mejorar la presentación. También he añadido
botones de navegación, para poder moverte entre todas las
páginas. Al hacer esto también he hecho que en la raiz de
todo "En localhost 127.0.0.1:5000/" haya una página que te
lleve a la lista de tablas. 
