import json, unicodedata, sys

WP = 'Winkler Prins'
VD = 'Grote Van Dale'
BOS = 'Bosatlas'
KM = 'Kroniek van de Mensheid'
KN = 'Kroniek van Nederland'
K20 = 'Kroniek van de 20e Eeuw'
VOG = 'ANWB-vogelgids'
FLORA = 'Heukels Flora'
NAT = 'Natuurgidsen'
MED = 'Winkler Prins Medische Encyclopedie'
STZ = 'Steinz, gids voor de wereldliteratuur'
KKM = 'Kroniek van de klassieke muziek'
HIT = '50 jaar Hitparade'
SFE = 'Speelfilmencyclopedie'
FJB = 'Filmjaarboeken'
U1001 = '1001 Uitvindingen'
POP = 'Populairwetenschappelijke boekenserie'
LAPTOP = 'Laptop (Wikipedia)'


def Q(c, d, q, a, acc=(), p=False, b=(), z='', x=''):
    return dict(c=c, d=d, q=q, a=a, acc=list(acc), p=p, b=list(b), z=z, x=x)


def PS(word, x=''):
    return dict(c='Puzzel', d=2, type='ps', a=word, acc=[], b=[], z='', x=x,
                q='Paardensprong: lees het woord van acht letters met de sprong van het paard. Begin en richting zijn onbekend. De eerste letter telt.')


def TP(word, miss, x=''):
    return dict(c='Puzzel', d=2, type='tp', a=word, miss=miss, acc=[], b=[], z='', x=x,
                q='Taartpuzzel: lees de letters rond de taart, met of tegen de klok in. Eén stuk ontbreekt. De ontbrekende letter telt.')


AFL = []

# ---------------- Aflevering 1: FIETSENMAKER ----------------
AFL.append(dict(w='FIETSENMAKER', qs=[
    Q('Geschiedenis', 2,
      'Op 5 juni 1568 werden op de Grote Markt in Brussel twee edelen onthoofd op last van de hertog van Alva. Ze waren katholiek en trouw aan de koning, maar hadden geprotesteerd tegen de vervolging van protestanten. Eén van hen was de graaf van Horne. Wie was de andere graaf?',
      'Egmont', ['egmond', 'lamoraal van egmont', 'graaf van egmont'], p=True,
      b=[KN, WP], z='Kroniek van Nederland op 5 juni 1568, of Winkler Prins op Horne',
      x='Lamoraal van Egmont. Goethe schreef er een toneelstuk over, Beethoven de muziek.'),
    Q('Muziek', 1,
      'In september 1791 ging in een volkstheater in Wenen een opera in première met onder anderen de vogelvanger Papageno en de Koningin van de Nacht, die een beroemde aria met torenhoge noten zingt. Twee maanden later overleed de componist, pas 35 jaar oud. Wie was die componist?',
      'Mozart', ['wolfgang amadeus mozart'], p=True,
      b=[KKM, WP], z='Kroniek van de klassieke muziek op september 1791',
      x='Die Zauberflöte (De toverfluit).'),
    Q('Natuur', 2,
      'Welke zwart-witte vogel met een lange staart heet in het Latijn Pica pica? Hij staat bekend om zijn voorliefde voor glimmende voorwerpen, al is dat volgens onderzoek eerder een fabel.',
      'Ekster', ['ekster', 'eksters'],
      b=[VOG], z='Register achterin de vogelgids, op Pica pica',
      x='Een ekster is een kraaiachtige; in een Rossini-opera steelt hij een zilveren lepel.'),
    Q('Geschiedenis', 3,
      'In 1494 sloten Spanje en Portugal een verdrag waarin ze de nieuw ontdekte wereld onder elkaar verdeelden langs een lijn van pool tot pool, zo\'n 370 leguas (ruim 2.000 kilometer) ten westen van de Kaapverdische Eilanden. Daardoor kwam Brazilië later aan Portugal. Naar welke Spaanse plaats is dit verdrag genoemd?',
      'Tordesillas', ['verdrag van tordesillas'],
      b=[KM, WP], z='Kroniek van de Mensheid op 1494, of Winkler Prins op Kaapverdische Eilanden of Brazilië',
      x='Het verdrag werd op 7 juni 1494 getekend; de paus had al eerder een lijn getrokken.'),
    PS('NACHTUIL', 'Een nachtuil is een nachtvlinder uit een grote familie (Noctuidae).'),
    Q('Geografie', 2,
      'Welke hoofdstad aan de Golf van Guinee was vroeger het bestuurscentrum van de Britse kolonie Goudkust? Het land werd in 1957 als een van de eerste Afrikaanse kolonies onafhankelijk.',
      'Accra', ['akkra'],
      b=[BOS, WP], z='Bosatlas op Golf van Guinee, of Winkler Prins op Goudkust',
      x='De Goudkust werd Ghana, onder leiding van Kwame Nkrumah.'),
    Q('Wetenschap', 3,
      'Welk zeldzaam, keihard en uiterst corrosiebestendig metaal heeft atoomnummer 77? Het werd in 1803 ontdekt door Smithson Tennant en is genoemd naar de Griekse godin van de regenboog, omdat de zouten ervan zoveel verschillende kleuren hebben.',
      'Iridium',
      b=[WP, POP], z='Winkler Prins op regenboog, of de elementen op atoomnummer 77',
      x='Een iridiumlaag in gesteente van 66 miljoen jaar oud wees op de meteorietinslag die de dinosauriërs uitroeide.'),
    Q('Medisch', 2,
      'Het onderbeen heeft twee pijpbeenderen: het scheenbeen, in het Latijn tibia, en het dunnere kuitbeen aan de buitenkant. Wat is de Latijnse naam van het kuitbeen?',
      'Fibula', ['fibulae'],
      b=[MED, VD], z='Medische Encyclopedie op kuitbeen',
      x='Fibula betekent ook "mantelspeld"; het bot zou op de pin van zo\'n speld lijken.'),
    Q('Kunst', 1,
      'Welke Nederlandse graficus, in 1898 geboren in Leeuwarden, maakte onmogelijke bouwwerken zoals "Klimmen en dalen", waarop monniken eindeloos een trap op lopen, en de litho met twee handen die elkaar tekenen?',
      'Escher', ['m.c. escher', 'mc escher', 'maurits escher'], p=True,
      b=[WP], z='Winkler Prins op Leeuwarden of op Klimmen en dalen',
      x='Maurits Cornelis Escher (1898-1972). In Den Haag staat Escher in Het Paleis.'),
    Q('Sport', 1,
      'Welke racketsport wordt gespeeld in een gesloten zaal, waarbij twee spelers om beurten een kleine, nauwelijks stuiterende bal tegen de voorwand slaan en ook de zijwanden en achterwand gebruikt mogen worden?',
      'Squash',
      b=[WP], z='Winkler Prins op racket / balsporten',
      x='Squash ontstond rond 1830 op de Engelse kostschool Harrow.'),
    Q('Film', 1,
      'Welke Amerikaanse regisseur maakte "2001: A Space Odyssey", "A Clockwork Orange", "The Shining" met Jack Nicholson, en de oorlogsfilm "Full Metal Jacket"?',
      'Kubrick', ['stanley kubrick'], p=True,
      b=[SFE, FJB], z='Speelfilmencyclopedie op The Shining of Full Metal Jacket (zoeken kan alleen op titel)',
      x='Stanley Kubrick (1928-1999).'),
    Q('Geschiedenis', 2,
      'Welke Franse revolutionair, bijgenaamd "l\'Incorruptible" (de onkreukbare), leidde tijdens het Schrikbewind het Comité van Openbaar Welzijn en werd in juli 1794 zelf onder de guillotine gebracht?',
      'Robespierre', ['maximilien robespierre', 'maximilien de robespierre'], p=True,
      b=[KM, WP], z='Kroniek van de Mensheid op juli 1794, of Winkler Prins op Schrikbewind',
      x='Maximilien de Robespierre, onthoofd op 28 juli 1794.'),
]))

