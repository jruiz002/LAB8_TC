"""
Módulo Analizador para Medición de Rendimiento y Visualización
Contiene las funciones para profiling, generación de tablas y gráficas.
"""

import time
import os
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from algorithms import Algorithms

class PerformanceAnalyzer:
    """Clase para análisis de rendimiento de algoritmos"""
    
    def __init__(self, results_dir="results"):
        """
        Inicializa el analizador
        
        Args:
            results_dir (str): Directorio donde guardar los resultados
        """
        self.results_dir = results_dir
        self.results = []
        self.current_problem = None
        
        # Crear directorio de resultados si no existe
        os.makedirs(self.results_dir, exist_ok=True)
    
    def profile_algorithm(self, algorithm_func, n, num_runs=3):
        """
        Perfila un algoritmo midiendo su tiempo de ejecución
        
        Args:
            algorithm_func: Función del algoritmo a perfilar
            n (int): Tamaño de entrada
            num_runs (int): Número de ejecuciones para promediar
            
        Returns:
            tuple: (tiempo_promedio, desviación_estándar, resultado)
        """
        times = []
        result = None
        
        for _ in range(num_runs):
            start_time = time.perf_counter()
            result = algorithm_func(n)
            end_time = time.perf_counter()
            times.append(end_time - start_time)
        
        avg_time = np.mean(times)
        std_time = np.std(times)
        
        return avg_time, std_time, result
    
    def run_analysis(self, problem_num, n_values=None):
        """
        Ejecuta el análisis completo para un problema específico
        
        Args:
            problem_num (int): Número del problema (1, 2, o 3)
            n_values (list): Lista de valores de n a analizar
            
        Returns:
            list: Lista de resultados del análisis
        """
        if n_values is None:
            # Valores por defecto según el problema
            if problem_num == 1:  # O(n² log n) - más lento
                n_values = [1, 10, 100, 1000, 10000, 100000]
            elif problem_num == 2:  # O(n) - rápido
                n_values = [1, 10, 100, 1000, 10000, 100000, 1000000]
            elif problem_num == 3:  # O(n²) - moderadamente lento
                n_values = [1, 10, 100, 1000, 10000, 100000]
            else:
                n_values = [1, 10, 100, 1000, 10000, 100000, 1000000]
        
        problem_info = Algorithms.get_problem_info(problem_num)
        if not problem_info:
            print(f"Problema {problem_num} no encontrado")
            return []
        
        algorithm_func = problem_info['algorithm_func']
        problem_name = f"Problema {problem_num}: {problem_info['name']} ({problem_info['complexity']})"
        
        print(f"Ejecutando análisis de rendimiento para {problem_name}")
        print("=" * 70)
        
        results = []
        
        for n in n_values:
            print(f"Procesando n = {n:,}...")
            
            # Ajustar número de ejecuciones según el tamaño
            if n <= 1000:
                num_runs = 5
            elif n <= 100000:
                num_runs = 3
            else:
                num_runs = 1
            
            try:
                avg_time, std_time, operations = self.profile_algorithm(
                    algorithm_func, n, num_runs
                )
                
                theoretical = Algorithms.get_theoretical_complexity(problem_num, n)
                
                result_data = {
                    'n': n,
                    'time_seconds': avg_time,
                    'time_ms': avg_time * 1000,
                    'std_dev': std_time,
                    'operations': operations,
                    'theoretical_complexity': theoretical
                }
                
                results.append(result_data)
                
                print(f"  Tiempo promedio: {avg_time:.6f} segundos ({avg_time * 1000:.3f} ms)")
                print(f"  Operaciones: {operations:,}")
                
            except KeyboardInterrupt:
                print(f"\nAnálisis interrumpido en n = {n}")
                break
            except Exception as e:
                print(f"  Error en n = {n}: {e}")
                continue
        
        self.results = results
        self.current_problem = problem_num
        return results
    
    def create_results_table(self, results, problem_num):
        """
        Crea y muestra la tabla de resultados
        
        Args:
            results (list): Lista de resultados
            problem_num (int): Número del problema
            
        Returns:
            tuple: (datos_tabla, encabezados)
        """
        if not results:
            print("No hay resultados para mostrar")
            return [], []
        
        table_data = []
        for result in results:
            table_data.append([
                f"{result['n']:,}",
                f"{result['time_seconds']:.6f}",
                f"{result['time_ms']:.3f}",
                f"{result['operations']:,}",
                f"{result['theoretical_complexity']:.0f}"
            ])
        
        headers = [
            "Tamaño de Input (n)", 
            "Tiempo (segundos)", 
            "Tiempo (ms)", 
            "Operaciones", 
            "Complejidad Teórica"
        ]
        
        problem_info = Algorithms.get_problem_info(problem_num)
        
        print("\n" + "=" * 80)
        print(f"TABLA DE RESULTADOS - PROBLEMA {problem_num}")
        print(f"{problem_info['name']} - {problem_info['complexity']}")
        print("=" * 80)
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        
        return table_data, headers
    
    def create_visualization(self, results, problem_num):
        """
        Crea la visualización gráfica de los resultados
        
        Args:
            results (list): Lista de resultados
            problem_num (int): Número del problema
        """
        if not results:
            print("No hay resultados para graficar")
            return
        
        n_values = [r['n'] for r in results]
        times_ms = [r['time_ms'] for r in results]
        
        problem_info = Algorithms.get_problem_info(problem_num)
        
        # Crear la gráfica
        plt.figure(figsize=(12, 7))
        
        plt.plot(n_values, times_ms, 'bo-', linewidth=2, markersize=8, 
                label=f'Tiempo medido - {problem_info["complexity"]}')
        plt.xlabel('Tamaño de Input (n)', fontsize=12)
        plt.ylabel('Tiempo de Ejecución (ms)', fontsize=12)
        plt.title(f'Problema {problem_num}: {problem_info["name"]}\n'
                 f'Tiempo de Ejecución vs Tamaño de Input', 
                 fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.legend(fontsize=11)
        
        # Formatear para mejor apariencia
        plt.tight_layout()
        
        # Guardar la gráfica
        filename = f'performance_analysis_problem_{problem_num}.png'
        filepath = os.path.join(self.results_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"Gráfica guardada en: {filepath}")
    
    def save_results_to_csv(self, results, problem_num):
        """
        Guarda los resultados en un archivo CSV
        
        Args:
            results (list): Lista de resultados
            problem_num (int): Número del problema
        """
        if not results:
            print("No hay resultados para guardar")
            return
        
        df = pd.DataFrame(results)
        filename = f'performance_results_problem_{problem_num}.csv'
        filepath = os.path.join(self.results_dir, filename)
        df.to_csv(filepath, index=False)
        
        print(f"Resultados guardados en: {filepath}")
    
    def display_summary(self, results, problem_num):
        """
        Muestra un resumen del análisis
        
        Args:
            results (list): Lista de resultados
            problem_num (int): Número del problema
        """
        if not results:
            print("No hay resultados para resumir")
            return
        
        problem_info = Algorithms.get_problem_info(problem_num)
        
        print("\n" + "=" * 80)
        print(f"RESUMEN DEL ANÁLISIS - PROBLEMA {problem_num}")
        print(f"{problem_info['name']}")
        print("=" * 80)
        print(f"• Complejidad teórica: {problem_info['complexity']}")
        print(f"• Descripción: {problem_info['description']}")
        print(f"• Valores de n analizados: {len(results)}")
        print(f"• Tiempo mínimo: {min(r['time_ms'] for r in results):.3f} ms")
        print(f"• Tiempo máximo: {max(r['time_ms'] for r in results):.3f} ms")
        
        # Calcular factor de crecimiento
        if len(results) > 1:
            first_time = results[0]['time_ms']
            last_time = results[-1]['time_ms']
            if first_time > 0:
                growth_factor = last_time / first_time
                print(f"• Factor de crecimiento total: {growth_factor:.2f}x")
        
        print("=" * 80)
    
    def compare_problems(self, problem_numbers, n_values=None):
        """
        Compara múltiples problemas en una sola gráfica
        
        Args:
            problem_numbers (list): Lista de números de problemas a comparar
            n_values (list): Lista de valores de n a analizar
        """
        if n_values is None:
            n_values = [1, 10, 100, 1000, 10000, 100000, 1000000]  # Valores completos para comparación
        
        plt.figure(figsize=(12, 8))
        colors = ['blue', 'red', 'green', 'orange', 'purple']
        
        all_results = {}
        
        for i, problem_num in enumerate(problem_numbers):
            print(f"\nAnalizando Problema {problem_num} para comparación...")
            results = self.run_analysis(problem_num, n_values)
            
            if results:
                all_results[problem_num] = results
                n_vals = [r['n'] for r in results]
                times_ms = [r['time_ms'] for r in results]
                
                problem_info = Algorithms.get_problem_info(problem_num)
                label = f'Problema {problem_num}: {problem_info["complexity"]}'
                
                plt.plot(n_vals, times_ms, f'{colors[i % len(colors)]}o-', 
                        linewidth=2, markersize=8, label=label)
        
        plt.xlabel('Tamaño de Input (n)', fontsize=12)
        plt.ylabel('Tiempo de Ejecución (ms)', fontsize=12)
        plt.title('Comparación de Complejidades Temporales', fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.legend(fontsize=11)
        plt.yscale('log')  # Escala logarítmica para mejor comparación
        plt.tight_layout()
        
        # Guardar comparación
        comparison_path = os.path.join(self.results_dir, 'comparison_all_problems.png')
        plt.savefig(comparison_path, dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"\nGráfica de comparación guardada en: {comparison_path}")
        
        return all_results