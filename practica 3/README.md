He creado un programa el cual mediante flask y la base de datos sqlite3, podemos conseguir datos en distintas urls.
Al ejecutar el programa, en la url inicial que aparece, mostrar� una p�gina dandonos la bienvenida. Si a dicha url le a�adimos
al final /html/tablas entonces nos aparecer� una p�gina en la cu�l hay un listado de los nombres de las tablas que existen
en la base de datos. En otro caso, si a�adimos /html/tablas/<nombre de la tabla> (cambiar <nombre de la tabla> por el nombre 
de la tabla correspondiente que queremos inspeccionar), entonces nos aparece una p�gina en la cu�l hay un listado de los registros
que tiene dicha tabla. Por �ltimo, si a�adimos /html/tablas/<nombre de la tabla>/info (cambiar <nombre de la tabla> por el nombre 
de la tabla correspondiente que queremos inspeccionar), entonces nos aparece una p�gina en la cu�l hay un listado de los nombres
de las columnas de dicha tabla y al final del todo aparece el n�mero de registros que tiene dicha tabla.