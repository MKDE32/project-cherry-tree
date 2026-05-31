## Repo holen / initial
```
git clone <url>
git clone -b <branch> <url>
git init
```
## Überblick (sehr wichtig)
```
git status
git log --oneline --graph --all
git show <commit>
git diff
git diff --staged
```

## Dateien & Änderungen
```
git add -A
git commit -m "notes / changes"
```

## Branches (minimal nötig)
```
git branch
git checkout <branch>
git checkout -b <branch>
```

## Remote
```
git pull
git fetch
```

## 🔍 Analyse / Forensik (KERN für Pentester)

# wer hat was geändert
```
git blame <file>
```

# gesamte Historie einer Datei (auch gelöscht)
```
git log --all --full-history -- <file>
```

# alle Änderungen inkl. Inhalt
```
git log -p
```

# nach Secrets suchen
```
git log -p | grep -i "password"
git log -p | grep -i "api_key"
git log -p | grep -i "token"
```

# bestimmte Datei in alter Version anzeigen
```
git show <commit>:<file>
```

# gelöschte Dateien finden
```
git log --diff-filter=D --summary
```

## 🕵️ Repo durchsuchen
```
grep -r "password" .
grep -r "secret" .
grep -r "key" .
```

## 🔄 Schnelles Wechseln (sehr praktisch)
```
git stash
git stash pop
```

## 🚨 Undo (vorsichtig!)
```
git reset --soft HEAD~1
git checkout -- <file>
```

## 🧹 Cleanup
```
git clean -fd
```

## ⚡ Typischer Pentest-Workflow
```
git clone <target-repo>
cd <repo>
git log -p | grep -i password
grep -r "secret" .
git log --all --full-history -- <file>
```

## ⚠️ Wichtige Hinweise

# niemals blind vertrauen → alte commits enthalten oft secrets

# gelöschte daten sind oft noch in git history

# .git ordner kann sensitive infos enthalten

# immer auch branches + tags prüfen
