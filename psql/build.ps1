# Usually this is the version (latest, ...)
$tag = "latest"

# Name of the image for GitHub Packages
$name = "ghcr.io/bvlp/monopoly/psql"

# Build as tagged image
(Write-Host "Starting build for $name ..." -ForegroundColor Cyan) `
&& (docker build -t ${name} -t ${name}:${tag} . -o ./build-container `
|| Write-Error 'Build error.') `
&& (Write-Host "Script finished for $name." -ForegroundColor Cyan)
