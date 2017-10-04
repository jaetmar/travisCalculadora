Feature: Suma de dos números
	Como usuario de la calculadora
	deseo realizar la suma de dos numeros
	para obtener el resultado preciso

	Scenario: Suma de 2 más 2
		Dado que ingreso los números "2" y "2"
		cuando realizo la operación
		entonces obtengo el resultado "4"

	Scenario: Suma de 7 más 5
		Dado que ingreso los números "7" y "5"
		cuando realizo la operación
		entonces obtengo el resultado "12"

	Scenario: Suma de 0 más -7
		Dado que ingreso los números "0" y "-7"
		cuando realizo la operación
		entonces obtengo el resultado "-7"