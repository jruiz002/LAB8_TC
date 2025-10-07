"""
Módulo de Menú Principal
Sistema interactivo para análisis de complejidad de algoritmos.
"""

from analyzer import PerformanceAnalyzer
from algorithms import Algorithms

class MenuSystem:
    """Sistema de menú para análisis de algoritmos"""
    
    def __init__(self):
        """Inicializa el sistema de menú"""
        self.analyzer = PerformanceAnalyzer()
        self.available_problems = [1, 2, 3]
    
    def display_main_menu(self):
        """Muestra el menú principal"""
        print("\n" + "=" * 60)
        print("    ANALIZADOR DE COMPLEJIDAD DE ALGORITMOS")
        print("=" * 60)
        print("Seleccione una opción:")
        print()
        
        # Mostrar problemas disponibles
        for problem_num in self.available_problems:
            problem_info = Algorithms.get_problem_info(problem_num)
            if problem_info:
                print(f"{problem_num}. Problema {problem_num}: {problem_info['name']}")
                print(f"   Complejidad: {problem_info['complexity']}")
                print(f"   Descripción: {problem_info['description']}")
                print()
        
        print("4. Comparar todos los problemas")
        print("5. Configurar valores de n personalizados")
        print("0. Salir")
        print("=" * 60)
    
    def get_user_choice(self):
        """
        Obtiene la elección del usuario
        
        Returns:
            int: Opción seleccionada por el usuario
        """
        try:
            choice = int(input("Ingrese su opción: "))
            return choice
        except ValueError:
            print("Por favor, ingrese un número válido.")
            return -1
    
    def get_custom_n_values(self):
        """
        Permite al usuario configurar valores de n personalizados
        
        Returns:
            list: Lista de valores de n personalizados
        """
        print("\nConfiguración de valores de n personalizados")
        print("Ingrese los valores de n separados por comas (ej: 1,10,100,1000)")
        print("O presione Enter para usar valores por defecto")
        
        user_input = input("Valores de n: ").strip()
        
        if not user_input:
            return None  # Usar valores por defecto
        
        try:
            n_values = [int(x.strip()) for x in user_input.split(',')]
            n_values = sorted(set(n_values))  # Eliminar duplicados y ordenar
            
            if not n_values:
                print("No se ingresaron valores válidos. Usando valores por defecto.")
                return None
            
            print(f"Valores de n configurados: {n_values}")
            return n_values
            
        except ValueError:
            print("Error en el formato. Usando valores por defecto.")
            return None
    
    def analyze_single_problem(self, problem_num, n_values=None):
        """
        Analiza un problema específico
        
        Args:
            problem_num (int): Número del problema
            n_values (list): Valores de n a analizar
        """
        problem_info = Algorithms.get_problem_info(problem_num)
        if not problem_info:
            print(f"Problema {problem_num} no encontrado.")
            return
        
        print(f"\nIniciando análisis del Problema {problem_num}...")
        
        # Ejecutar análisis
        results = self.analyzer.run_analysis(problem_num, n_values)
        
        if not results:
            print("No se pudieron obtener resultados.")
            return
        
        # Generar tabla
        self.analyzer.create_results_table(results, problem_num)
        
        # Generar gráfica
        self.analyzer.create_visualization(results, problem_num)
        
        # Guardar en CSV
        self.analyzer.save_results_to_csv(results, problem_num)
        
        # Mostrar resumen
        self.analyzer.display_summary(results, problem_num)
        
        print(f"\nAnálisis del Problema {problem_num} completado.")
        input("Presione Enter para continuar...")
    
    def compare_all_problems(self, n_values=None):
        """
        Compara todos los problemas disponibles
        
        Args:
            n_values (list): Valores de n a analizar
        """
        print("\nIniciando comparación de todos los problemas...")
        
        # Usar valores optimizados para comparación si no se especifican
        if n_values is None:
            n_values = [1, 10, 100, 1000, 10000, 100000]  # Sin 1M para evitar tiempos excesivos
        
        results = self.analyzer.compare_problems(self.available_problems, n_values)
        
        print("\nComparación completada.")
        input("Presione Enter para continuar...")
    
    def run(self):
        """Ejecuta el sistema de menú principal"""
        custom_n_values = None
        
        while True:
            self.display_main_menu()
            choice = self.get_user_choice()
            
            if choice == 0:
                print("\n¡Gracias por usar el Analizador de Complejidad!")
                print("Resultados guardados en la carpeta 'results'")
                break
            
            elif choice in self.available_problems:
                self.analyze_single_problem(choice, custom_n_values)
            
            elif choice == 4:
                self.compare_all_problems(custom_n_values)
            
            elif choice == 5:
                custom_n_values = self.get_custom_n_values()
                if custom_n_values:
                    print(f"Valores personalizados configurados: {custom_n_values}")
                else:
                    print("Se usarán los valores por defecto.")
                input("Presione Enter para continuar...")
            
            else:
                print("Opción no válida. Por favor, seleccione una opción del menú.")
                input("Presione Enter para continuar...")

def main():
    """Función principal del programa"""
    try:
        menu = MenuSystem()
        menu.run()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")
        print("¡Hasta luego!")
    except Exception as e:
        print(f"\nError inesperado: {e}")
        print("Por favor, reporte este error.")

if __name__ == "__main__":
    main()