# ---------------- Aflevering 2: TUINKABOUTER ----------------
AFL.append(dict(w='TUINKABOUTER', qs=[
    Q('Geografie', 1,
      'Welk Zuid-Amerikaans land, ingeklemd tussen Brazilië en Argentinië, heeft Montevideo als hoofdstad en won in 1930 het allereerste wereldkampioenschap voetbal, dat het ook zelf organiseerde?',
      'Uruguay',
      b=[BOS, WP], z='Bosatlas: register op Montevideo',
      x='Uruguay won in 1950 nog een keer, in Brazilië.'),
    Q('Natuur', 3,
      'Welke grote, geel-zwarte dagvlinder met twee staartjes aan de achtervleugels heet in het Latijn Papilio machaon? In Nederland is hij zeldzaam; de rupsen eten van wilde peen en venkel.',
      'Koninginnenpage', ['koninginnepage'],
      b=[NAT, WP], z='Register achterin een natuurgids, op Papilio machaon',
      x='Hij is familie van de nog zeldzamere koningspage.'),
    Q('Muziek', 1,
      'Welke Russische componist schreef de balletten "Het Zwanenmeer", "De Schone Slaapster" en "De Notenkraker", en ook de "1812-ouverture" met echte kanonschoten?',
      'Tsjaikovski', ['tchaikovsky', 'tsjaikovsky', 'tchaikovski', 'pjotr iljitsj tsjaikovski', 'tjaikovski'], p=True,
      b=[KKM, WP], z='Winkler Prins op Notenkraker of Zwanenmeer',
      x='Pjotr Iljitsj Tsjaikovski (1840-1893).'),
    Q('Geschiedenis', 2,
      'Welke liberale staatsman schreef in het revolutiejaar 1848 de grondwetsherziening die van Nederland een parlementaire democratie maakte, waarin de ministers verantwoordelijk werden in plaats van de koning?',
      'Thorbecke', ['johan rudolph thorbecke', 'j.r. thorbecke'], p=True,
      b=[KN, WP], z='Kroniek van Nederland op 1848, of Winkler Prins op grondwet',
      x='Johan Rudolph Thorbecke. Zijn standbeeld staat op het Thorbeckeplein in Amsterdam.'),
    Q('Medisch', 2,
      'Welk hormoon, gemaakt in de eilandjes van Langerhans in de alvleesklier, verlaagt het suikergehalte van het bloed? Frederick Banting en Charles Best isoleerden het in 1921 in Toronto.',
      'Insuline', ['insulin'],
      b=[MED, U1001], z='Medische Encyclopedie op alvleesklier of eilandjes van Langerhans',
      x='Banting kreeg er in 1923 de Nobelprijs voor, samen met Macleod.'),
    Q('Natuur', 2,
      'Welke zwarte watervogel, Phalacrocorax carbo, zie je vaak met gespreide vleugels op een paal zitten om zijn veren te laten drogen?',
      'Aalscholver', ['aalscholvers'],
      b=[VOG], z='Register achterin de vogelgids, op Phalacrocorax',
      x='In China en Japan worden aalscholvers van oudsher voor de visvangst gebruikt.'),
    TP('TROMPETER', 2, 'Een trompetter is ook een vogel en een zwaan (trompetzwaan).'),
    Q('Geschiedenis', 1,
      'Welke Romeinse keizer zou volgens de overlevering op zijn lier hebben gespeeld terwijl Rome in het jaar 64 brandde? Hij gaf de christenen de schuld en liet later een enorm paleis bouwen, het Gouden Huis.',
      'Nero', ['keizer nero'], p=True,
      b=[KM, WP], z='Kroniek van de Mensheid op het jaar 64',
      x='Nero pleegde in 68 zelfmoord.'),
    Q('Kunst', 2,
      'Welke Zuid-Nederlandse schilder uit de zestiende eeuw maakte "De boerenbruiloft", "De jagers in de sneeuw" en "De toren van Babel", die in Museum Boijmans Van Beuningen hangt in een kleinere versie?',
      'Bruegel', ['brueghel', 'breughel', 'pieter bruegel', 'pieter brueghel'], p=True,
      b=[WP], z='Winkler Prins op Toren van Babel of Jagers in de sneeuw',
      x='Pieter Bruegel de Oude (ca. 1525-1569).'),
    Q('Wetenschap', 2,
      'Welke planeet werd in 1781 ontdekt door William Herschel, als eerste planeet die met een telescoop werd gevonden? Hij draait bijna op zijn kant, met de as in het vlak van zijn baan.',
      'Uranus',
      b=[POP, WP], z='Het Astronomieboek op 1781, of Winkler Prins op Herschel',
      x='Herschel wilde hem naar koning George III noemen.'),
    Q('Wetenschap', 2,
      'Welke Griekse wiskundige uit Alexandrië schreef rond 300 voor Christus "De Elementen", tweeduizend jaar lang hét leerboek meetkunde, met onder meer het bewijs dat er oneindig veel priemgetallen zijn?',
      'Euclides', ['euclid', 'eukleides'], p=True,
      b=[POP, WP], z='Het Wiskundeboek (op jaartal) rond 300 voor Christus, of Winkler Prins op Alexandrië',
      x='Naar hem heet de euclidische meetkunde.'),
    Q('Literatuur', 2,
      'Welke schrijver debuteerde in 1947 met "De avonden", over tien decemberavonden van de kantoorklerk Frits van Egters, en is samen met Hermans en Mulisch een van de Grote Drie?',
      'Reve', ['gerard reve', 'van het reve', 'simon van het reve'], p=True,
      b=[STZ, WP], z='Steinz: register achterin op de titel De avonden',
      x='Gerard Reve (1923-2006); het boek verscheen onder het pseudoniem Simon van het Reve.'),
]))

