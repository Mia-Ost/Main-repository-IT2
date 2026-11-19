"""Arrey og dict"""
Person = [{"fornamn": "Mia", "Etternamn": "Øsetvold"}]
print(Person[0]["fornamn"])
"""dict"""
person = {"fornamn": "Mia", "Etternamn": "Øsetvold"}
print(person["fornamn"])

"""person.pop("fornamn") fjern fornamn"""

"""person = {
  "fornavn": "Per", 
  "etternavn": "Christensen"
}
for x in person:    
  print(x)
  print(person[x]) """
""".keys gir nøkler, .values gir kva nøklene aktiverer og .values gir kva biblioteket ineholder"""

sommer_ol = [
  { "årstall": 2004, "vinnertider": { "100 m": 10.93, "200 m": 22.06, "400 m": 49.41 } },
  { "årstall": 2008, "vinnertider": { "100 m": 10.78, "200 m": 21.74, "400 m": 49.62 } },
  { "årstall": 2012, "vinnertider": { "100 m": 10.75, "200 m": 21.88, "400 m": 49.55 } },
  { "årstall": 2016, "vinnertider": { "100 m": 10.71, "200 m": 21.78, "400 m": 49.44 } },
  { "årstall": 2020, "vinnertider": { "100 m": 10.61, "200 m": 21.53, "400 m": 48.36 } }
]

for x in sommer_ol:
  aar = x["årstall"]
  vinnertid_100m = x["vinnertider"]["100 m"]
  print(f"I {aar} var vinnertiden på 100 m: {vinnertid_100m}.")
