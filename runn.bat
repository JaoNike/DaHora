@echo off
:: Crie um script de execução do Python como administrador
set "script_path=C:\Users\20232IN023\Downloads\Dahora-20240603T214626Z-001\Dahora\test.py"

:: Verifique se o script está sendo executado como administrador
:: Se não estiver, eleva os privilégios
:: Utilize o "runas" para abrir uma nova janela de prompt de comando como administrador
whoami /groups | find "S-1-5-32-544" >nul || (
    echo Batch...
    powershell -Command "Start-Process cmd -ArgumentList '/c %0 %*' -Verb RunAs"
    exit /b
)

:: Executa o script Python
python "%script_path%"