# ---------------- Aflevering 3: SCHOENENKAST ----------------
AFL.append(dict(w='SCHOENENKAST', qs=[
    Q('Geschiedenis', 1,
      'Welke Romeinse veldheer stak in januari 49 voor Christus met zijn leger de rivier de Rubicon over, wat een burgeroorlog ontketende? Hij zou daarbij "Alea iacta est" (de teerling is geworpen) hebben gezegd.',
      'Caesar', ['julius caesar', 'gaius julius caesar', 'cesar'], p=True,
      b=[KM, WP], z='Winkler Prins op Rubicon',
      x='Gaius Julius Caesar, vermoord op de Iden van maart in 44 v.Chr.'),
    Q('Geografie', 2,
      'Welke rivier vormt samen met haar zijrivier de Neisse een groot deel van de grens tussen Duitsland en Polen, en mondt bij Szczecin uit in de Oostzee?',
      'Oder', ['odra'],
      b=[BOS, WP], z='Bosatlas: register op Szczecin, dan de rivier volgen',
      x='De Oder-Neissegrens werd in 1945 vastgelegd in Potsdam.'),
    Q('Natuur', 1,
      'Welk roodbruin knaagdier met pluimoortjes heet in het Latijn Sciurus vulgaris? Het verstopt in de herfst noten in de grond en vergeet een deel daarvan, waardoor het bijdraagt aan nieuwe bomen.',
      'Eekhoorn', ['eekhoren', 'rode eekhoorn'],
      b=[NAT, WP], z='Register van een natuurgids, op Sciurus',
      x='In Engeland is de rode eekhoorn grotendeels verdrongen door de Amerikaanse grijze.'),
    Q('Muziek', 2,
      'Welke Engelse componist schreef de "Enigma-variaties" en de marsen "Pomp and Circumstance", waarvan er één met de tekst "Land of Hope and Glory" elk jaar op de Last Night of the Proms wordt gezongen?',
      'Elgar', ['edward elgar'], p=True,
      b=[KKM, WP], z='Winkler Prins op Pomp and Circumstance of Enigma-variaties',
      x='Sir Edward Elgar (1857-1934). Zijn portret stond op het Britse biljet van 20 pond.'),
    Q('Geschiedenis', 3,
      'In 1672, het Rampjaar, vielen Frankrijk, Engeland en twee Duitse bisdommen de Republiek aan. In welke Gelderse stad werd in 1678 de vrede gesloten die de oorlog met Frankrijk beëindigde?',
      'Nijmegen', ['vrede van nijmegen'],
      b=[KN, WP], z='Kroniek van Nederland op 1678',
      x='Het was een van de eerste grote Europese vredescongressen; Lodewijk XIV gaf Maastricht terug.'),
    PS('HOOGLAND'),
    Q('Wetenschap', 1,
      'Welk edelgas met atoomnummer 10 geeft in een gasontladingsbuis een feloranjerood licht, en is daarom de naamgever van reclameverlichting?',
      'Neon',
      b=[WP, POP], z='Winkler Prins op edelgas, of de elementen op atoomnummer 10',
      x='Ontdekt in 1898 door Ramsay en Travers; de naam komt van het Griekse neos, nieuw.'),
    Q('Medisch', 2,
      'Welke besmettelijke kinderziekte, veroorzaakt door de bacterie Bordetella pertussis, geeft wekenlang hevige aanvallen met een gierende, piepende inademing en is voor zuigelingen levensgevaarlijk? Baby\'s worden ertegen ingeënt, en zwangeren krijgen er tegenwoordig ook een prik tegen.',
      'Kinkhoest',
      b=[MED], z='Medische Encyclopedie op Bordetella pertussis',
      x='In China heet het de honderddagenhoest.'),
    Q('Literatuur', 1,
      'Welke Deense schrijver uit Odense schreef sprookjes als "Het lelijke jonge eendje", "De kleine zeemeermin" en "De nieuwe kleren van de keizer"?',
      'Andersen', ['hans christian andersen', 'h.c. andersen', 'hc andersen'], p=True,
      b=[STZ, WP], z='Steinz: register op De kleine zeemeermin',
      x='Hans Christian Andersen (1805-1875). Het beeld van de kleine zeemeermin staat in Kopenhagen.'),
    Q('Sport', 2,
      'In welke Japanse vechtsport proberen zware worstelaars elkaar uit een cirkelvormige ring van klei, de dohyo, te duwen of de grond te laten raken met iets anders dan de voetzolen? De hoogste rang is yokozuna.',
      'Sumo', ['sumoworstelen', 'sumo worstelen'],
      b=[WP, VD], z='Van Dale of Winkler Prins op yokozuna',
      x='Voor de wedstrijd strooien de worstelaars zout om de ring te reinigen.'),
    Q('Film', 1,
      'Welke Amerikaanse regisseur maakte "Jaws", "E.T. the Extra-Terrestrial" en "Schindler\'s List", en won voor die laatste film en voor "Saving Private Ryan" de Oscar voor beste regie?',
      'Spielberg', ['steven spielberg'], p=True,
      b=[SFE, FJB], z='Speelfilmencyclopedie op de titel Jaws',
      x='Steven Spielberg (1946).'),
    Q('Taal', 3,
      'Hoe heet de stijlfiguur waarin twee woorden van dezelfde woordsoort met (bijna) dezelfde betekenis naast elkaar staan, zoals in "oud en bejaard", "vrede en rust" of "nooit en te nimmer"? Het is iets anders dan een pleonasme zoals "een witte schimmel".',
      'Tautologie', ['tautologieen'],
      b=[VD], z='Van Dale op pleonasme',
      x='Bij een pleonasme herhaalt een bijvoeglijk naamwoord een eigenschap die al in het zelfstandig naamwoord zit.'),
]))

