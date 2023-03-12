def arithmetic_arranger(problemas, respuestas=False):
   
        # Revisar el número de problemas aritméticos ingresados
        if len(problemas) > 5:
            return "Error: Too many problems."
        else:
            # Variables para la impresión de salida de los problemas
            primeraLinea = ""
            segundaLinea = ""
            lineaPunteada = ""
            lineaRespuesta = ""
            
            # Asignar números y operadores de la cadena en nuevas variables para su manipulación
            for problema in problemas:
                # Haciendo uso del método split, separabamos los elementos de problema que serán almacenados en numeros
                numeros = problema.split() 

                primerNumero = numeros[0]  # Corresponde al primer número
                operador = numeros[1]  # Operador para la operación a realizar
                segundoNumero = numeros[2]  # Corresponde al segundo número
                
                # Revisar que los problemas arítmeticos son números
                if not primerNumero.isnumeric() or not segundoNumero.isnumeric():
                    return "Error: Numbers must only contain digits."

                # Revisar que los números de cada operación no sean mayores de 4 dígitos
                if len(primerNumero) > 4 or len(segundoNumero) > 4:
                    return "Error: Numbers cannot be more than four digits."

                # Revisar si el operador ingresado es suma o resta
                if operador == '+':
                    respuesta = int(primerNumero) + int(segundoNumero)
                elif operador == '-':
                    respuesta = int(primerNumero) - int(segundoNumero)
                else:
                    return "Error: Operator must be '+' or '-'."

                # Haciendo uso de la función MAX, se obtiene el mayor número de la operación
                # para poder dar forma a la estructura de salida de las operaciones
                estructura = (max(len(segundoNumero), len(primerNumero)))
                # Añadimos 2 espacios, el primero para el operador (+/-) y el segundo para el espacio entre el operador y el numero más largo
                estructura = estructura + 2  

                # El método rjust alinea el texto a la derecha, completando los espacios con la variable estructura
                primeraLinea += str(primerNumero).rjust(estructura)
                # Agregando -1 a la estructura se pretende crear un espacio entre el operador y el segundo número
                segundaLinea += operador + str(segundoNumero).rjust(estructura - 1)
                # Se multiplica el caracter "-" por la estructura para que se repita el caracter el número de veces que sea el largo del número
                lineaPunteada += "-" * estructura
                # Finalmente se agrega la respuesta de la operación en nuestra variable lineaRespuesta
                lineaRespuesta += str(respuesta).rjust(estructura)

                # Agregamos los 4 espacios solicitados entre nuestras variables de salida
                if len(problemas) >= 1:
                    primeraLinea += "    "
                    segundaLinea += "    "
                    lineaPunteada += "    "
                    lineaRespuesta += "    "

                # Finalmente, si la respuesta del arreglo es verdadero se retornan las respuestas, dando fin a la iteración 
                if respuestas == True:
                    arranged_listaProblemas = (primeraLinea.rstrip() + "\n" +
                                            segundaLinea.rstrip() + '\n' +
                                            lineaPunteada.rstrip() + '\n' +
                                            lineaRespuesta.rstrip())
                else:
                    arranged_listaProblemas = (primeraLinea.rstrip() + "\n" +
                                            segundaLinea.rstrip() + '\n' +
                                            lineaPunteada.rstrip())

        return arranged_listaProblemas