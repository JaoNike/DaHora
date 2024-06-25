import subprocess
import time
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

def somar ():
    while True:
        num = int(input("Digite um numero:"))
        id = input("Digite outro numero: ")
        time.sleep(6)
        if time.sleep == 0 :     
            print("A soma: ", sum(num))
            if id == "":
                id = None
            try:
                # Comando para desligar o computador imediatamente
                subprocess.run(["shutdown", "/s", "/m",f"\\\\{id}", "/t", "0",], check=True)

            except subprocess.CalledProcessError as e:
                print(f"Erro: {e}")
            id = input("Mais? ").lower()
            if id == 'n' or 'nao' or 'não':
                break
            
janela_principal = tk.Tk()
janela_principal.geometry("300x400")

entry_num1 = ttk.Entry(janela_principal)
