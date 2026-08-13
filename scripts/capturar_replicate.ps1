$f = "C:\Users\playg\BUUM\config\config.local.env"
Write-Host ""
Write-Host "=== TOKEN NUEVO DE REPLICATE (empieza con r8_) ===" -ForegroundColor Cyan
while ($true) {
  $tok = (Read-Host "Pega el token y Enter (o escribe salir)").Trim()
  if ($tok -eq "salir") { break }
  if ($tok -match '^r8_[A-Za-z0-9]{20,}$') {
    $lines = Get-Content $f | ForEach-Object {
      if ($_ -match '^REPLICATE_API_TOKEN=') { "REPLICATE_API_TOKEN=$tok" } else { $_ }
    }
    [IO.File]::WriteAllLines($f, $lines)
    Write-Host ""
    Write-Host "GUARDADO OK - dile 'guardado' a BUUM." -ForegroundColor Green
    break
  } else {
    Write-Host ("Eso no parece un token de Replicate (debe empezar con r8_). Mide " + $tok.Length + ". Intenta de nuevo.") -ForegroundColor Red
  }
}
Read-Host "Enter para cerrar"
