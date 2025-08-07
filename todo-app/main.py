# from services.Service_Task import Service_Task
# print ("opciones---------")
# print ("1. Crear una tarea")
# print ("2. Buscar una tarea")
# print ("3. Mostrar todas las tareas")
# print ("4. Actualizar una tarea")
# print ("5. Eliminar una tarea")
# print ("6. Salir ")


# st = Service_Task()

# # # # Agregar tareas
# st.add_task("Tarea 1", "Descripcion de la tarea 1")
# st.add_task("Tarea 2", "Descripcion de la tarea 2")
# st.add_task("Tarea 4", "Descripcion de la tarea 4")

# # #Buscar una tarea
# print("Buscar una tarea")
# print(st.get_task(69))

# print("Todas las tareas:")
# for task in st.get_all_tasks():
#     print(task)

# ##actualizar una tarea
# st.update_task(2, Task("Tarea 1.1", "Barrer la casa", completed=True, id= 69))

# ##Eliminar una unica tarea
# # st.delete_task(1)

# print("Todas las tareas:")
# for task in st.get_all_tasks():
#     print(task)

# # ##Completar tareas
# # print("tarea completada")
# # st.complete_task(3)
# print(st.get_task(69))

# Borrar todas las tareas
# st.delete_all_tasks()

from flask import Flask
from controllers.Controller_Task import task_bp

app = Flask(__name__)
app.register_blueprint(task_bp)

if __name__ == "__main__":
    app.run(debug=True)