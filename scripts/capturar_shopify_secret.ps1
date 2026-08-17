$f = Join-Path $env:TEMP "buum_shopify_secret.tmp"
Write-Host ""
Write-Host "=== SECRETO de la app BUUM-2026 (Dev Dashboard > Configuracion) ===" -ForegroundColor Cyan
Write-Host "Dale al ojito o al boton de copiar junto a 'Secreto' y pegalo aqui." -ForegroundColor DarkGray
while ($true) {
  $tok = (Read-Host "Pega el secreto y Enter (o escribe salir)").Trim()
  if ($tok -eq "salir") { break }
  if ($tok.Length -ge 20 -and $tok -notmatch '\s') {
    [IO.File]::WriteAllText($f, $tok)
    Write-Host ""
    Write-Host "GUARDADO OK - dile 'guardado' a BUUM." -ForegroundColor Green
    break
  } else {
    Write-Host ("No parece un secreto valido (mide " + $tok.Length + "). Intenta de nuevo.") -ForegroundColor Red
  }
}
Read-Host "Enter para cerrar"
