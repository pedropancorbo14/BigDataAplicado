# Insertar, Modificar y Borrar

## Listar todos los profesores:
db.profesores.find()

## Insertar un profesor y una asignatura en la colección:
db.profesores.insertOne([
    "nombre":"Pedro",
    "apellido":"López",
    "edad":28,
    "asignatura":"Matematicas"
])

db.asignaturas.insertOne([
    "nombre":"Matematicas",
    "curso":"1º",
    "alumnos":28,
    "profesor":"Pedro",
    "ingles": false
])

## Actualizar la asignatura del profesor que acabáis de insertar

db.profesores.update({name:"Pedro"},{$set:{asignatura:"Lengua"}})

## Borrar el profesor que se acaba de insertar

db.profesores.deleteOne({name:"Pedro"})

## Actualizar todas las edades de los profesores en una unidad

db.profesores.updateMany({}, { $inc: { edad: 1 } })

## Usar upsert para añadir un nuevo profesor con nombre “Aitor”, en caso de que no lo encuentre, añade un campo “Personal” con valor ”Fijo”

db.profesores.updateOne({name:"Aitor"}, {$set:{Puntuación:"Fijo}}, {upsert:true})

# Selectores de consultas

## Listar las asignaturas con 23 alumnos

db.asignaturas.find({alumnos:23})

## Listar las asignaturas con 23 alumnos o más

db.asignaturas.find({alumnos:{$gte:23}})

## Listar las asignaturas que imparte el profesor Juan

db.asignaturas.find({profesor:"Juan"})

## Listar las asignaturas que NO imparte el profesor Juan

db.asignaturas.find({ profesor: { $ne: "Juan" } })

## Listar las asignaturas que imparten Juan o Laura

db.asignaturas.find({ profesor: { $in: ["Juan", "Laura"] } })

## Listar las asignaturas que NO imparten ni Juan ni Laura

db.asignaturas.find({ profesor: { $nin: ["Juan", "Laura"] } })
