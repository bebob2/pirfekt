# πrfekt! von Fionn und Benjamin

**πrfekt!** ist ein Spiel, indem man versuchen muss, einen möglichst
perfekten Kreis zu zeichnen.

Der gezeichnete Kreis wird von unserer Software registriert,
ausgewertet und mit einer Punktzahl versehrt: Ein
perfekter Kreis bringt eine Punktzahl von **_100_**.
Die Software ermittelt Automatisch den Mittelpunkt und den Radius
des gezeichneten Kreises, von dem aus die
Software die Abweichung von einem _idealen Kreis_
ermittelt.
Die Position des Mittelpunktes, sowie der Radius des gezeichneten Kreises
sind für den Nutzer frei wählbar.

## 💻🛠️ Was brauche ich um **πrfekt!** zu spielen?

**Entweder:**
Ein Betriebssystem mit Python (am besten Version 13.3 oder höher) und Pygame.

Pygame installieren:

```sh
pip install pygame
```

**Oder:**
Windows 10+ um die `exe` Datei auszuführen.

**Und:** **Bildschirm** (mindestens 1280x720) + **Maus** + (Tastatur)

## 🎮 Wie Verwende/Starte ich πrfekt!?

### 0. Spiel starten

- Option 1: im Python-Projektordner die Python Datei `main.py` ausführen
  mit:
  ```sh
  python main.py
  ```
  bzw.
  ```sh
  python3 main.py
  ```
- Option 2: Unter Windows, die `main.exe` aus der extrahierten `.zip` Datei starten.
  Die Datei sollte folgenden Namen haben: `Pirfekt.v3.14159_Win_x64.zip`.
  Diese Datei sollte in den GitHub Releases zu sehen sein, also unter
  <a>https://github.com/bebob2/pirfekt/releases/</a>
  . Nicht vergessen die `.zip` Datei zu extrahieren!

### 1. 🖊️Auf der Benutzeroberfläche Zeichnen / Das Spiel spielen

- Maustaste drücken & gedrückt lassen und die Maus bewegen zum zeichnen
- Sobald die Maustaste losgelassen wird, wird die Zeichnung beendet
- (Es können alle 5 Maustasten zum Zeichnen verwendet werden)
- Nach dem die Zeichnung vorbei ist d.h. die Maustaste losgelassen wird,
  kann in dem Spiel nicht mehr gezeichnet werden
- Wenn die Zeichnung Beendet ist und man eine Mindestlänge der Zeichnung erfüllt
  hat, beginnt die Auswertung: Mittelpunkt und Radius werden automatisch ermittelt und ein _ideal Kreis_ in Rot angezeigt, so wie der Mittelpunkt mit einem 'X' Markiert. Der Score (die Punktzahl) wird angezeigt und evtl. ein _highscore_ gespeichert (aber noch nicht Angezeigt)
- Um ein neues Spiel zu starten d.h. einen neuen Kreis zu zeichnen, gibt es zwei
  Wege:
  1. Den `Neustart` Knopf, oben rechts mit dem `⟳` Symbol, drücken
  2. Auf der Tastatur die Taste `c` drücken
- Nach einem _Neustart_ ist alles so wie am Anfang, nur dass man jetzt evtl.
  einen anderen Highscore hat
- Man kann ein Bild (bzw. einen Screenshot) von seinem Kreis speichern,
  zusammen mit dem (high)score (Informationen zum Speicherort weiter unten) indem man:
  1. den `Download/Speichern` Knopf, oben rechts mit dem `⤓` Symbol, drückt.
  2. die Tastenkombination `Strg`+`S` drückt.
- Spiel beenden: Fenster schließen oder (unter Windows) `alt`+`F4` drücken (genauso wie bei anderen Programmen)

---

### (OPTIONAL:🧑‍💻 Unter Windows eine `.exe` Datei kompilieren)

Das geht mit `pyinstaller`. Dafür muss pyinstaller installiert sein, das geht mit:

```sh
pip install pyinstaller
```

um die `exe` zu kompilieren muss folgendes eingegeben werden:

```sh
pyinstaller  main.py --icon=./logos/pirfekt1.ico
```

**Danach** muss noch der der Ordner `./logos` in den entstehenden Ordner `./dist/main` kopiert werden.

Unter `./dist/main` findet man auch die `main.exe` Datei, also unter `./dist/main/main.exe`

Die `.exe` Datei und alle benötigten Dateien sind auch als `.zip` zur Verfügung gestellt als _Release_ (Mehr dazu Oben unter: "🎮 Wie Verwende/Starte ich πrfekt!?" )

### 💡Wie wird die Punktzahl vergeben?

Zuerst werden Mittelpunkt und Radius vom Kreis ermittelt. Danach wird die durchschnittliche Abweichung vom ermittelten Radius zu jedem einzelnen Punkt des Kreises ausgerechnet. Diese Abweichung wird in Prozent berechnet und von hundert Prozent abgezogen. Ein _perfekter_ Kreis, mit gleichbleibendem Radius, entspricht der Punktzahl 100.

### 📷 Wo werden die Screenshots gespeichert?

Die Screenshots/Bilder werden in dem Projektordner unter `./screenshots` gespeichert (im `.png` Format).

## 📄Unterlagen (Beschreibung, UML, ...)

Die zusätzlichen Unterlagen sind unter `./Unterlagen` zu finden:

- Die Produktbeschreibung: `./Beschreibung.pdf`
- Das Lastenheft: `./Lastenheft.pdf`
- Substantiv-Verb-Methode: `./Substaniv-verb.pdf`
- UML:
  - `./UML/UML_Pifekt.png`<--- Eigentliche UML
  - `./UML/Dateien_Pifekt.png`
