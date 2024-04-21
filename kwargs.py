def buscador_datos(*args, **kwargs):
    resultados = {}
    
    for key, data in kwargs.items():
        if sorted(data.values()) == sorted(args):
            resultados[key] = data
    
    if resultados:
        print("-" * 40)
        print("Resultados encontrados:")
        for key, value in resultados.items():
            print(f"Key: {key}")
            print("Datos:")
            for k, v in value.items():
                print(f"\t{k}: {v}")
            print("-" * 40)
    else:
        print("No se encontraron resultados.")  
    
    
    return resultados
db={
    "Persona 0":{
        "primer_nombre":"Pablo", 
        "segundo_nombre":"Diego", 
        "primer_apellido":"Maradona", 
        "segundo_apellido":"Messi"
    },
    "Persona  1":{
        "primer_nombre":"Jose", 
        "segundo_nombre":"Lucas", 
        "primer_apellido":"Mosca",
        "segundo_apellido":"Nono"
    },
    "Persona  2":{
        "primer_nombre":"Jose", 
        "segundo_nombre":"Pedro", 
        "primer_apellido":"Rodriguez",
        "segundo_apellido":"Luca"
    }
}