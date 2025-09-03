# -*- coding: utf-8 -*-
"""
Created on Sep 03  12:30:00 2025 

@author: WilliamPerezBeltran 
"""

#####################################
# STRINGS:  basics  
#####################################



t1 = "a"
t2 = "b"
print(t1, t2) # => "a b"
gre = "ole bizarro " + "we are fucked"
print(gre) # => "ole bizarro we are fuckeb"

echo = "ole"
print(echo*3) # => " oleoleole" 

word = "python3"
print(word[:1]) # -> p
print(word[:3]) # -> pyt
print(word[:len(word)]) # -> python3
print(word[1:6]) # -> ython 
print(word[::-1]) # -> 3nohtyp  

text = " abc "
print(text.upper()) # -> ABC 
print(text.lower()) # -> ab
print(text.strip()) # ->  abc
print(text.replace("a","B")) # -> Bb
print(text.split()) # -> abc


name = "Hanoi"
score = 23.234245690
print(f"{name}  {score:.5f}")
print(f"{name:^20}")  # centra el texto en 20 espacios
print(f"{name:<20}")  # alinea a la izquierda
print(f"{name:>20}")       

text = "bananana"
print(text.count("a"))  # -> 4
print(text.find("na"))  # -> 2 que corresponde al index ( y a la primera aparicion)j
print(text.rfind("na")) # - 6 correspondel al index y a la ultima aparición 
print("na" in text)  # -> True 
print("ole" in text) # -> False

print("oe ole reo dare".split(" ")) # -> ["oe", "ole" ,"reo" ,"dare"]
print("oe,ole,reo,dare".split(",")) # -> ["oe", "ole" ,"reo" ,"dare"]
data =  "oe,ole,reo,dare".split(",")
joined = "-".join(data)
print(joined)


print("""
Información y búsqueda
len(s) → longitud.
    - s.count(sub) → cuenta apariciones.
    - s.find(sub) → primera posición, o -1 si no está.
    - s.rfind(sub) → última posición.
    - s.index(sub) → como find, pero error si no existe.
    - s.rindex(sub) → como rfind, pero error si no existe.
 
Transformación de texto
    - s.upper() → mayúsculas.
    - s.lower() → minúsculas.
    - s.capitalize() → primera letra mayúscula.
    - s.title() → cada palabra capitalizada.
    - s.swapcase() → invierte mayúsculas/minúsculas.
    - s.casefold() → versión “lower” más fuerte (útil en comparaciones).
 
Eliminación de caracteres
    - s.strip() → elimina espacios (o chars dados) al inicio/fin.
    - s.lstrip() → solo a la izquierda.
    - s.rstrip() → solo a la derecha.
 
Verificación (booleanos)
    - s.startswith(prefix) / s.endswith(suffix)
    - s.isalpha() → solo letras.
    - s.isdigit() → solo dígitos.
    - s.isalnum() → letras o dígitos.
    - s.islower() / s.isupper()
    - s.isspace() → solo espacios.
    - s.istitle() → si está en formato título.
 
Modificación estructural
    - s.replace(old, new) → reemplazo.
    - s.split(sep) → divide en lista.
    - s.rsplit(sep) → divide desde la derecha.
    - s.splitlines() → divide por saltos de línea.
    - sep.join(lista) → une lista en string.
    - s.partition(sep) → divide en (antes, sep, después).
    - s.rpartition(sep) → desde la derecha.
 
Alineación y formato
    - s.center(width) → centra el texto.
    - s.ljust(width) → alinea izquierda.
    - s.rjust(width) → alinea derecha.
    - s.zfill(width) → rellena con ceros a la izquierda.
    - s.format(...) → formateo clásico.
    - s.format_map(dict)
 
Tablas de traducción
    - s.maketrans(...) → crea tabla de traducción.
    - s.translate(tabla) → aplica la traducción.



""")




len(s)	Longitud del string	len("Hola")	4
s.count(x)	Cuenta cuántas veces aparece x	"banana".count("a")	3
s.find(x)	Índice de la primera aparición (-1 si no existe)	"banana".find("na")	










# 📌 Python 3 String Methods

