Feature: Multiplicación de dos números
	Como usuario de la calculadora
	deseo realizar la multiplicacion de dos numeros
	para obtener el resultado preciso

	Scenario: Multiplicacion de 2 por 2
		Dado que ingreso los números de multiplicacion "2" y "2"
		cuando realizo la operación
		entonces obtengo el resultado "4"

	Scenario: Multiplicacion de 7 por 5
		Dado que ingreso los números de multiplicacion "7" y "5"
		cuando realizo la operación
		entonces obtengo el resultado "35"

	Scenario: Multiplicacion de 0 por -7
		Dado que ingreso los números de multiplicacion "0" y "-7"
		cuando realizo la operación
		entonces obtengo el resultado "0"
