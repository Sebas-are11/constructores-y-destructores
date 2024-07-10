class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None  # Inicializamos el atributo del archivo
        
        try:
            self.file = open(self.filename, self.mode)
            print(f"Archivo {self.filename} abierto en modo {self.mode}")
        except Exception as e:
            print(f"No se pudo abrir el archivo {self.filename}: {e}")
    
    def write(self, text):
        if self.file:
            self.file.write(text)
        else:
            print("Error: El archivo no está abierto.")
    
    def __del__(self):
        if self.file:
            self.file.close()
            print(f"Archivo {self.filename} cerrado")
        else:
            print("No hay archivo abierto para cerrar.")

# Ejemplo de uso
if __name__ == "__main__":
    # Creamos un objeto FileHandler para escribir en un archivo
    file_handler = FileHandler("ejemplo.txt", "w")
    file_handler.write("¡Hola mundo!\n")
    
    # El archivo se cerrará automáticamente al eliminar el objeto file_handler
    del file_handler
