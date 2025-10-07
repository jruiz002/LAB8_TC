import time
import cProfile
import pstats
import io
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

class ComplexityAnalyzer:
    def __init__(self):
        self.results = []
        self.current_problem = None
        
    def algorithm_problem_1(self, n):
        """
        Problem 1: Triple nested loops
        Time complexity: O(n² log n)
        """
        counter = 0
        
        # First loop: i from n//2 to n (inclusive)
        for i in range(n // 2, n + 1):
            # Second loop: j from 1 while j + n//2 <= n
            j = 1
            while j + n // 2 <= n:
                # Third loop: k powers of 2 from 1 to n
                k = 1
                while k <= n:
                    counter += 1
                    k = k * 2
                j += 1
        
        return counter
    
    def algorithm_problem_2(self, n):
        """
        Problem 2: Double nested loops with break
        Time complexity: O(n)
        """
        if n <= 1:
            return 0
            
        counter = 0
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                counter += 1  # Simulating the printf operation
                break  # This break makes the inner loop execute only once
        
        return counter
    
    def algorithm_problem_3(self, n):
        """
        Problem 3: Placeholder for future implementation
        Time complexity: TBD
        """
        # Placeholder - will be implemented later
        return n
    
    def profile_function(self, algorithm_func, n):
        """Profile the algorithm function and return execution time"""
        start_time = time.perf_counter()
        result = algorithm_func(n)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        return execution_time, result
    
    def get_theoretical_complexity(self, problem_num, n):
        """Get theoretical complexity for each problem"""
        if problem_num == 1:
            return n * n * np.log2(n) if n > 0 else 0
        elif problem_num == 2:
            return n  # Linear complexity
        elif problem_num == 3:
            return n  # Placeholder
        return 0
    
    def run_performance_analysis(self, problem_num):
        """Run performance analysis for selected problem"""
        n_values = [1, 10, 100, 1000, 10000, 100000, 1000000]
        results = []
        
        # Select algorithm based on problem number
        if problem_num == 1:
            algorithm_func = self.algorithm_problem_1
            problem_name = "Problema 1: Triple bucles anidados (O(n² log n))"
        elif problem_num == 2:
            algorithm_func = self.algorithm_problem_2
            problem_name = "Problema 2: Doble bucle con break (O(n))"
        elif problem_num == 3:
            algorithm_func = self.algorithm_problem_3
            problem_name = "Problema 3: Por implementar"
        else:
            print("Problema no válido")
            return []
        
        print(f"Ejecutando análisis de rendimiento para {problem_name}")
        print("=" * 70)
        
        for n in n_values:
            print(f"Procesando n = {n:,}...")
            
            # Run multiple times and take average for more accurate measurements
            times = []
            counter_result = None
            
            # Adjust number of runs based on expected execution time
            num_runs = 5 if n <= 10000 else 3 if n <= 100000 else 1
            
            for _ in range(num_runs):
                exec_time, counter = self.profile_function(algorithm_func, n)
                times.append(exec_time)
                counter_result = counter
            
            avg_time = np.mean(times)
            std_time = np.std(times)
            
            results.append({
                'n': n,
                'time_seconds': avg_time,
                'time_ms': avg_time * 1000,
                'std_dev': std_time,
                'counter_operations': counter_result,
                'theoretical_complexity': self.get_theoretical_complexity(problem_num, n)
            })
            
            print(f"  Tiempo promedio: {avg_time:.6f} segundos ({avg_time * 1000:.3f} ms)")
            print(f"  Operaciones contador: {counter_result:,}")
        
        self.results = results
        self.current_problem = problem_num
        return results
    
    def create_results_table(self, results, problem_num):
        """Create and display results table"""
        table_data = []
        for result in results:
            table_data.append([
                f"{result['n']:,}",
                f"{result['time_seconds']:.6f}",
                f"{result['time_ms']:.3f}",
                f"{result['counter_operations']:,}",
                f"{result['theoretical_complexity']:.0f}"
            ])
        
        headers = ["Tamaño de Input (n)", "Tiempo (segundos)", "Tiempo (ms)", 
                   "Operaciones", "Complejidad Teórica"]
        
        print("\n" + "=" * 80)
        print(f"TABLA DE RESULTADOS - PROBLEMA {problem_num}")
        print("=" * 80)
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        
        return table_data, headers
    
    def create_visualization(self, results, problem_num):
        """Create visualization graph - Linear scale only"""
        n_values = [r['n'] for r in results]
        times_ms = [r['time_ms'] for r in results]
        
        # Create single figure with linear scale plot
        plt.figure(figsize=(12, 7))
        
        plt.plot(n_values, times_ms, 'bo-', linewidth=2, markersize=8, label='Tiempo medido')
        plt.xlabel('Tamaño de Input (n)', fontsize=12)
        plt.ylabel('Tiempo de Ejecución (ms)', fontsize=12)
        plt.title(f'Problema {problem_num}: Tiempo de Ejecución vs Tamaño de Input', 
                 fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.legend(fontsize=11)
        
        # Format the plot for better appearance
        plt.tight_layout()
        
        # Save the plot
        filename = f'performance_analysis_problem_{problem_num}.png'
        filepath = os.path.join('/Users/joseruiz_002/Documents/UVG/6to Semestre/Teoria de la computacion/LAB8_TC', filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"Gráfica guardada como: {filename}")
    
    def save_results_to_csv(self, results, problem_num):
        """Save results to CSV file"""
        df = pd.DataFrame(results)
        filename = f'performance_results_problem_{problem_num}.csv'
        csv_path = os.path.join('/Users/joseruiz_002/Documents/UVG/6to Semestre/Teoria de la computacion/LAB8_TC', filename)
        df.to_csv(csv_path, index=False)
        print(f"Resultados guardados en: {filename}")
    
    def display_analysis_summary(self, results, problem_num):
        """Display analysis summary"""
        print("\n" + "=" * 80)
        print(f"RESUMEN DEL ANÁLISIS - PROBLEMA {problem_num}")
        print("=" * 80)
        
        if problem_num == 1:
            print("• Complejidad teórica: O(n² log n)")
        elif problem_num == 2:
            print("• Complejidad teórica: O(n)")
        elif problem_num == 3:
            print("• Complejidad teórica: Por determinar")
            
        print(f"• Valores de n analizados: {len(results)}")
        print(f"• Tiempo mínimo: {min(r['time_ms'] for r in results):.3f} ms")
        print(f"• Tiempo máximo: {max(r['time_ms'] for r in results):.3f} ms")
        
        # Calculate growth factor
        if len(results) > 1:
            first_time = results[0]['time_ms']
            last_time = results[-1]['time_ms']
            if first_time > 0:
                growth_factor = last_time / first_time
                print(f"• Factor de crecimiento total: {growth_factor:.2f}x")
        
        print("=" * 80)
    
    def show_menu(self):
        """Display main menu"""
        print("\n" + "=" * 60)
        print("    ANALIZADOR DE COMPLEJIDAD TEMPORAL")
        print("=" * 60)
        print("Seleccione el problema a analizar:")
        print()
        print("1. Problema 1: Triple bucles anidados (O(n² log n))")
        print("2. Problema 2: Doble bucle con break (O(n))")
        print("3. Problema 3: Por implementar")
        print("4. Comparar todos los problemas")
        print("0. Salir")
        print("=" * 60)
    
    def compare_all_problems(self):
        """Compare all implemented problems"""
        print("\n" + "=" * 60)
        print("COMPARACIÓN DE TODOS LOS PROBLEMAS")
        print("=" * 60)
        
        # Run analysis for problems 1 and 2
        results_1 = self.run_performance_analysis(1)
        results_2 = self.run_performance_analysis(2)
        
        # Create comparison visualization
        n_values = [r['n'] for r in results_1]
        times_1 = [r['time_ms'] for r in results_1]
        times_2 = [r['time_ms'] for r in results_2]
        
        plt.figure(figsize=(12, 7))
        plt.plot(n_values, times_1, 'bo-', linewidth=2, markersize=8, label='Problema 1: O(n² log n)')
        plt.plot(n_values, times_2, 'ro-', linewidth=2, markersize=8, label='Problema 2: O(n)')
        plt.xlabel('Tamaño de Input (n)', fontsize=12)
        plt.ylabel('Tiempo de Ejecución (ms)', fontsize=12)
        plt.title('Comparación de Complejidades Temporales', fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.legend(fontsize=11)
        plt.yscale('log')  # Log scale for better comparison
        plt.tight_layout()
        
        comparison_path = '/Users/joseruiz_002/Documents/UVG/6to Semestre/Teoria de la computacion/LAB8_TC/comparison_all_problems.png'
        plt.savefig(comparison_path, dpi=300, bbox_inches='tight')
        plt.show()
        
        print("Gráfica de comparación guardada como: comparison_all_problems.png")
    
    def run(self):
        """Main execution loop"""
        while True:
            self.show_menu()
            try:
                choice = input("\nIngrese su opción (0-4): ").strip()
                
                if choice == '0':
                    print("¡Gracias por usar el Analizador de Complejidad Temporal!")
                    break
                elif choice in ['1', '2', '3']:
                    problem_num = int(choice)
                    if problem_num == 3:
                        print("El Problema 3 aún no está implementado.")
                        continue
                    
                    # Run analysis
                    results = self.run_performance_analysis(problem_num)
                    
                    if results:
                        # Display table
                        self.create_results_table(results, problem_num)
                        
                        # Create visualization
                        print("\nGenerando gráfica...")
                        self.create_visualization(results, problem_num)
                        
                        # Save results
                        self.save_results_to_csv(results, problem_num)
                        
                        # Display summary
                        self.display_analysis_summary(results, problem_num)
                
                elif choice == '4':
                    self.compare_all_problems()
                
                else:
                    print("Opción no válida. Por favor, seleccione una opción del 0 al 4.")
                    
            except KeyboardInterrupt:
                print("\n\nOperación interrumpida por el usuario.")
                break
            except Exception as e:
                print(f"Error: {e}")
                continue
            
            input("\nPresione Enter para continuar...")

def main():
    """Main function"""
    analyzer = ComplexityAnalyzer()
    analyzer.run()

if __name__ == "__main__":
    main()