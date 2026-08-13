$f = "C:\Users\playg\BUUM\config\config.local.env"
Write-Host ""
Write-Host "=== SOLO LA CLAVE SECRETA DE LA APP (32 caracteres) ===" -ForegroundColor Cyan
Write-Host "Pagina: Configuracion de la app > Basica > 'Clave secreta de la app' > Mostrar" -ForegroundColor DarkGray
Write-Host ""
while ($true) {
  $sec = (Read-Host "Pega la clave y Enter (o escribe salir)").Trim()
  if ($sec -eq "salir") { break }
  if ($sec -match '^[0-9a-f]{32}$') {
    $lines = Get-Content $f | ForEach-Object {
      if ($_ -match '^META_APP_SECRET=') { "META_APP_SECRET=$sec" } else { $_ }
    }
    [IO.File]::WriteAllLines($f, $lines)
    Write-Host ""
    Write-Host "PERFECTA - GUARDADA. Cierra esta ventana y dile 'guardado' a BUUM." -ForegroundColor Green
    break
  } else {
    Write-Host ("ESO NO ES LA CLAVE (mide " + $sec.Length + ", debe medir 32, solo numeros y letras a-f minusculas). Intenta de nuevo.") -ForegroundColor Red
  }
}
Read-Host "Enter para cerrar"
