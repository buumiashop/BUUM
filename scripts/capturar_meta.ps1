$ErrorActionPreference = "Stop"
$f = "C:\Users\playg\BUUM\config\config.local.env"
Write-Host ""
Write-Host "=== CAPTURA SEGURA DE CLAVES META (BUUM) ===" -ForegroundColor Cyan
Write-Host "Los valores NO se muestran al agente ni al chat; van directo al archivo." -ForegroundColor DarkGray
Write-Host ""
$sec = Read-Host "1) CLAVE SECRETA (Enter vacio = conservar la actual)"
$tok = Read-Host "2) TOKEN nuevo del Graph Explorer y Enter"
$sec = $sec.Trim(); $tok = $tok.Trim()
if ($tok.Length -lt 40) {
  Write-Host "EL TOKEN ESTA CORTO ($($tok.Length) chars). Cierra y reintenta." -ForegroundColor Red
} else {
  $lines = Get-Content $f | ForEach-Object {
    if ($_ -match '^META_APP_SECRET=' -and $sec.Length -ge 20) { "META_APP_SECRET=$sec" }
    elseif ($_ -match '^META_USER_TOKEN=') { "META_USER_TOKEN=$tok" }
    else { $_ }
  }
  [IO.File]::WriteAllLines($f, $lines)
  Write-Host ""
  Write-Host "GUARDADO OK - ya puedes cerrar esta ventana y decirle 'guardado' a BUUM." -ForegroundColor Green
}
Read-Host "Enter para cerrar"
