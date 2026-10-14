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
3. Anders zoekt de pagina een plaatje op Wikimedia Commons. Klopt het niet, klik dan op
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

## Bediening

- Kies bij *Vraag* tussen de voorgelezen (uitgebreide) of de korte vraag.
- De luidsprekerknop leest de vraag hardop voor (Nederlandse computerstem); of zet *Vraag automatisch voorlezen* aan.
- Tik op de kaart of druk **spatie** om om te draaien.
- **→** / *Wist ik* en **←** / *Nog niet*. Kaarten die je niet wist komen een paar kaarten later terug.
- De voortgang wordt per apparaat en per browser bewaard. *Voortgang wissen* begint opnieuw.
- *Bladeren met plaatjes* laat alle kaarten van je selectie in één overzicht zien.
