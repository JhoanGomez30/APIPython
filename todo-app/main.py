from services.Service_Task import Service_Task
# print ("opciones---------")
# print ("1. Crear una tarea")
# print ("2. Buscar una tarea")
# print ("3. Mostrar todas las tareas")
# print ("4. Actualizar una tarea")
# print ("5. Eliminar una tarea")
# print ("6. Salir ")


st = Service_Task()

# # Agregar tareas
# st.add_task("Tarea 1", "Descripcion de la tarea 1")
# st.add_task("Tarea 2", "Descripcion de la tarea 2")
# st.add_task("Tarea 3", "Descripcion de la tarea 3")

# # Borrar todas las tareas
# st.delete_all_tasks()

# # print("Todas las tareas:")
# for task in st.get_all_tasks():
#     print(task)

# #Buscar una tarea
print(st.get_task(13))

##Completar tareas
st.complete_task(13)

# #Buscar una tarea
print(st.get_task(13))