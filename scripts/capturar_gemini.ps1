$f = "C:\Users\playg\BUUM\config\config.local.env"
Write-Host ""
Write-Host "=== API KEY NUEVA DE GEMINI (empieza con AIza) ===" -ForegroundColor Cyan
while ($true) {
  $tok = (Read-Host "Pega la clave y Enter (o escribe salir)").Trim()
  if ($tok -eq "salir") { break }
  if ($tok -match '^(AIza|AQ\.)[A-Za-z0-9_\.\-]{20,}$') {
    $lines = Get-Content $f | ForEach-Object {
      if ($_ -match '^GEMINI_API_KEY=') { "GEMINI_API_KEY=$tok" } else { $_ }
    }
    [IO.File]::WriteAllLines($f, $lines)
    Write-Host ""
    Write-Host "GUARDADO OK - dile 'guardado' a BUUM." -ForegroundColor Green
    break
  } else {
    Write-Host ("Eso no parece una clave de Gemini (debe empezar con AIza). Mide " + $tok.Length + ". Intenta de nuevo.") -ForegroundColor Red
  }
}
Read-Host "Enter para cerrar"
