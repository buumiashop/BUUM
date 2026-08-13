$f = "C:\Users\playg\BUUM\config\config.local.env"
Write-Host ""
Write-Host "=== API KEY NUEVA DE OPENAI (empieza con sk-) ===" -ForegroundColor Cyan
while ($true) {
  $tok = (Read-Host "Pega la clave y Enter (o escribe salir)").Trim()
  if ($tok -eq "salir") { break }
  if ($tok -match '^sk-[A-Za-z0-9_\-]{20,}$') {
    $lines = Get-Content $f | ForEach-Object {
      if ($_ -match '^OPENAI_API_KEY=') { "OPENAI_API_KEY=$tok" } else { $_ }
    }
    [IO.File]::WriteAllLines($f, $lines)
    Write-Host ""
    Write-Host "GUARDADO OK - dile 'guardado' a BUUM." -ForegroundColor Green
    break
  } else {
    Write-Host ("Eso no parece una clave de OpenAI (debe empezar con sk-). Mide " + $tok.Length + ". Intenta de nuevo.") -ForegroundColor Red
  }
}
Read-Host "Enter para cerrar"