| Método | Descripción | Ejemplo | Resultado |
|--------|-------------|---------|-----------|
| `len(s)` | Longitud del string | `len("Hola")` | `4` |
| `s.count(x)` | Cuenta cuántas veces aparece `x` | `"banana".count("a")` | `3` |
| `s.find(x)` | Índice de la primera aparición (`-1` si no existe) | `"banana".find("na")` | `2` |
| `s.rfind(x)` | Índice de la última aparición (`-1` si no existe) | `"banana".rfind("na")` | `4` |
| `s.index(x)` | Como `find`, pero lanza error si no existe | `"banana".index("na")` | `2` |
| `s.rindex(x)` | Como `rfind`, pero lanza error si no existe | `"banana".rindex("na")` | `4` |
| `s.upper()` | Convierte en mayúsculas | `"hola".upper()` | `"HOLA"` |
| `s.lower()` | Convierte en minúsculas | `"HOLA".lower()` | `"hola"` |
| `s.capitalize()` | Primera letra mayúscula | `"hola mundo".capitalize()` | `"Hola mundo"` |
| `s.title()` | Cada palabra con mayúscula inicial | `"hola mundo".title()` | `"Hola Mundo"` |
| `s.swapcase()` | Invierte mayúsculas/minúsculas | `"Hola".swapcase()` | `"hOLA"` |
| `s.casefold()` | Versión “lower” más agresiva (útil en comparaciones) | `"ß".casefold()` | `"ss"` |
| `s.strip()` | Elimina espacios (o chars dados) al inicio/fin | `"  hola  ".strip()` | `"hola"` |
| `s.lstrip()` | Elimina solo a la izquierda | `"  hola".lstrip()` | `"hola"` |
| `s.rstrip()` | Elimina solo a la derecha | `"hola  ".rstrip()` | `"hola"` |
| `s.startswith(x)` | Verifica prefijo | `"python".startswith("py")` | `True` |
| `s.endswith(x)` | Verifica sufijo | `"python".endswith("on")` | `True` |
| `s.isalpha()` | Solo letras | `"abc".isalpha()` | `True` |
| `s.isdigit()` | Solo dígitos | `"123".isdigit()` | `True` |
| `s.isalnum()` | Letras o dígitos | `"abc123".isalnum()` | `True` |
| `s.islower()` | ¿Está en minúsculas? | `"hola".islower()` | `True` |
| `s.isupper()` | ¿Está en mayúsculas? | `"HOLA".isupper()` | `True` |
| `s.isspace()` | ¿Solo espacios? | `"   ".isspace()` | `True` |
| `s.istitle()` | ¿Formato título? | `"Hola Mundo".istitle()` | `True` |
| `s.replace(a, b)` | Reemplaza subcadenas | `"banana".replace("a", "o")` | `"bonono"` |
| `s.split(sep)` | Divide en lista | `"a,b,c".split(",")` | `["a","b","c"]` |
| `s.rsplit(sep)` | Divide desde la derecha | `"a,b,c".rsplit(",",1)` | `["a,b","c"]` |
| `s.splitlines()` | Divide por saltos de línea | `"uno\ndos".splitlines()` | `["uno","dos"]` |
| `sep.join(lista)` | Une lista en string | `"-".join(["a","b","c"])` | `"a-b-c"` |
| `s.partition(sep)` | Divide en 3 partes (antes, sep, después) | `"python".partition("th")` | `("py","th","on")` |
| `s.rpartition(sep)` | Igual pero desde la derecha | `"python".rpartition("o")` | `("pyth","o","n")` |
| `s.center(w)` | Centra en ancho `w` | `"hi".center(6,"-")` | `"--hi--"` |
| `s.ljust(w)` | Alinea a la izquierda | `"hi".ljust(6,"-")` | `"hi----"` |
| `s.rjust(w)` | Alinea a la derecha | `"hi".rjust(6,"-")` | `"----hi"` |
| `s.zfill(w)` | Rellena con ceros a la izquierda | `"42".zfill(5)` | `"00042"` |
| `s.format(...)` | Formateo clásico | `"{} {}".format("hola","mundo")` | `"hola mundo"` |
| `s.format_map(d)` | Formateo con diccionario | `"{x}-{y}".format_map({'x':1,'y':2})` | `"1-2"` |
| `str.maketrans(...)` | Crea tabla de traducción | `str.maketrans("abc","123")` | `{97:49,98:50,99:51}` |
| `s.translate(tabla)` | Aplica la tabla creada | `"abc".translate(str.maketrans("abc","123"))` | `"123"` |































