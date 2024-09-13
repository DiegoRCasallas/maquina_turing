import conjunto_de_estados as sist

N = 1000  # longitud de la cinta, inicializada con un valor grande

class MaquinaDeTuring:
    def __init__(self, algoritmo, entrada, estado=0):
        # inicializar diccionario
        self.transiciones = {}
        # convertir el estado a cadena
        self.estado = str(estado)
        # inicializar la cinta con guiones bajos
        self.cinta = ''.join(['_'] * N)
        # establecer la posición de la cabeza
        self.cabeza = N // 2  # la cabeza está en el medio
        # insertar la entrada en el medio de la cinta
        self.cinta = self.cinta[self.cabeza:] + entrada + self.cinta[:self.cabeza]
        print('\nTabla de estados internos')
        print('-------------------------')
        # asignar valor a la clave
        for linea in algoritmo.splitlines():  # por cada línea en la tabla de estados internos
            # s, s1: estado actual y siguiente estado; d: dirección de desplazamiento;
            s, a, r, d, s1 = linea.split(',')  # a: valor leído; r: valor a escribir
            self.transiciones[s, a] = (r, d, s1)  # estado actual y valor a aceptar
            print(linea)
            print('---------')

    def mover_un_paso(self, i):
        # H significa detenerse
        if self.estado != 'H':
            # obtener el valor leído en la posición actual de la cinta
            valor_leido = self.cinta[self.cabeza]
            # obtener la acción basada en el estado actual y el valor leído
            accion = self.transiciones.get((self.estado, valor_leido))

            if accion:  # si hay una acción (r, d, s1)
                # asignar r = valor a escribir, d = dirección, s1 = siguiente estado
                valor_a_escribir, direccion, siguiente_estado = accion
                # escribir el valor en la cinta
                self.cinta = self.cinta[:self.cabeza] + valor_a_escribir + self.cinta[self.cabeza + 1:]
                # mover la cabeza y cambiar el estado
                if direccion != '*':
                    self.cabeza += 1 if direccion == 'r' else -1
                    self.estado = siguiente_estado
                    print(str(i + 1) + ' ' + self.cinta.replace('_', ''), self.estado)
                    print('---------')

    def ejecutar(self, max_iter=10000):
        print('\ni en   estado')
        print('------------')
        i = 0
        # ejecutar la máquina hasta que se detenga o llegue al máximo de iteraciones
        while self.estado != 'H' and i < max_iter:  # prevenir bucles infinitos
            self.mover_un_paso(i)
            i += 1
        # limpiar la cinta
        resultado = self.cinta.replace('_', '')
        print('\nRESULTADO')
        # salida de los resultados
        #el argumento 2 dentro del metodo int cambia el valor binario a decimal
        print(primer_num_bin + " + " + segundo_num_bin + " = " + resultado + " (binario)")
        print(str(int(primer_num_bin, 2)) + " + " + str(int(segundo_num_bin, 2)) + " = " + str(int(resultado, 2)) + " (decimal)")



if __name__ == '__main__':
    # encabezado
    print("Suma de dos números binarios x + y")
    # recibir entradas
    primer_num_bin = str(input("x = "))
    segundo_num_bin = str(input("y = "))
    entrada = primer_num_bin + '_' + segundo_num_bin
    # leer la tabla de estados internos
    algoritmo = open(sist.suma_dos_binarios).read()
    # ejecutar la máquina de Turing
    turing = MaquinaDeTuring(algoritmo, entrada)
    turing.ejecutar()
