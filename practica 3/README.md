He creado un programa el cual mediante flask y la base de datos sqlite3, podemos conseguir datos en distintas urls.
Al ejecutar un programa en la url inicial aparece un listado de los nombres de las tablas que tenemos en la base de datos. Si a 
esa url le a�adimos /Clientes entonces nos aparecer� otro listado, pero esta vez con los nombres de los clientes que tenemos en la 
base de datos. Y por �ltimo si a la url inicial le a�adimos /ids entonces nos aparece un listado de los ids de los clientes que
tenemos registrados en la base de datos.
En los tres casos he guardado los elementos que me devolv�a la query en un vector. Lo he intentado convertir a json pero no he
conseguido solucionar el error de que no era serializable, por lo tanto he seguido trabajando con los vectores.
Para crear los html me he creado una funci�n auxiliar que es la que se encarga de montar las listas (<ol> ... </ol>)