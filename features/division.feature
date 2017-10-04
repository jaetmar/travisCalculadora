Feature: División de dos números
	Como usuario de la calculadora
	deseo realizar la multiplicacion de dos numeros
	para obtener el resultado preciso

	Scenario: Divison de 2 entre 2
		Dado que ingreso los números de divison "2" y "2"
		cuando realizo la operación
		entonces obtengo el resultado "1.0"

	Scenario: Divison de 7 entre 0
		Dado que ingreso los números de divison "7" y "0"
		cuando realizo la operación
		entonces obtengo el resultado "Infinito"

	Scenario: Divison de 0 entre -7
		Dado que ingreso los números de divison "0" y "-7"
		cuando realizo la operación
		entonces obtengo el resultado "0.0"
