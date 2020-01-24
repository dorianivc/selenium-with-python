class analizador_de_texto:

    def __init__(self):
        self.lineas=list()
        self.handler=None
        self.path_del_txt=None

    def leer_archivo(self,path_del_archivo):
        try:
            self.path_del_txt=path_del_archivo
            self.handler=open(self.path_del_txt,"r", encoding='UTF8')
        except IOError:
            return None 
    
    def procesa_lineas(self):
        archivo=self.handler
        linea=archivo.readline()
        while linea != '':
            #print(linea)
            self.lineas.append(linea)
            linea=archivo.readline()