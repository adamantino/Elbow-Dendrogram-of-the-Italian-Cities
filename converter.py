import json, io

with open('comuni.json') as data_file:    
    data = json.load(data_file)

regioni = set()
provincie = set()
comuni = set()
for comune in data:
    regioni.add(comune["regione"]["nome"].encode('ascii', 'ignore').decode('ascii'))
    provincie.add(comune["provincia"]["nome"].encode('ascii', 'ignore').decode('ascii'))
    comuni.add(comune["nome"].encode('ascii', 'ignore').decode('ascii'))

# remove empty province because will use 'cm' instead
provincie.discard("");

comuni_per_regione = {}
comuni_per_regione["name"] =  "Italia"


children_regioni = []
for regione in regioni:
	children_regioni.append({"name" : regione,
				 		 	 "children" : []})

comuni_per_regione["children"] = children_regioni


for provincia in data:
	for regione in comuni_per_regione["children"]:
		if regione["name"] == provincia["regione"]["nome"].encode('ascii', 'ignore').decode('ascii') and provincia["provincia"]["nome"].encode('ascii', 'ignore').decode('ascii') in provincie:
			regione["children"].append({"name" : provincia["provincia"]["nome"].encode('ascii', 'ignore').decode('ascii'), "children" : []})
			provincie.discard(provincia["provincia"]["nome"].encode('ascii', 'ignore').decode('ascii'))

			
for comune in data:
 	for regione in comuni_per_regione["children"]:
 		for provincia in regione["children"]:
 			# if province is "" we need to use the 'cm' attibute instead
 			if comune["provincia"]["nome"].encode('ascii', 'ignore').decode('ascii') == "" and provincia["name"] == comune["cm"]["nome"].encode('ascii', 'ignore').decode('ascii'):
 				provincia["children"].append({"name" : comune["nome"].encode('ascii', 'ignore').decode('ascii')})

 			if provincia["name"] == comune["provincia"]["nome"].encode('ascii', 'ignore').decode('ascii'):
 				provincia["children"].append({"name" : comune["nome"].encode('ascii', 'ignore').decode('ascii')})


with io.open('comuni_new.json', 'w', encoding='utf-8') as f:
	f.write(json.dumps(comuni_per_regione, ensure_ascii=False))



# https://bl.ocks.org/mbostock/2429963





# Enrico berton - popolamento del mercato, engagement
# Carlo federico gnechi - avvocato
# .... - operazioni internazionali (fondo d'investimento)




















# Te
# Programmatore


# Aiuto a capire
# Quale blockchain andare
# farne una noi
# se vogliamo farkla noi

# Si tratta di analisi 

# Maggio