# ---------------- Aflevering 4: BOSWANDELING ----------------
AFL.append(dict(w='BOSWANDELING', qs=[
    Q('Geschiedenis', 1,
      'Bij welk dorp ten zuiden van Brussel werd Napoleon op 18 juni 1815 definitief verslagen door de Britten onder Wellington en de Pruisen onder Blücher? Ook de Nederlandse kroonprins, de latere Willem II, raakte er gewond.',
      'Waterloo',
      b=[KM, WP], z='Kroniek van de Mensheid op 18 juni 1815',
      x='Na de slag werd Napoleon verbannen naar Sint-Helena.'),
    Q('Natuur', 2,
      'Welke bruine zangvogel, Luscinia megarhynchos, is onopvallend van uiterlijk maar beroemd om zijn zang, vaak ook \'s nachts? In de Amsterdamse Waterleidingduinen kun je hem in mei volop horen.',
      'Nachtegaal', ['nachtegalen'],
      b=[VOG], z='Register achterin de vogelgids, op Luscinia',
      x='Van de nachtegaal zingt alleen het mannetje.'),
    Q('Muziek', 1,
      'Welke componist, geboren in Bonn, was al grotendeels doof toen hij zijn Negende symfonie schreef, met in het slotdeel het koor "Ode an die Freude", dat nu het Europese volkslied is?',
      'Beethoven', ['ludwig van beethoven'], p=True,
      b=[KKM, WP], z='Winkler Prins op Ode an die Freude of op Bonn',
      x='Ludwig van Beethoven (1770-1827).'),
    Q('Geschiedenis', 2,
      'Welke landsadvocaat van Holland, jarenlang de machtigste politicus van de Republiek, kwam in conflict met prins Maurits over het Twaalfjarig Bestand en de godsdiensttwisten, en werd in mei 1619 op het Binnenhof onthoofd?',
      'Oldenbarnevelt', ['van oldenbarnevelt', 'johan van oldenbarnevelt'], p=True,
      b=[KN, WP], z='Kroniek van Nederland op mei 1619',
      x='Johan van Oldenbarnevelt was 71 toen hij werd onthoofd. Hugo de Groot kreeg levenslang en ontsnapte later in een boekenkist.'),
    Q('Natuur', 2,
      'Welke plant, in het Latijn Galanthus nivalis, bloeit vaak al in januari of februari met kleine witte, hangende bloemetjes met groene vlekjes, en staat in Nederland veel op oude landgoederen als stinsenplant?',
      'Sneeuwklokje', ['sneeuwklokjes', 'sneeuwklok'],
      b=[FLORA], z='Register achterin de Heukels, op Galanthus',
      x='Het bloeit soms letterlijk door de sneeuw heen.'),
    Q('Geografie', 2,
      'Welke Afrikaanse hoofdstad, op zo\'n 2.400 meter hoogte, is de zetel van de Afrikaanse Unie? De naam betekent "nieuwe bloem".',
      'Addis Abeba', ['addis ababa', 'addis'],
      b=[BOS, WP], z='Winkler Prins op Afrikaanse Unie',
      x='Addis Abeba is de hoofdstad van Ethiopië.'),
    Q('Literatuur', 1,
      'Welke Engelse schrijver beschreef het leven van arme kinderen in Londen in boeken als "Oliver Twist" en "David Copperfield", en schreef "A Christmas Carol" over de vrekkige Ebenezer Scrooge?',
      'Dickens', ['charles dickens'], p=True,
      b=[STZ, WP], z='Steinz: register op Oliver Twist',
      x='Charles Dickens (1812-1870).'),
    TP('LEGPUZZEL', 2),
    Q('Medisch', 3,
      'Hoe heet de medisch specialist, meestal een internist, die zich bezighoudt met hormonen en de klieren die ze maken, zoals de schildklier en de bijnieren, en die bijvoorbeeld de ziekte van Graves behandelt?',
      'Endocrinoloog', ['endocrinologie', 'endocrinologe'],
      b=[MED, VD], z='Medische Encyclopedie op hormoon of schildklier',
      x='Endocrien betekent "naar binnen afscheidend": de klieren geven hun stoffen af aan het bloed.'),
    Q('Geschiedenis', 1,
      'Welke Russische revolutionair keerde in april 1917 met hulp van Duitsland in een verzegelde trein terug uit Zwitserland en leidde in november van dat jaar de bolsjewistische Oktoberrevolutie? Zijn gebalsemde lichaam ligt nog altijd op het Rode Plein.',
      'Lenin', ['vladimir lenin', 'oeljanov', 'vladimir iljitsj lenin'], p=True,
      b=[K20, WP], z='Kroniek van de 20e Eeuw op november 1917',
      x='Lenin is een schuilnaam; hij heette Vladimir Iljitsj Oeljanov.'),
    Q('Wetenschap', 2,
      'Hoe noem je atomen van hetzelfde scheikundige element die een verschillend aantal neutronen in hun kern hebben, zoals koolstof-12 en het radioactieve koolstof-14, dat gebruikt wordt om de ouderdom van fossielen te bepalen?',
      'Isotoop', ['isotopen'],
      b=[WP, POP], z='Winkler Prins op koolstof-14',
      x='Isotoop betekent "op dezelfde plaats": in het periodiek systeem.'),
    Q('Film', 1,
      'Welke Britse regisseur maakte "Inception", "Interstellar", de Batman-trilogie "The Dark Knight" en "Oppenheimer", waarvoor hij in 2024 de Oscar voor beste regie kreeg?',
      'Nolan', ['christopher nolan'], p=True,
      b=[FJB, SFE], z='Speelfilmencyclopedie of Filmjaarboek op Inception of Oppenheimer (zoeken op titel)',
      x='Christopher Nolan (1970).'),
]))

