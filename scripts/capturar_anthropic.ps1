$f = Join-Path $env:TEMP "buum_anthropic.tmp"
Write-Host ""
Write-Host "=== TOKEN DE SUSCRIPCION CLAUDE (empieza con sk-ant-oat) ===" -ForegroundColor Cyan
Write-Host "Va directo al servidor; no se guarda en esta compu." -ForegroundColor DarkGray
while ($true) {
  $tok = (Read-Host "Pega el token y Enter (o escribe salir)").Trim()
  if ($tok -eq "salir") { break }
  if ($tok -match '^sk-ant-oat[A-Za-z0-9_\-]{20,}$') {
    [IO.File]::WriteAllText($f, $tok)
    Write-Host ""
    Write-Host "GUARDADO OK - dile 'guardado' a BUUM." -ForegroundColor Green
    break
  } else {
    Write-Host ("Eso no parece el token (debe empezar con sk-ant-oat). Mide " + $tok.Length + ". Intenta de nuevo.") -ForegroundColor Red
  }
}
Read-Host "Enter para cerrar"
