$f = Join-Path $env:TEMP "buum_anthropic.tmp"
Write-Host ""
Write-Host "=== TOKEN BUUM: TODO EN UNO ===" -ForegroundColor Cyan
Write-Host "1) Se abrira el navegador -> AUTORIZA"
Write-Host "2) Vuelve aqui y espera: esta ventana guarda el token sola."
Write-Host ""
$salida = claude setup-token 2>&1 | Out-String
$m = [regex]::Match($salida, 'sk-ant-oat[A-Za-z0-9_\-]{20,}')
if ($m.Success) {
  [IO.File]::WriteAllText($f, $m.Value)
  Write-Host ""
  Write-Host "GUARDADO OK - dile 'guardado' a BUUM. Ya puedes cerrar esta ventana." -ForegroundColor Green
} else {
  Write-Host ""
  Write-Host "NO ENCONTRE EL TOKEN. Dile a BUUM: 'no salio'." -ForegroundColor Red
}
Read-Host "Enter para cerrar"
