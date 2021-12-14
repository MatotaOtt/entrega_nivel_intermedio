from tkinter.messagebox import askokcancel,askquestion

Cuadrodialogo= askquestion(title="Alerta", message="esta seguro que quiere eliminar este evento?")
if Cuadrodialogo=="yes":   
    print("la respuesta es",Cuadrodialogo)
else:
    print("no se sabe")