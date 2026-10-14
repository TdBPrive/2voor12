# 2 voor 12 – stamkaarten

Flashcards om te stampen voor 2 voor 12. De kaarten komen uit `stamlijsten.xlsx`;
de webpagina (`index.html`) leest die spreadsheet in.

## Wat zit erin

| Bestand | Wat |
|---|---|
| `index.html` | De flashcard-pagina |
| `stamlijsten.xlsx` | Alle lijsten (één tabblad per lijst) + Uitleg + Opzoektips |
| `img/` | Hier kun je eigen plaatjes neerzetten |

## Lijsten aanpassen

Open `stamlijsten.xlsx` in Excel. Per tabblad: `Prio`, `Vraag` (kort), `Voorleesvraag` (uitgebreid,
zoals de presentator hem voorleest), `Antwoord` (altijd één woord of naam), `Extra`, `Afbeelding`, `Wiki`, `Al gevraagd`. Rijen toevoegen of een nieuw tabblad met dezelfde
kolommen maken mag: de pagina pakt het automatisch op.

**Plaatjes**, in deze volgorde:
1. Kolom `Afbeelding` – een webadres van een plaatje, of `img/bestandsnaam.jpg` voor een eigen plaatje in de map `img/`.
2. Kolom `Wiki` – titel van een Wikipedia-artikel; de pagina haalt dan zelf het plaatje op
   (eerst Nederlandse, dan Engelse Wikipedia). Met een `?` ervoor wordt er gezocht.
3. Bij films slaat de pagina de poster over en zoekt hij foto's van opnames, acteurs of locaties
   (echte filmstills zijn meestal auteursrechtelijk beschermd en staan niet op Wikipedia).
4. Anders zoekt de pagina een plaatje op Wikimedia Commons. Klopt het niet, klik dan op
   **Ander plaatje**, of vul de kolom `Afbeelding` in.

## Online zetten met GitHub Pages (gratis, ~5 minuten)

1. Log in op [github.com](https://github.com) (of maak een gratis account).
2. Klik rechtsboven op **+ → New repository**. Naam bijvoorbeeld `stampen`, kies **Public**, klik **Create repository**.
3. Klik op **uploading an existing file** en sleep `index.html`, `stamlijsten.xlsx`
   (en eventueel de map `img`) erin. Klik **Commit changes**.
4. Ga naar **Settings → Pages**. Kies bij *Branch* `main` en map `/ (root)`, klik **Save**.
5. Na een minuut staat de site op `https://<jouw-gebruikersnaam>.github.io/stampen/`.
   Deel die link met je teamgenoten; werkt ook op de telefoon.

Spreadsheet bijgewerkt? Upload `stamlijsten.xlsx` opnieuw (stap 3) en ververs de pagina.

Let op: met een gratis account is een Pages-site openbaar (de link is niet geheim).

## Lokaal openen

Dubbelklik je `index.html`, dan gebruikt de pagina een ingebouwde kopie van de lijsten. Heb je de spreadsheet aangepast, kies hem dan op de pagina bij "Aangepaste spreadsheet?". Online (GitHub Pages) leest de pagina altijd zelf de nieuwste `stamlijsten.xlsx`.

## Puzzels oefenen

Op het beginscherm staan drie oefenspellen:

- **Paardensprong** – 8 letters in een 3×3-raster; lees het woord met paardensprongen (begin en richting onbekend).
- **Taartpuzzel** – 9 stukken, één ontbreekt; typ de ontbrekende letter of het hele woord.
- **12-letterwoord** – jullie letters staan los (IJ telt als één); een fout beantwoorde vraag geeft een **?** op de juiste plek in het woord.
  Tik letters om ze in het woord te plaatsen, *Koop letter* onthult een **?**, *Husselen* geeft een nieuwe volgorde.
  Met *Onzekere antwoorden* (max. 6) zijn sommige letters oranje: het team weet niet zeker of het antwoord goed was.
  Elk heeft 50% kans fout te zijn; dan past die letter niet en staat er ergens een extra **?**. Na afloop zie je welke klopten.

Met *Alleen woorden uit de uitzendingen* oefen je alleen met woorden die echt in 2 voor 12 voorkwamen
(45 paardensprongen, 37 taartpuzzels, 86 twaalfletterwoorden); anders komen er extra woorden bij.

## Bediening

- Kies bij *Vraag* tussen de voorgelezen (uitgebreide) of de korte vraag.
- De luidsprekerknop leest de vraag hardop voor (Nederlandse computerstem); of zet *Vraag automatisch voorlezen* aan.
- Klik op de vraag of op **Toon antwoord** (of druk **spatie**) om het antwoord te zien.
- **→** / *Wist ik* en **←** / *Nog niet*. Kaarten die je niet wist gaan achteraan de stapel en komen pas terug als je alle andere kaarten hebt gehad.
- De voortgang wordt per apparaat en per browser bewaard. *Voortgang wissen* begint opnieuw.
- *Bladeren met plaatjes* laat alle kaarten van je selectie in één overzicht zien.
