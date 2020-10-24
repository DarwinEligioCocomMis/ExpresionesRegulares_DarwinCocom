import re

regex = r"[aA-zZ]{7,}"

test_str = ("El ex presidente de Sudáfrica, Nelson Mandela, ha fallecido a los 95 años, según ha informado el presidente de Sudáfrica, Jacob Zuma, que ha añadido que se ha ido en paz en su casa de Johannesburgo, en compañía de su familia. La muerte se produjo el jueves a las 20.50 hora local, después de una larga convalecencia por una infeccion pulmonar.Nuestra nación ha perdido a su padre. Nelson Mandela nos unió y juntos nos despedimos de él”, dijo Zuma en un mensaje televisado a toda la Mtch\n"
	"darwin@gmail.com\n"
	"Fuente: https://www.ejemplos.co/texto-informativo/#ixzz6bWGojPds\n"
	"192.168.1.0\n"
	"Mi numero de celukar es el 985 134 67 87\n"
	"Pedro Fernandez 984-324-56-87\n"
	"Los días 25 de Abril a las 12:00 PM comienza el horario de Verano")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))


