import json

# Esquema de base de datos en formato diccionario
db_schema = {
    "tables": {
        "usuarios": {
            "columns": {
                "id_usuario": {
                    "type": "int",
                    "primary_key": True,
                    "auto_increment": True
                },
                "nombre": {
                    "type": "varchar",
                    "length": 100
                },
                "email": {
                    "type": "varchar",
                    "length": 100,
                    "unique": True
                },
                "password": {
                    "type": "varchar",
                    "length": 255
                },
                "id_rol": {
                    "type": "int",
                    "foreign_key": {
                        "table": "rol",
                        "column": "id_rol"
                    }
                }
            }
        },
        "rol": {
            "columns": {
                "id_rol": {
                    "type": "int",
                    "primary_key": True,
                    "auto_increment": True
                },
                "nombre_rol": {
                    "type": "varchar",
                    "length": 50
                }
            },
            "data": [
                {
                    "id_rol": 1,
                    "nombre_rol": "administrador"
                },
                {
                    "id_rol": 2,
                    "nombre_rol": "estudiante"
                }
            ]
        },
        "calificaciones": {
            "columns": {
                "id_calificacion": {
                    "type": "int",
                    "primary_key": True,
                    "auto_increment": True
                },
                "id_usuario": {
                    "type": "int",
                    "foreign_key": {
                        "table": "usuarios",
                        "column": "id_usuario"
                    }
                },
                "materia": {
                    "type": "varchar",
                    "length": 100
                },
                "calificacion": {
                    "type": "decimal",
                    "precision": 3,
                    "scale": 2
                }
            }
        },
        "becas": {
            "columns": {
                "id_beca": {
                    "type": "int",
                    "primary_key": True,
                    "auto_increment": True
                },
                "nombre_beca": {
                    "type": "varchar",
                    "length": 100
                },
                "descripcion": {
                    "type": "text"
                },
                "promedio_minimo": {
                    "type": "decimal",
                    "precision": 3,
                    "scale": 2
                },
                "id_usuario": {
                    "type": "int",
                    "foreign_key": {
                        "table": "usuarios",
                        "column": "id_usuario"
                    },
                    "nullable": True
                }
            }
        }
    }
}

# Guardar en un archivo JSON
file_path = 'db_schema.json'

with open(file_path, 'w') as json_file:
    json.dump(db_schema, json_file, indent=4)

print(f"Esquema guardado en {file_path}")