# ---------------- Aflevering 5: TREINKAARTJE ----------------
AFL.append(dict(w='TREINKAARTJE', qs=[
    Q('Muziek', 2,
      'Welke Franse componist schreef in 1928 de "Boléro", waarin hetzelfde thema steeds luider wordt herhaald boven een onafgebroken trommelritme? Ook "Pavane voor een dode prinses" is van hem.',
      'Ravel', ['maurice ravel'], p=True,
      b=[KKM, WP], z='Kroniek van de klassieke muziek op 1928',
      x='Maurice Ravel (1875-1937). Hij noemde de Boléro zelf "een stuk zonder muziek".'),
    Q('Geschiedenis', 2,
      'Hoe heet het verdrag waarmee de Republiek en Spanje in 1609, midden in hun oorlog, voor een vaste periode de wapens neerlegden? Het liep af in 1621, waarna de strijd weer begon.',
      'Twaalfjarig Bestand', ['het twaalfjarig bestand', 'twaalfjarig'],
      b=[KN, WP], z='Kroniek van Nederland op 1609',
      x='Tijdens het Bestand laaide de strijd tussen remonstranten en contraremonstranten op.'),
    Q('Natuur', 3,
      'Welke loofboom, Alnus glutinosa, groeit graag op natte grond langs beken en heeft als enige inheemse loofboom kleine houtige kegeltjes? Zijn hout werd vroeger gebruikt voor klompen en voor palen onder water.',
      'Els', ['zwarte els', 'elzen'],
      b=[FLORA], z='Register achterin de Heukels, op Alnus',
      x='Elzenhout wordt onder water juist sterker; Venetië staat deels op elzenpalen.'),
    Q('Wetenschap', 1,
      'Welke Griekse geleerde uit Syracuse zou "Eureka!" hebben geroepen toen hij in bad ontdekte hoe hij het volume van een kroon kon meten? De wet van de opwaartse kracht is naar hem genoemd.',
      'Archimedes', p=True,
      b=[POP, WP], z='Winkler Prins op opwaartse kracht of op Syracuse',
      x='Archimedes kwam in 212 v.Chr. om toen de Romeinen Syracuse innamen.'),
    Q('Geografie', 1,
      'Welk land, met Teheran als hoofdstad, heette tot 1935 internationaal Perzië?',
      'Iran',
      b=[BOS, WP], z='Bosatlas: register op Teheran',
      x='In 1979 verdreef de islamitische revolutie de sjah.'),
    PS('KAPSALON', 'Ook een Rotterdams gerecht: patat, shoarma, kaas en salade in één bakje.'),
    Q('Geschiedenis', 3,
      'Welke Egyptische president nationaliseerde in juli 1956 het Suezkanaal, waarna Groot-Brittannië, Frankrijk en Israël Egypte aanvielen en onder druk van de VS en de Sovjet-Unie weer moesten terugtrekken?',
      'Nasser', ['gamal abdel nasser', 'abdel nasser'], p=True,
      b=[K20, WP], z='Kroniek van de 20e Eeuw op juli 1956, of Winkler Prins op Suezkanaal',
      x='Gamal Abdel Nasser (1918-1970).'),
    Q('Kunst', 2,
      'Welke Amsterdamse kunstenaar van de Cobra-beweging zorgde in 1949 voor ophef met zijn muurschildering "Vragende kinderen" in het Amsterdamse stadhuis? Die werd jarenlang achter behang verborgen.',
      'Appel', ['karel appel'], p=True,
      b=[WP], z='Winkler Prins op Cobra',
      x='Karel Appel (1921-2006): "Ik rotzooi maar wat aan."'),
    Q('Sport', 1,
      'In welke balsport met een ovale bal proberen twee ploegen van vijftien spelers een "try" te scoren door de bal achter de doellijn op de grond te drukken? Spelregelovertredingen leiden vaak tot een "scrum".',
      'Rugby', ['rugby union'],
      b=[WP], z='Winkler Prins op scrum of balsporten',
      x='Volgens de legende pakte William Webb Ellis in 1823 op de school in Rugby de bal op en liep ermee weg.'),
    Q('Film', 1,
      'Welke Amerikaanse regisseur maakte "Reservoir Dogs", "Pulp Fiction", dat in 1994 de Gouden Palm won, en de tweedelige wraakfilm "Kill Bill"?',
      'Tarantino', ['quentin tarantino'], p=True,
      b=[SFE, FJB], z='Speelfilmencyclopedie op de titel Pulp Fiction',
      x='Quentin Tarantino (1963).'),
    Q('Literatuur', 2,
      'Welke Ierse schrijver liet zijn roman "Ulysses" uit 1922 zich afspelen op één dag in Dublin, 16 juni 1904? Die dag wordt elk jaar gevierd als Bloomsday, naar de hoofdpersoon Leopold Bloom.',
      'Joyce', ['james joyce'], p=True,
      b=[STZ, WP], z='Steinz: register op de titel Ulysses',
      x='James Joyce (1882-1941).'),
    Q('Medisch', 1,
      'Hoe heet de hersenaandoening waarbij iemand terugkerende aanvallen krijgt door een plotselinge ontlading van zenuwcellen, soms met bewusteloosheid en schokken? Vroeger heette het "vallende ziekte".',
      'Epilepsie', ['epilepsia'],
      b=[MED], z='Medische Encyclopedie op vallende ziekte',
      x='Een EEG meet de hersenactiviteit om de aanvallen te onderzoeken.'),
]))

