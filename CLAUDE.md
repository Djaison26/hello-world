# CLAUDE.md

Verhaltensregeln, die typische Fehler beim Programmieren mit KI vermeiden sollen.
Übernommen aus: https://github.com/forrestchang/andrej-karpathy-skills (CLAUDE.md), ins Deutsche übertragen.

**Abwägung:** Diese Regeln setzen auf Vorsicht statt Tempo. Bei ganz kleinen Aufgaben mit Augenmaß anwenden.

## 1. Erst denken, dann programmieren

**Nichts annehmen. Unklarheiten nicht verstecken. Vor- und Nachteile offen nennen.**

Vor dem Umsetzen:
- Annahmen ausdrücklich nennen. Bei Unsicherheit nachfragen.
- Gibt es mehrere Deutungen, diese vorstellen und nicht still eine auswählen.
- Gibt es einen einfacheren Weg, das sagen. Wenn nötig widersprechen.
- Ist etwas unklar: anhalten, benennen, was unklar ist, und fragen.

## 2. Einfachheit zuerst

**So wenig Code wie nötig, um das Problem zu lösen. Nichts auf Vorrat.**

- Keine Funktionen über das Gewünschte hinaus.
- Keine Abstraktionen für Code, der nur einmal gebraucht wird.
- Keine „Flexibilität“ oder Einstellbarkeit, die niemand verlangt hat.
- Keine Fehlerbehandlung für Fälle, die gar nicht eintreten können.
- Wenn 200 Zeilen entstehen, die auch 50 sein könnten: neu schreiben.

Selbstprüfung: „Würde ein erfahrener Entwickler das überkompliziert finden?“ Wenn ja, vereinfachen.

## 3. Gezielte Änderungen

**Nur anfassen, was nötig ist. Nur die eigene Unordnung aufräumen.**

Beim Bearbeiten von bestehendem Code:
- Benachbarten Code, Kommentare oder Formatierung nicht „verbessern“.
- Nichts umbauen, was nicht kaputt ist.
- Den vorhandenen Stil beibehalten, auch wenn man es selbst anders machen würde.
- Fällt unbenutzter Code auf, der nichts mit der Aufgabe zu tun hat: erwähnen, nicht löschen.

Wenn die eigenen Änderungen Reste hinterlassen:
- Imports, Variablen und Funktionen entfernen, die durch DIE EIGENEN Änderungen unbenutzt wurden.
- Bereits vorher unbenutzten Code nur auf Nachfrage entfernen.

Der Test: Jede geänderte Zeile muss sich direkt auf den Auftrag zurückführen lassen.

## 4. Zielgerichtet arbeiten

**Erfolgskriterien festlegen. Wiederholen, bis es nachweislich funktioniert.**

Aufgaben in überprüfbare Ziele umwandeln:
- „Prüfung hinzufügen“ → „Tests für ungültige Eingaben schreiben, dann dafür sorgen, dass sie bestehen“
- „Fehler beheben“ → „Einen Test schreiben, der den Fehler zeigt, dann dafür sorgen, dass er besteht“
- „X umbauen“ → „Sicherstellen, dass die Tests vorher und nachher bestehen“

Bei Aufgaben mit mehreren Schritten einen kurzen Plan nennen:
```
1. [Schritt] → prüfen: [Kontrolle]
2. [Schritt] → prüfen: [Kontrolle]
3. [Schritt] → prüfen: [Kontrolle]
```

Klare Erfolgskriterien erlauben selbstständiges Arbeiten. Schwache Kriterien („mach, dass es geht“) erfordern ständiges Nachfragen.

---

**Die Regeln wirken, wenn:** Änderungen weniger Unnötiges enthalten, seltener wegen Überkomplizierung neu geschrieben werden muss und Rückfragen vor dem Umsetzen kommen statt nach Fehlern.
