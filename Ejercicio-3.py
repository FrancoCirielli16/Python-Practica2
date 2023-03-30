
import string


jupyter_info = """ JupyterLab is a web-based interactive development 
environment for Jupyter notebooks, 
code, and data. JupyterLab is flexible: configure and arrange the user 
interface to support a wide range 
of workflows in data science, scientific computing, and machine learning. 
JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing 
ones.
"""

letra = input("ingrese una letra: ")
if not(letra in string.ascii_letters):
    print("No se ingreso una letra")

for palabra in jupyter_info.split():
    if(palabra.lower()[0].startswith(letra.lower())):
        print(palabra)
 