AANZ = 'Het Aanzien van … (per jaar)'
JB = 'Jaarboeken'
def ACT(q, a, acc=(), p=True, b=(AANZ, JB, LAPTOP), z='', x='', d=2):
    return Q('Actualiteit', d, q, a, acc, p=p, b=b, z=z, x=x)

REPL = {
 # aflevering 1
 (0, 'Fibula'): ACT('Op 14 januari 2024 deed koningin Margrethe II van Denemarken na 52 jaar troonsafstand. Onder welke naam besteeg haar zoon de troon als de tiende met die naam?',
      'Frederik', ['frederik x', 'frederik de tiende', 'frederick'], p=False, d=1, z='Het Aanzien van 2024 of het jaarboek op 14 januari', x='Koning Frederik X; zijn vrouw is de Australische Mary Donaldson.'),
 (0, 'Squash'): ACT('Welke voormalige topambtenaar, eerder onder meer directeur van de AIVD en Nationaal Coördinator Terrorismebestrijding, werd in juli 2024 als partijloze minister-president beëdigd van het kabinet van PVV, VVD, NSC en BBB?',
      'Schoof', ['dick schoof'], d=1, z='Het Aanzien van 2024 (juli), of Winkler Prins op AIVD', x='Dick Schoof; het kabinet viel in juni 2025 toen de PVV eruit stapte.'),
 # aflevering 2
 (1, 'Thorbecke'): ACT('Welke Britse premier hield het in het najaar van 2022 maar 49 dagen vol, na een "minibegroting" met ongedekte belastingverlagingen die de pond deed kelderen? Een tabloid liet via een livestream zien dat een krop sla het langer volhield.',
      'Truss', ['liz truss', 'elizabeth truss'], d=2, z='Het Aanzien van 2022 (najaar), of de laptop op minibegroting', x='Liz Truss werd opgevolgd door Rishi Sunak.'),
 (1, 'Aalscholver'): ACT('Welke Labor-politicus is sinds mei 2022 premier van Australië en werd in mei 2025 met een ruime meerderheid herkozen?',
      'Albanese', ['anthony albanese'], d=3, z='Laptop op premier van Australië', x='Anthony Albanese volgde Scott Morrison op.'),
 # aflevering 3
 (2, 'Caesar'): ACT('Welke Britse koning werd op 6 mei 2023 in Westminster Abbey gekroond, ruim acht maanden nadat hij zijn moeder was opgevolgd?',
      'Charles', ['charles iii', 'karel', 'karel iii', 'koning charles'], p=False, d=1, z='Het Aanzien van 2023 op 6 mei', x='Charles III; zijn vrouw Camilla werd tegelijk tot koningin gekroond.'),
 (2, 'Spielberg'): ACT('Welke Conservatieve politicus werd in oktober 2022 de eerste Britse premier van Indiase afkomst, en verloor in juli 2024 de verkiezingen van Keir Starmer?',
      'Sunak', ['rishi sunak'], d=1, z='Het Aanzien van 2022 (oktober) of 2024 (juli)', x='Rishi Sunak was eerder minister van Financiën onder Boris Johnson.'),
 # aflevering 4
 (3, 'Waterloo'): ACT('Welke partijleider won met zijn partij op 22 november 2023 onverwacht de Tweede Kamerverkiezingen, met 37 zetels?',
      'Wilders', ['geert wilders'], d=1, z='Het Aanzien van 2023 op 22 november', x='Geert Wilders, PVV. Hij werd zelf geen premier.'),
 (3, 'Nachtegaal'): ACT('Welke Russische oppositieleider, die in 2020 een vergiftiging met novitsjok overleefde, overleed op 16 februari 2024 in een strafkamp boven de poolcirkel?',
      'Navalny', ['navalni', 'navalnyj', 'aleksej navalny', 'alexei navalny'], d=2, z='Het Aanzien van 2024 op 16 februari', x='Aleksej Navalny; zijn weduwe Joelia Navalnaja zet zijn werk voort.'),
 # aflevering 5
 (4, 'Rugby'): ACT('Welke langstzittende premier van Nederland, van 2010 tot 2024, werd op 1 oktober 2024 secretaris-generaal van de NAVO?',
      'Rutte', ['mark rutte'], d=1, z='Het Aanzien van 2024 op 1 oktober', x='Mark Rutte volgde de Noor Jens Stoltenberg op.'),
 (4, 'Tarantino'): ACT('Welke politica van de Liberaal-Democratische Partij werd in oktober 2025 de eerste vrouwelijke premier van Japan? Ze geldt als politiek erfgenaam van de vermoorde oud-premier Shinzo Abe.',
      'Takaichi', ['sanae takaichi'], d=3, z='Het Aanzien van 2025 (oktober), of de laptop op premier van Japan', x='Sanae Takaichi, ooit drummer in een heavymetalband.'),
}
for (i, a), new in REPL.items():
    j = next(j for j, q in enumerate(AFL[i]['qs']) if q['a'] == a)
    AFL[i]['qs'][j] = new


