# Hollymovies

Online filmová databáze.

Funkcionalita:
- zobrazovat informace o filmu
  -[x] zobrazit název filmu
  -[x] jména herců
  -[x] jméno režiséra
  -[x] rok natočení
  - dostupnost (streamovací platformy)
  -[x] popis
  -[x] hodnocení
  -[x] státy
  -[x] jazyk
  - film/seriál
  -[x] žánry
  - počet dílů/pokračování
  -[x] PG - přístupnost (od jakého věku je dostupný)
  -[x] délka filmu
  -[x] čas děje - odkaz na přechozí/následující díl
  - ocenění
-[x] filtrovat filmy podle žánru
- filtrovat filmy pro dospělé a pro děti
- seznam filmů dle:
  -[x] abecedy
  - hodnocení
  -[x] délka
  -[x] dle herce
  -[x] dle režiséra
  - dle ocenění
- u série zobrazit dle chronologie děje
- doporučení podobných filmů
-[x] uživatelské skupiny:
  -[x] přidávání nové země
  -[x] přidávání nového žánru
  -[x] přidávání nového filmu
  -[x] přidávání nového herce
  -[x] přidávání nového režiséra
-[x] přihlášený uživatel:
  -[x] hodnotit (pouze jednou)
  -[x] komentovat (pouze jednou)
- notifikace (pro nově přidaný film)
-[x] vyhledávání
  -[x] dle originálního názvu filmu
  -[x] dle českého názvu filmu
  -[x] dle jména a příjmení herce/režiséra
  -[x] dle textu v popisu

## Úkoly
- vyřešit pohlaví u Person (Male/Female/Unknown/Non-binary)
- Add permissions (viz TODO)
- Změnit vzhled (css)
- Notifikace (nově přidaný film) (AJAX)
- uspořádat seznam filmů podle hodnocení
- upravit Profile (accounts/models.py)
  -[x] zobrazit podrobnosti uživatele
  - můžete něco i přidat do modelu
    - např. public - jestli je profil veřejný
  - seznam všech uživatelů (zobrazí se pouze pro Staff)
  - seznam veřejných profilů (zobrazí se všem přihlášeným uživatelům)
- cokoliv vás napadne 

## Dále probrat
-[x] REST API
-[x] Testování