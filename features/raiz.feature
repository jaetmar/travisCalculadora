Feature: Raíz de dos números
	Como usuario de la calculadora
	deseo realizar la multiplicacion de dos numeros
	para obtener el resultado preciso

	Scenario: Raiz de 2 a 2
		Dado que ingreso los números de raiz "2" y "2"
		cuando realizo la operación
		entonces obtengo el resultado "1"

	Scenario: Raiz de 7 a 0
		Dado que ingreso los números de raiz "7" y "0"
		cuando realizo la operación
		entonces obtengo el resultado "Datos Incorrectos"

	Scenario: Raiz de 0 a -7
		Dado que ingreso los números de raiz "0" y "-7"
		cuando realizo la operación
		entonces obtengo el resultado "Datos Incorrectos"
