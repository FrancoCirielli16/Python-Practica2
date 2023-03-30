evaluar = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance 
computing resources provides the promise of capturing unprecedented details 
of large-scale complex systems. However, the specialized knowledge required 
for developing such ABMs creates barriers to wider adoption and utilization. 
Here we present our experiences in developing an initial implementation of 
Repast4Py, a Python-based distributed ABM toolkit. We build on our 
experiences in developing ABM toolkits, including Repast for High 
Performance Computing (Repast HPC), to identify the key elements of a useful 
distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages 
and the Python C-API to create a scalable modeling system that can exploit 
the largest HPC resources and emerging computing architectures.
"""


def titulo_cumple(text):
    titulo = evaluar.split("título: ")[1].split("\n")[0]
    if len(titulo.split()) <= 10:
        print("Título: ok")
    else:
        print("Título: no cumple con la especificación de máximo 10 palabras")

def oraciones(text):
    resumen = evaluar.split("resumen: ")[1]

    oraciones_faciles = 0
    oraciones_aceptables = 0
    oraciones_dificiles = 0
    oraciones_muy_dificiles = 0

    for oracion in resumen.split("."):
        num_palabras = len(oracion.split())
        if num_palabras <= 12:
            oraciones_faciles += 1
        elif num_palabras <= 17:
            oraciones_aceptables += 1
        elif num_palabras <= 25:
            oraciones_dificiles += 1
        else:
            oraciones_muy_dificiles += 1

    print("Cantidad de oraciones fáciles de leer:", oraciones_faciles)
    print("Cantidad de oraciones aceptables para leer:", oraciones_aceptables)
    print("Cantidad de oraciones difíciles de leer:", oraciones_dificiles)
    print("Cantidad de oraciones muy difíciles de leer:", oraciones_muy_dificiles)

titulo_cumple(evaluar)
oraciones(evaluar)
