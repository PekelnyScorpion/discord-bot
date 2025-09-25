# Nastavení proměnných
$repoUrl = "https://github.com/TVOJE_UZIVATELSKE_JMENO/discord-bot.git"
$commitMsg = "🚀 Nahrání Discord bota"
$branch = "main"

# Přejdi do složky s projektem
Set-Location "E:\bot"

# Inicializace Git (pokud není)
if (-not (Test-Path ".git")) {
    git init
}

# Přidání vzdáleného repozitáře
git remote remove origin 2>$null
git remote add origin $repoUrl

# Přidání všech souborů
git add .

# Commit
git commit -m $commitMsg

# Push na GitHub
git push -u origin $branch
