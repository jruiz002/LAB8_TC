import time
import cProfile
import pstats
import io
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def algorithm_function(n):
    """
    Python implementation of the C algorithm
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

def profile_function(n):
    """Profile the algorithm function and return execution time"""
    start_time = time.perf_counter()
    result = algorithm_function(n)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return execution_time, result

def detailed_profile(n):
    """Detailed profiling using cProfile"""
    pr = cProfile.Profile()
    pr.enable()
    result = algorithm_function(n)
    pr.disable()
    
    # Get stats
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats()
    
    return result, s.getvalue()

def run_performance_analysis():
    """Run performance analysis for different values of n"""
    n_values = [1, 10, 100, 1000, 10000]
    results = []
    
    print("Ejecutando análisis de rendimiento...")
    print("=" * 50)
    
    for n in n_values:
        print(f"Procesando n = {n:,}...")
        
        # Run multiple times and take average for more accurate measurements
        times = []
        counter_result = None
        
        for _ in range(3):  # Run 3 times for averaging
            exec_time, counter = profile_function(n)
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
            'theoretical_complexity': n * n * np.log2(n) if n > 0 else 0
        })
        
        print(f"  Tiempo promedio: {avg_time:.6f} segundos ({avg_time * 1000:.3f} ms)")
        print(f"  Operaciones contador: {counter_result:,}")
    
    return results

def create_results_table(results):
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
    print("TABLA DE RESULTADOS")
    print("=" * 80)
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    
    return table_data, headers

def create_visualization(results):
    """Create visualization graph - Linear scale only"""
    n_values = [r['n'] for r in results]
    times_ms = [r['time_ms'] for r in results]
    
    # Create single figure with linear scale plot
    plt.figure(figsize=(10, 6))
    
    plt.plot(n_values, times_ms, 'bo-', linewidth=2, markersize=8, label='Tiempo medido')
    plt.xlabel('Tamaño de Input (n)', fontsize=12)
    plt.ylabel('Tiempo de Ejecución (ms)', fontsize=12)
    plt.title('Tiempo de Ejecución vs Tamaño de Input', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=11)
    
    # Format the plot for better appearance
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('performance_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()

def save_results_to_csv(results):
    """Save results to CSV file"""
    df = pd.DataFrame(results)
    csv_path = 'performance_results.csv'
    df.to_csv(csv_path, index=False)
    print(f"\nResultados guardados en: {csv_path}")

def main():
    """Main function to run the complete analysis"""
    print("ANÁLISIS DE COMPLEJIDAD TEMPORAL")
    print("=" * 50)
    print("Algoritmo: Tres bucles anidados")
    print("Complejidad teórica: O(n² log n)")
    print("=" * 50)
    
    # Run performance analysis
    results = run_performance_analysis()
    
    # Create and display table
    table_data, headers = create_results_table(results)
    
    # Create visualizations
    print("\nGenerando gráficas...")
    create_visualization(results)
    
    # Save results
    save_results_to_csv(results)
    
    # Analysis summary
    print("\n" + "=" * 80)
    print("RESUMEN DEL ANÁLISIS")
    print("=" * 80)
    print(f"• Complejidad teórica: O(n² log n)")
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

if __name__ == "__main__":
    main()