def tiles(w):
    import re
    w = unicodedata.normalize('NFD', w.upper())
    w = ''.join(ch for ch in w if not unicodedata.combining(ch))
    return re.findall(r'IJ|[A-Z]', w)


def letter(q):
    if q.get('type') == 'ps':
        return tiles(q['a'])[0]
    if q.get('type') == 'tp':
        return tiles(q['a'])[q['miss']]
    return tiles(q['a'].split()[0] if not q.get('p') else q['a'].split()[-1])[0]


import re as _re
def _n(s): return _re.sub(r'[^a-z ]', ' ', unicodedata.normalize('NFD', s.lower()).encode('ascii', 'ignore').decode())
# Het antwoord (of een groot deel ervan) mag niet in de vraag, de zoektip of een andere vraag van dezelfde aflevering staan.
# Korte woorden (< 4 letters, zoals lidwoorden) tellen niet; woorden t/m 5 letters moeten heel voorkomen, langere voor 60% (minstens 5 letters). Toegestane uitzonderingen staan in OK_HIT.
OK_HIT = {('Andersen', 'ander'), ('Andersen', 'nders'), ('Andersen', 'derse')}  # 'anders', 'andere': gewone woorden
def leaks(E):
    out = []
    for k, q in enumerate(E['qs']):
        if q.get('type'): continue
        ws = [w for w in _n(q['a']).split() if len(w) >= 4]
        for j, o in enumerate(E['qs']):
            txt = _n(o['q'] + ' ' + (o.get('z') or '' if j == k else ''))
            for w in ws:
                L = len(w) if len(w) <= 5 else max(5, -(-len(w) * 3 // 5))
                for a in range(len(w) - L + 1):
                    sub = w[a:a + L]
                    if sub in txt and (q['a'], sub) not in OK_HIT:
                        out.append((q['a'], j + 1, sub))
    return out

# De zoektip mag alleen zoekwoorden bevatten die ook in de vraag staan (naast boeknamen en verbindingswoorden).
BOEKWOORDEN = set(_n(' '.join([WP, VD, BOS, KM, KN, K20, VOG, FLORA, NAT, MED, STZ, KKM, HIT, SFE, FJB, U1001, POP, LAPTOP, AANZ, JB,
    'Kroniek Aanzien Medische Encyclopedie Steinz Heukels Speelfilmencyclopedie Filmjaarboek Wiskundeboek Natuurkundeboek Astronomieboek vogelgids natuurgids jaarboek laptop'])).split())
TIPWOORDEN = set('op of de het een van en in register achterin kaart zoeken kan alleen titel jaartal rond elementen atoomnummer najaar dan rivier volgen'.split())
def tip_buiten_vraag(q):
    vraag = _n(q['q'])
    return [w for w in _n(q.get('z') or '').split() if len(w) > 1 and w not in BOEKWOORDEN and w not in TIPWOORDEN and w[:5] not in vraag]

ok = True
for i, A in enumerate(AFL, 1):
    assert len(A['qs']) == 12, (i, len(A['qs']))
    ls = sorted(letter(q) for q in A['qs'])
    if ls != sorted(tiles(A['w'])):
        print('FOUT', i, A['w'], ''.join(ls)); ok = False
    for q in A['qs']:
        q['L'] = letter(q)
    for l in leaks(A):
        print('ANTWOORD IN VRAAG', i, l); ok = False
    for q in A['qs']:
        w = tip_buiten_vraag(q)
        if w: print('ZOEKTIP MET ANDERE WOORDEN', i, q['a'], w); ok = False
    from collections import Counter
    print(i, A['w'], Counter(q['d'] for q in A['qs']), Counter(q['c'] for q in A['qs']))
if not ok: sys.exit(1)
json.dump(AFL, open(__import__('os').path.join(__import__('os').path.dirname(__file__), 'afleveringen.json'), 'w'), ensure_ascii=False)
print('ok')
