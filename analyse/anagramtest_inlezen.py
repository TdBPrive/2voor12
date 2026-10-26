"""Zet de tekst van de knop 'Kopieer resultaten' om naar resultaten/anagramtest_<a|b>_resultaten.json.
Gebruik: python3 anagramtest_inlezen.py b "ANAGRAMTEST-B 32/32 | woord:k:opgelost:seconden:pogingen ..."
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
test, txt = sys.argv[1].lower(), sys.argv[2]
res = {}
for part in txt.split('|', 1)[1].split():
    w, k, ok, sec, tries = part.split(':')
    res[w] = dict(k=int(k), solved=ok == '1', ms=int(float(sec) * 1000), tries=int(tries))
out = os.path.join(HERE, 'resultaten', f'anagramtest_{test}_resultaten.json')
json.dump(res, open(out, 'w'), indent=0, sort_keys=True)
print(len(res), 'resultaten opgeslagen in', out)
