$f = "C:\Users\playg\BUUM\config\config.local.env"
Write-Host ""
Write-Host "=== PASSWORD DE THEME ACCESS (empieza con shptka_) ===" -ForegroundColor Cyan
while ($true) {
  $tok = (Read-Host "Pega el password y Enter (o escribe salir)").Trim()
  if ($tok -eq "salir") { break }
  if ($tok -match '^shptka_[0-9a-f]{32}$') {
    $lines = Get-Content $f | ForEach-Object {
      if ($_ -match '^SHOPIFY_CLI_THEME_TOKEN=') { "SHOPIFY_CLI_THEME_TOKEN=$tok" } else { $_ }
    }
    [IO.File]::WriteAllLines($f, $lines)
    Write-Host ""
    Write-Host "GUARDADO OK - dile 'guardado' a BUUM." -ForegroundColor Green
    break
  } else {
    Write-Host ("Formato incorrecto (debe ser shptka_ + 32 caracteres). Mide " + $tok.Length + ". Intenta de nuevo.") -ForegroundColor Red
  }
}
Read-Host "Enter para cerrar"
