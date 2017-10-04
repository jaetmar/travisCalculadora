Feature: Potencia de dos números
	Como usuario de la calculadora
	deseo realizar la multiplicacion de dos numeros
	para obtener el resultado preciso

	Scenario: Potencia de 2 a la 2
		Dado que ingreso los números de potencia "2" y "2"
		cuando realizo la operación
		entonces obtengo el resultado "4"

	Scenario: Potencia de 7 a la 0
		Dado que ingreso los números de potencia "7" y "0"
		cuando realizo la operación
		entonces obtengo el resultado "1"

	Scenario: Potencia de 0 a la -7
		Dado que ingreso los números de potencia "0" y "-7"
		cuando realizo la operación
		entonces obtengo el resultado "Datos Incorrectos"
