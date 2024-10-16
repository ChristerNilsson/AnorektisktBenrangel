import json

def indent(text):
	if len(text) == 0: return 0
	i = 0
	while text[i] == '\t': i+=1
	return i

def buildTreeFrom (text):
	lines = text.split('\n')
	root = {}
	stack = []
	for line in lines:
		# level = line.count('\t')
		level = indent(line)
		label = line.strip()
		print(level,label)
		if label == '': continue
		if len(stack) <= level: stack.append(label)
		else: stack[level] = label
		curr = root
		for i in range(level):
			curr = curr[stack[i]]
		curr[label] = {}
	return root

tree = """Arkiv
	Dokument
		2024.html
		2023.html
		2022.html
		2021.html
		2020.html
		2019.html
		2018.html
		2017.html
		2016.html
		2015.html
		2014.html
		2013.html
		2012.html
	Resultat i blixt.html
	Resultat i klassiskt.html
	Resultat i snabbschack.html
	Veckans kombination.html
	Äldre hemsida
		https://www.seniorschackstockholm.se
	Äldre hemsida (sök)
		pelle
		https://www.google.com/search?q=site:seniorschackstockholm.se		
	Övrigt.html
Externa länkar.html
Klubben
	Blanketter
		Byte av huvudklubb.pdf
		Fullmakt SrS årsmöte.pdf
		Ny medlem.pdf
		Rondlistor 4-24 deltagare.xls
	GDPR info.pdf
	Matrikel.html
	Stadgar.pdf
	Styrelse.html
	Tjänster.pdf
	Webmaster.html
Kontakt.html
Nyheter
	2024-10-22 F Christer Nilsson - Datorkalkylering.html
Program.html
Rating.html
Resultat
	Individ.html
	Lag.html"""

z = buildTreeFrom(tree)
t = json.dumps(z)
print(len(tree),'=>',len(t),'bytes')
print(t)
