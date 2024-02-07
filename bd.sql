CREATE TABLE Clasificaciones(
  año       INT,            
  deporte   VARCHAR (30),   
  equipo    VARCHAR (30),
  genero    VARCHAR (1),    -- 'm' masculino, 'f' femenino
  puesto    INT,            --Puesto en la clasificacion final, -1 si ha sido descalificado
  puntos    INT,            
  asc_desc  INT,            --1 ascenso, -1 descenso, 0 permanencia
  alfonso   INT,            --Puesto en final, -1 si no se ha clasificado
  PRIMARY KEY(año, deporte, equipo, genero)
);
