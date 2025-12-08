# ¡Resuelve los retos!

## Reto 1
Accede a la web de [cryptii](https://cryptii.com) y descifra el siguiente mensaje cifrado "¡Ub YUJ Sqibfj Rfljfef ub cuzfi!" 
(sí, no te hemos dado la clave :D ... tendrás que apañarte jeje)

## Reto 2
Usando la web de [cryptii](https://cryptii.com) de nuevo, ¿deberías aceptar el mensaje "PARQUE, 20:00" 
si viene acompañado por un código de autenticación de mensajes calculado con HMAC SHA-256 que comienza por "42 AE E7 97" con Clave=1234?

## Reto 3
Ahora nos dan un mensaje cifrado con un cifrador "ya-en-serio"... ¡A ver si eres capaz de descifrarlo con [cryptii](https://cryptii.com)! 

Ojo, que el mensaje una vez descifrado debe poder leerse... tú sabrás cómo podrás pasar de bytes a texto... 
Puedes usar [BinaryHexConverters](https://www.binaryhexconverter.com/hex-to-ascii-text-converter) 
o añadir una "caja" más en el flujo de cryptii  para procesar los bytes en texto ASCII.

algoritmo := AES-128 (block cipher)

modo de operación := CTR (counter)

key := 00 11 22 33 44 55 66 77 88 99 aa bb cc dd ee ff

iv := 00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f

mensaje cifrado (bytes en hexadecimal) : =  77 ea d2 39 55 1c 7c 7e 
                                            fc fa ec 9f b0 ce 91 76 
                                            65 27 f8 63 fc f0 75 1f 
                                            a1 3c d5 04 53 d1 f4 8e 
                                            a9 2d b5 17 4a a9 ff ca 
                                            5e 53 0c 86 59 37 d1 da 
                                            06 d8 1f b3 79 cd 76 74 25

## Reto 4 (¡solo para l@s más motivad@s!)
AVISO: Es necesario saber "algo" de Python para resolver este reto.

[pyca/cryptography]() es una librería para Python que implementa herramientas criptográficas. Entre las herramientas que ofrece están los Fernets,
que cifran y autentican un mensaje que se le pase en bytes, y PBKDF2, que genera una clave simétrica de alta calidad a partir de una contraseña común. 

En la sección de su página web [Using Fernet with passwords](https://cryptography.io/en/latest/fernet/#using-passwords-with-fernet) explica como generar la clave
y usar el Fernet. 

En este mismo repositorio tienes el archivo de Python [test_Fernet.py](https://github.com/aigonzal/talks_awareness/blob/main/test_Fernet.py) que ilustra 
cómo generar una clave para el Fernet y usarla para cifrar un mensaje y guardarlo en un archivo (message.enc). 

¿Eres capaz de revertir el cifrado del programa test_fernet.py para descifrar el mesaje cifrado que se encuentra en el archivo 
[mensaje_100.enc](https://github.com/aigonzal/talks_awareness/blob/main/message_100.enc)? 

Nota: Podría no ser así... pero no somos tan malign@s, hemos usado la misma pwd y el mismo salt que se usan en test_Fernet.py... ya el mensaje no, claro :X 

