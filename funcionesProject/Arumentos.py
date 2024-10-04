#Ejemplo de argumentos predeterminados

def my_function(country = "Colombia"):
    print("I am from " + country)

    #Invocar la function
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Ejemplo argumento arbitrario *args

def mostrarEstudiantes(*args):
    print("El estudiante : "+args[2])

mostrarEstudiantes("Email", "Tobias", "Linus")

#Argumentos de palabras claves

def mostrarCarros(carro1, carro2, carro3):
    print("El carro es: " + carro2)
mostrarCarros(carro1= "BMW", carro3= "ferrari", carro2= "Ford")

#Ejemplo arbitrario **kwargs

def mostrarCliente(**kwargs):
    print("Su apellido es: " + kwargs["apellido"])

mostrarCliente(nombre = "Tobias", apellido= "Refsnes")