Python 3 String Methods

Búsqueda y conteo
Método	         Descripción	                                 Ejemplo	      Resultado
len(s)	        Longitud del string	                          len("Hola")	        4
s.count(x)	Cuenta cuántas veces aparece x	                  "banana".count("a")	3
s.find(x)	Índice de la primera aparición (-1 si no existe)  "banana".find("na")	2
s.rfind(x)	Índice de la última aparición (-1 si no existe)	  "banana".rfind("na")	4
s.index(x)	Como find, pero lanza error si no existe	  "banana".index("na")	2
s.rindex(x)	Como rfind, pero lanza error si no existe	  "banana".rindex("na")	4
















🔤 Transformación de texto
Método	Descripción	Ejemplo	Resultado
s.upper()	Convierte en mayúsculas	"hola".upper()	"HOLA"
s.lower()	Convierte en minúsculas	"HOLA".lower()	"hola"
s.capitalize()	Primera letra mayúscula	"hola mundo".capitalize()	"Hola mundo"
s.title()	Cada palabra con mayúscula inicial	"hola mundo".title()	"Hola Mundo"
s.swapcase()	Invierte mayúsculas/minúsculas	"Hola".swapcase()	"hOLA"
s.casefold()	Versión “lower” más agresiva	"ß".casefold()	"ss"


✂️ Limpieza de texto
Método	Descripción	Ejemplo	Resultado
s.strip()	Elimina espacios (o chars dados) al inicio/fin	" hola ".strip()	"hola"
s.lstrip()	Elimina solo a la izquierda	" hola".lstrip()	"hola"
s.rstrip()	Elimina solo a la derecha	"hola ".rstrip()	"hola"



✅ Validación de contenido
Método	Descripción	Ejemplo	Resultado
s.startswith(x)	Verifica prefijo	"python".startswith("py")	True
s.endswith(x)	Verifica sufijo	"python".endswith("on")	True
s.isalpha()	Solo letras	"abc".isalpha()	True
s.isdigit()	Solo dígitos	"123".isdigit()	True
s.isalnum()	Letras o dígitos	"abc123".isalnum()	True
s.islower()	¿Está en minúsculas?	"hola".islower()	True
s.isupper()	¿Está en mayúsculas?	"HOLA".isupper()	True
s.isspace()	¿Solo espacios?	" ".isspace()	True
s.istitle()	¿Formato título?	"Hola Mundo".istitle()	True





🔧 Modificación y reemplazo
Método	Descripción	Ejemplo	Resultado
s.replace(a, b)	Reemplaza subcadenas	"banana".replace("a", "o")	"bonono"
s.translate(tabla)	Aplica la tabla creada	"abc".translate(str.maketrans("abc","123"))	"123"
str.maketrans(...)	Crea tabla de traducción	str.maketrans("abc","123")	{97:49,98:50,99:51}


📎 División y unión
Método	Descripción	Ejemplo	Resultado
s.split(sep)	Divide en lista	"a,b,c".split(",")	["a","b","c"]
s.rsplit(sep)	Divide desde la derecha	"a,b,c".rsplit(",",1)	["a,b","c"]
s.splitlines()	Divide por saltos de línea	"uno\ndos".splitlines()	["uno","dos"]
sep.join(lista)	Une lista en string	"-".join(["a","b","c"])	"a-b-c"
s.partition(sep)	Divide en 3 partes (antes, sep, después)	"python".partition("th")	("py","th","on")
s.rpartition(sep)	Igual pero desde la derecha	"python".rpartition("o")	("pyth","o","n")



🎨 Formato y alineación
Método	Descripción	Ejemplo	Resultado
s.center(w)	Centra en ancho w	"hi".center(6,"-")	"--hi--"
s.ljust(w)	Alinea a la izquierda	"hi".ljust(6,"-")	"hi----"
s.rjust(w)	Alinea a la derecha	"hi".rjust(6,"-")	"----hi"
s.zfill(w)	Rellena con ceros a la izquierda	"42".zfill(5)	"00042"
s.format(...)	Formateo clásico	"{} {}".format("hola","mundo")	"hola mundo"
s.format_map(d)	Formateo con diccionario	"{x}-{y}".format_map({'x':1,'y':2})	"1-2"



