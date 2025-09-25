# Přepnutí do složky s projektem
Set-Location "E:\bot"

# Nastavení proměnných
$repoUrl = "https://github.com/PekelnyScorpion/discord-bot.git"
$commitMsg = "🚀 Přepsání GitHubu verzí z PC"
$branch = "main"

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

# Přepsání GitHubu
git push origin $branch --force
