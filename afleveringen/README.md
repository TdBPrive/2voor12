# Afleveringen

`afleveringen.py` bevat de vragen van *Aflevering spelen* en controleert ze:

- de beginletters (bij personen van de achternaam) vormen precies het 12-letterwoord;
- de zoektip gebruikt alleen zoekwoorden die ook in de vraag staan (Latijnse namen uit de vraag mogen dus);
- het antwoord, of een groot deel ervan, staat niet in de vraag, niet in de zoektip en niet in een andere vraag van dezelfde aflevering.

`python3 afleveringen.py` schrijft `afleveringen.json`; die inhoud staat in `index.html` in het blok `aflData`.
