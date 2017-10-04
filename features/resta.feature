Feature: Resta de dos números
	Como usuario de la calculadora
	deseo realizar la resta de dos numeros
	para obtener el resultado preciso

	Scenario: Resta de 2 menos 2
		Dado que ingreso los números de resta "2" y "2"
		cuando realizo la operación
		entonces obtengo el resultado "0"

	Scenario: Resta de 7 menos 5
		Dado que ingreso los números de resta "7" y "5"
		cuando realizo la operación
		entonces obtengo el resultado "2"

	Scenario: Resta de 0 menos -7
		Dado que ingreso los números de resta "0" y "-7"
		cuando realizo la operación
		entonces obtengo el resultado "7"