' Servidor local del Centro de Mando BUUM (puerto 8130, oculto)
' La raiz se calcula desde la ubicacion de este script (os\..) — sin rutas a carpetas viejas.
Set sh = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
raiz = fso.GetParentFolderName(fso.GetParentFolderName(WScript.ScriptFullName))
sh.Run """C:\Users\playg\Tools\Miniconda\python.exe"" -m http.server 8130 --bind 127.0.0.1 --directory """ & raiz & """", 0, False
