
# Python 3 String Methods

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



