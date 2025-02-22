Proyecto basado en filtrado de análisis de datos a través de la página oficial de Aemet y en concretro de la estación metereológogica de Aragón medidos en Zaragoza diariamente desde 2020 hasta finales de 2024.

Se descargan archivos Json para después convertirlos a CSV.

Minucioso depurado y limpieza de datos NAN, barras, parentesis y comas de las 48 columnas para poder operar sin posible error. 

Creación de funciones para automatizar las conversiones y limpieza de posteriores dataframes de los años que hiciera faslta.

Creacion de BBDD para guardar en ella todos los DF y poder filtar cualquier información necesaria a través de la propia base de datos.

Mi proyecto se enfoca en tomar información detallada de los últimos 5 años en Zaragoza sobre el viento, tomando como variables dependientes la humedad y la temperatura al haberlas detectado con un heatmap.

Conclusiones finales en pestaña de analytics con gráfico de dispersión, graficos lineales superpuestos de los 5 aós para mayor legibilidad y finalmente técnica de regresión lineal para terminar observando y
concluyendo que aunque cada año los picos máximos y mínimos tienden a polarizarse cada vez mas, la pendiente negativa de -0.58 sugiere que, en general, la velocidad del viento media ha disminuido en los últimos cinco años y la pendiente negativa de -0.21 sugiere que, la temperatura media también está disminuyendo en los últimos años.
