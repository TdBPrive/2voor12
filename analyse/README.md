# Analyse: letters kopen bij het 12-letterwoord

Simulatie en metingen achter het beslisschema voor de laatste twee minuten van 2 voor 12.
De site zelf heeft deze map niet nodig.

## Opzetten

```sh
./setup.sh        # haalt de OpenTaal-woordenlijst en de ondertitelfrequenties op naar data/ (niet in git)
```

`sim.py` en `anagramfit.py` hebben alleen `resultaten/` en `../index.html` nodig; `setup.sh` is alleen nodig om `gangbaarheid.py` opnieuw te draaien.

## Bestanden

| Bestand | Wat |
|---|---|
| `sim.py` | De simulatie. Speelt echte rondes (`uitzending`), de 86 echte woorden (`echt`) of willekeurige OpenTaal-woorden (`lijst`) na. |
| `ijken.sh` | Hulpfunctie `run` die een instelling naast de echte cijfers zet: `. ./ijken.sh; run start=0.73 aha=0.1 rand=1.5` |
| `gangbaarheid.py` | Schat hoe gangbaar elk 12-letterwoord is (ondertitelfrequentie, samenstellingen via hun delen) → `resultaten/gangbaarheid.json` (percentiel 0–1). |
| `anagramfit.py` | Zet een anagramtest naast de voorspelling van het model: `python3 anagramfit.py test=b speler=speler2 start=0.73 aha=0.1 rand=1.5` |
| `anagramtest_inlezen.py` | Zet de tekst van de knop *Kopieer resultaten* om naar `resultaten/anagramtest_<test>_<speler>.json`: `python3 anagramtest_inlezen.py b speler2 "ANAGRAMTEST-B …"` |
| `resultaten/` | Gangbaarheid, de opgaven van anagramtest A en B, en de resultaten per speler (`anagramtest_a_speler1`, `anagramtest_b_speler1`, `anagramtest_b_speler2`). |

## Het model

- **Bord:** bij `uitzending` precies de letters die het team had (ook foute antwoorden en lege vakjes). Bij andere woorden worden fouten getrokken zoals in de uitzendingen (87 rondes S25–S26). Naast de foute antwoorden voelt een vergelijkbaar aantal goede antwoorden onzeker.
- **Mens:** kent elk woord met een kans gelijk aan zijn gangbaarheid (`basis` tilt dat op). Van woorden die je kent zie je een deel van de letters: `start` (standaard 0,5) plus `erbij` (0,05) per gekochte letter. Letters aan begin en eind (posities 1, 2, 11, 12) wegen `rand` keer zwaarder, en een gekochte letter die daar landt helpt ook `rand` keer meer. Een woord blijft een mogelijkheid zolang de zichtbare letters passen; onzekere letters, streepjes en lege vakjes tellen als joker.
- **Stoppen:** zodra er nog één mogelijkheid is. Een woord dat je niet kent schiet je per gekochte letter met kans `aha` alsnog te binnen, en bij `lezen` (9) letters op hun plek lees je het hoe dan ook.
- **Strategieën:** `willekeurig`, `schema` (onzeker eerst, dan zeldzame enkele medeklinker, nooit E of dubbele), `medeklinker eerst`, `hybride` (schema, maar bij 3+ onzeker eerst medeklinkers), `rand`, `klinker eerst` en `achteraf beste` (kent de uitkomst: ondergrens).

## Ijking (26 oktober 2026)

Beste instelling: `start=0.73 aha=0.1 rand=1.5`.

| | Gem. | 0–2 | 3–4 | 5–7 | 8+ | 0 fout | 1 | 2 | 3+ |
|---|---|---|---|---|---|---|---|---|---|
| Echte teams | 4,9 | 15% | 34% | 32% | 18% | 3,5 | 4,6 | 5,7 | 7,2 |
| Model | 5,1 | 15% | 31% | 37% | 16% | 3,4 | 5,4 | 6,3 | 6,9 |

Correlatie met de echte telling per ronde: ongeveer 0,5.

Koopvolgordes (gekochte letters, echte borden): willekeurig 5,6 · schema 5,2 · medeklinker eerst 5,3 · hybride 5,2 · achteraf beste 3,9.
Bij 3+ fouten: schema 6,9, hybride 5,9, medeklinker eerst 5,8.

## Anagramtests (26–27 oktober 2026)

32 samengestelde woorden per test, 90 s per woord, 0/2/4/6 letters al op hun plek (8 woorden elk).

| | 0 | 2 | 4 | 6 | Totaal | Binnen 30 s |
|---|---|---|---|---|---|---|
| Speler 1, test A | 0/8 | 4/8 | 4/8 | 8/8 | 16 | 14 |
| Speler 1, test B | 0/8 | 2/8 | 5/8 | 8/8 | 15 | 12 |
| Speler 2, test B | 1/8 | 0/8 | 4/8 | 5/8 | 10 | 4 |
| Model (start 0,73), test A | 0% | 44% | 88% | 83% | 17 | |
| Model (start 0,73), test B | 0% | 27% | 80% | 86% | 16 | |

- Op dezelfde woorden (test B): allebei 8, alleen speler 1 7, alleen speler 2 2. Bij 6 van de 8 gedeelde woorden was speler 1 sneller, vaak twee tot drie keer.
- Speler 1 geeft gemiddeld na ~25 s op; speler 2 gebruikt meestal de volle 90 s en probeert vaker een fout woord.
- Per speler geijkt: speler 1 ≈ `start=0.70`, speler 2 ≈ `start=0.57`. Met die waarden koopt het team in het model gemiddeld 5,5 respectievelijk 6,3 letters (`strategie=hybride`).
- Gangbaarheid maakte voor beiden nauwelijks uit: het knelpunt is het anagram, niet de woordenschat.
- Speler 1 had de woorden van test B heel kort gezien voordat hij hem maakte.

## Kanttekeningen

- Het aantal gekochte letters per ronde is geteld uit transcripties en kan een paar keer één naast zitten.
- Gangbaarheid is ruw: samenstellingen als RIOOLHEFFING komen te laag uit.
- Het model kent geen tijd; de 2 minuten zitten alleen in het beslisschema.
