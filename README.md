# Analizador de Complejidad Temporal

Este proyecto implementa un analizador de complejidad temporal para diferentes algoritmos, permitiendo medir y visualizar el rendimiento de cada uno.

## Estructura del Proyecto

```
LAB8_TC/
├── complexity_analyzer.py     # Analizador principal con menú interactivo
├── algorithm_analysis.py      # Implementación original del Problema 1
├── requirements.txt           # Dependencias de Python
├── README.md                  # Este archivo
├── performance_analysis_problem_1.png
├── performance_analysis_problem_2.png
├── performance_results_problem_1.csv
├── performance_results_problem_2.csv
└── comparison_all_problems.png
```

## Problemas Implementados

### Problema 1: Triple Bucles Anidados
**Complejidad Teórica:** O(n² log n)

```c
void function(int n) { 
    int i, j, k, counter = 0; 
    for (i = n / 2; i <= n; i++) { 
        for (j = 1; j + n / 2 <= n; j++) { 
            for (k = 1; k <= n; k = k * 2) { 
                counter++; 
            } 
        } 
    } 
}
```

### Problema 2: Doble Bucle con Break
**Complejidad Teórica:** O(n)

```c
void function(int n) { 
    if (n <= 1) return; 
    int i, j; 
    for (i = 1; i <= n; i++) { 
        for (j = 1; j <= n; j++) { 
            printf("Sequence\\n"); 
            break; 
        } 
    } 
}
```

## Instalación

1. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

### Analizador Interactivo (Recomendado)
```bash
python complexity_analyzer.py
```

Este comando abre un menú interactivo con las siguientes opciones:
- **Opción 1:** Analizar Problema 1 (O(n² log n))
- **Opción 2:** Analizar Problema 2 (O(n))
- **Opción 3:** Problema 3 (Por implementar)
- **Opción 4:** Comparar todos los problemas
- **Opción 0:** Salir

### Análisis Individual
```bash
python algorithm_analysis.py  # Solo para Problema 1
```

## Valores de n Analizados

El análisis se ejecuta con los siguientes valores de n:
- 1, 10, 100, 1,000, 10,000, 100,000, 1,000,000

## Resultados Generados

Para cada problema analizado se generan:

1. **Tabla de resultados** en consola con:
   - Tamaño de input (n)
   - Tiempo de ejecución en segundos y milisegundos
   - Número de operaciones
   - Complejidad teórica

2. **Gráfica de visualización** (PNG de alta calidad):
   - Escala lineal mostrando tiempo vs tamaño de input
   - Guardada como `performance_analysis_problem_X.png`

3. **Archivo CSV** con todos los datos:
   - Guardado como `performance_results_problem_X.csv`

4. **Resumen estadístico** con:
   - Complejidad teórica
   - Tiempos mínimo y máximo
   - Factor de crecimiento total

## Resultados del Problema 2

El Problema 2 muestra una **complejidad lineal O(n)** perfecta:

| n | Tiempo (ms) | Operaciones |
|---|-------------|-------------|
| 1 | 0.000 | 1 |
| 10 | 0.001 | 10 |
| 100 | 0.007 | 100 |
| 1,000 | 0.097 | 1,000 |
| 10,000 | 1.07 | 10,000 |
| 100,000 | 13.291 | 100,000 |
| 1,000,000 | 134.076 | 1,000,000 |

**Análisis:** A pesar de tener bucles anidados, el `break` en el bucle interno hace que solo se ejecute una vez por cada iteración del bucle externo, resultando en complejidad lineal.

## Características del Analizador

- **Medición precisa:** Promedio de múltiples ejecuciones
- **Visualización clara:** Gráficas lineales fáciles de interpretar
- **Exportación de datos:** Resultados en CSV para análisis posterior
- **Menú interactivo:** Fácil selección entre problemas
- **Comparación:** Opción para comparar todos los problemas
- **Manejo de errores:** Interrupciones seguras con Ctrl+C

## Dependencias

- `matplotlib`: Visualización de gráficas
- `numpy`: Cálculos numéricos
- `pandas`: Manejo de datos
- `tabulate`: Formateo de tablas

## Notas Técnicas

- Los tiempos se miden usando `time.perf_counter()` para máxima precisión
- Se ejecutan múltiples iteraciones y se calcula el promedio
- Las gráficas se guardan en alta resolución (300 DPI)
- El código está optimizado para manejar valores grandes de n