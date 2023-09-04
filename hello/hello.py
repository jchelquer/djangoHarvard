print ("Hello, world!")
def anuncia(f):
	def envoltorio():
		print ("Se va a ejecutar")
		f()
		print ("Ejecutado")
	return envoltorio

@anuncia
def hello():
	print ("Hello")
@anuncia
def pepe():
	print ("Pepe")


hello()
pepe()
hello()