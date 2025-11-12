# BIG DATA APLICADO

## Comando aplicado para iniciar docker

sudo docker compose up -d  

parametro: -p smartcity (para abrir un proyecto si tienes un contenedor con ese nombre)

## Ver servicios funcionando

sudo docker ps -a 

## Comando para utilizar el servicio mongo

sudo docker run -it mongo mongo


## Comando para crear o entrar en una base de datos 

use XXX

## Crear una colección

db.createCollection("XXXX")

## Coomando para crear o insertar una colección con datos

db.XXX.insertOne({"name":"Pedro","lastname":"Pancorbo Sánchez"})

## Eliminar un registro

  db.XXX.deleteOne( {id:23})

## Para hacer un update de un registro(atributo) de la colección

 db.XXX.update({name:"Arturo"},{$set:{nota:8.2,orden:12,actitud:"positiva"}})

 ## Para eliminar un campo(atributo) del registro

  db.XXX.update({name:"Arturo"},{$unset:{nota:8.2,orden:12,actitud:"positiva"}})

## Para incrementar valores numericos o disminuirlos

db.XXX.update({name:"Arturo"},{$inc:{nota:2}})

## Permite dejar el Valor al que pongas siempre y cuando sea mayor que ese valor (por ejemplo si le pongo 3 y el valor es 2 no cambia si es mayor a 3 si cambia)
### Existen los tipos ($mul, $min, $max y $currentDate.)

db.XXX.update({name:"Arturo"},{$min:{puntuacion:3}})

## Igual que el updateOne, pero si no existe el where me lo crea, solo el primero que encuentra

db.XXX.update({name:"Sofia"},
                {$set:{apellidos:"Alarcon Revilla"}},
                {upsert:true})

## Igual que la anterior pero modificaría todos los que cumplen la condición

db.XXX.update({lang:"en"},
                {$inc: {price: 50.00}}, 
                {multi:true})


# Consulta de datos

## Comando para hacer un all() a la coleccion(Tabla)

db.XXX.find()

## Comando para buscar con condiciones ( es como un orWhere )

db.XXX.find({ name:"Pedro", edad:27})

## Find tiene las opciones condicion, claves que quiero mostrar ( si pongo _id:0 en claves no muestra id)

db.XXX.find({ },{ name:1, edad:1 })

## Operadores 

Operador	Condición
$lt	            <
$lte	        <=
$gt	            >
$gte	        >=


 db.XXX.find({"puntuacion":{$gt:10}},{name:1,puntuacion:1})

 ## Operadores lógicos

$in	    Recupera documentos cuyo campo clave esté entre alguno de los valores especificados en el array

$nin	Recupera documentos cuyo campo clave NO esté entre alguno de los valores especificados en el array

$or	    Con el siguiente find, vamos a recuperar aquellos documentos que estén en stock (enstock:false) o que tengan editorial (editorial:null).

$nor	Con el siguiente find, vamos a recuperar aquellos documentos que no estén en stock (enstock:false) o que no tengan editorial (editorial:null).

$not	Es lo que se conoce como un metacondicional, que son opeadores que pueden aplicarse por encima de cualquier otro criterio. Su sintaxis es sencilla, solo hay que ponerlo 
        “fuera” de aquello que queremos negar.	

$exist	Se utiliza para comprobar los documentos que tienen informado o no un campo determinado	

### Devuelve los campos donde editorial tenga esos valores
db.XXX.find({editorial:{$in:["Debolsillo","Planeta","Gigamesh"]}},
              {titulo:1,editorial:1}
             )

###  Devuelve los campos donde editorial no tenga esos valores
db.XXX.find({editorial:{$nin:["Debolsillo","Planeta","Gigamesh"]}},
                {titulo:1,editorial:1}
               )
### Devuelve los cammpos donde editorial tenga o un valor u otro
db.XXX.find({$or:[{enstock:false},{editorial:null}]},
                {titulo:1,editorial:1,enstock:1}
               )
### Lo mismo que antes pero que no tenga ni uno ni otro
db.XXX.find({$nor:[{enstock:false},{editorial:null}]},
                {titulo:1,editorial:1,enstock:1}
               )
### Que no sea ese valor, pero solo sire para expresiones regulares tipo que no empiece por x o que no sea mayor o menor que
db.XXX.find( { paginas: {$not: { $eq:480 } } },
                 {titulo:1,paginas:1}
               )

### Que no sea ese valor
db.asignaturas.find({ profesor: { $ne: "Juan" } })

### Devuelve si existe páginas, si esta vacio no devuelve
db.XXX.find({paginas:{$exists:true}},{paginas:1})

### Devuelve si se cumplen las 2 condiciones AND
db.XXX.find({$and:[{enstock:false},{editorial:null}]},
                {titulo:1,editorial:1,enstock:1})


### SI hay que buscar en un json

db.libro.findOne({"autor.nacimiento.anyo":{$gt:1965}})