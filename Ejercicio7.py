import re

regex = r"\d{3}[\s.-]\d{3}[\s.-]\d{2}[\s.-]\d{2}"

test_str = ("El ex presidente de Sudáfrica, Nelson Mandela, ha fallecido a los 95 años, según ha informado el presidente de Sudáfrica, Jacob Zuma, que ha añadido que se ha ido en paz en su casa de Johannesburgo, en compañía de su familia. La muerte se produjo el jueves a las 20.50 hora local, después de una larga convalecencia por una infeccion pulmonar.Nuestra nación ha perdido a su padre. Nelson Mandela nos unió y juntos nos despedimos de él”, dijo Zuma en un mensaje televisado a toda la Mtch\n"
	"darwin@gmail.com\n"
	"Fuente: https://www.ejemplos.co/texto-informativo/#ixzz6bWGojPds\n"
	"192.168.1.0\n"
	"Mi numero de celular es el 985 134 67 87\n"
	"Pedro Fernandez 984-324-56-87\n"
	"Los días 25 de Abril a las 12:00 PM comienza el horario de Verano")

matches = re.search(regex, test_str)

if matches:
    print ("Match was found at {start}-{end}: {match}".format(start = matches.start(), end = matches.end(), match = matches.group()))
    
    for groupNum in range(0, len(matches.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = matches.start(groupNum), end = matches.end(groupNum), group = matches.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.

