He creado un programa el cual mediante flask y la base de datos sqlite3, podemos conseguir datos en distintas urls.
Al ejecutar el programa, en la url inicial que aparece, mostrará una página dandonos la bienvenida. Si a dicha url le añadimos
al final /html/tablas entonces nos aparecerá una página en la cuál hay un listado de los nombres de las tablas que existen
en la base de datos. En otro caso, si añadimos /html/tablas/"nombre de la tabla" (cambiar "nombre de la tabla" por el nombre 
de la tabla correspondiente que queremos inspeccionar), entonces nos aparece una página en la cuál hay un listado de los registros
que tiene dicha tabla. Por último, si añadimos /html/tablas/"nombre de la tabla"/info (cambiar "nombre de la tabla" por el nombre 
de la tabla correspondiente que queremos inspeccionar), entonces nos aparece una página en la cuál hay un listado de los nombres
de las columnas de dicha tabla y al final del todo aparece el número de registros que tiene dicha tabla.
