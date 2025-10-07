# Analizador de Complejidad Temporal

Este proyecto implementa un analizador de complejidad temporal modular para diferentes algoritmos, permitiendo medir, visualizar y comparar el rendimiento de cada uno de manera interactiva.

## 🚀 Características Principales

- **Sistema Modular:** Arquitectura bien estructurada con separación de responsabilidades
- **Análisis Interactivo:** Menú intuitivo para seleccionar problemas específicos
- **Visualización Avanzada:** Gráficas de alta calidad con escalas lineales
- **Exportación de Datos:** Resultados automáticos en CSV y PNG
- **Comparación Múltiple:** Análisis comparativo de todos los problemas
- **Configuración Flexible:** Valores de n personalizables
- **Optimización Inteligente:** Ajuste automático de rangos según complejidad

## 📁 Estructura del Proyecto

```
LAB8_TC/
├── menu.py                    # 🎯 Punto de entrada - Sistema de menú interactivo
├── algorithms.py              # 🧮 Implementaciones de los 3 problemas
├── analyzer.py                # 📊 Motor de análisis y visualización
├── algorithm_analysis.py      # 📈 Implementación original del Problema 1
├── complexity_analyzer.py     # 🔧 Analizador legacy (mantenido por compatibilidad)
├── requirements.txt           # 📦 Dependencias de Python
├── README.md                  # 📖 Esta documentación
├── __pycache__/              # 🗂️ Archivos compilados de Python
└── results/                   # 📁 Carpeta de resultados automáticos
    ├── performance_analysis_problem_1.png
    ├── performance_analysis_problem_2.png
    ├── performance_analysis_problem_3.png
    ├── performance_results_problem_1.csv
    ├── performance_results_problem_2.csv
    └── performance_results_problem_3.csv
```

## 🧮 Problemas Implementados

### Problema 1: Triple Bucles Anidados
**Complejidad Teórica:** O(n² log n)

```c
void function(int n) { 
    int i, j, k, counter = 0; 
    for (i = n / 2; i <= n; i++) {           // n/2 iteraciones
        for (j = 1; j + n / 2 <= n; j++) {   // n/2 iteraciones  
            for (k = 1; k <= n; k = k * 2) { // log n iteraciones
                counter++; 
            } 
        } 
    } 
}
```
**Análisis:** (n/2) × (n/2) × (log n) = O(n² log n)

### Problema 2: Doble Bucle con Break
**Complejidad Teórica:** O(n)

```c
void function(int n) { 
    if (n <= 1) return; 
    int i, j; 
    for (i = 1; i <= n; i++) {      // n iteraciones
        for (j = 1; j <= n; j++) {  // Solo 1 iteración por el break
            printf("Sequence\\n"); 
            break;                   // Rompe el bucle interno
        } 
    } 
}
```
**Análisis:** n × 1 = O(n) - El break hace que el bucle interno solo ejecute una vez

### Problema 3: Bucles Anidados con Incrementos Específicos
**Complejidad Teórica:** O(n²)

```c
void function(int n) {
    int i, j, counter = 0;
    for (i = 1; i <= n/3; i++) {     // n/3 iteraciones
        for (j = 1; j <= n/4; j++) { // n/4 iteraciones
            counter++;
        }
    }
}
```
**Análisis:** (n/3) × (n/4) = n²/12 = O(n²)

## 🛠️ Instalación

### Prerrequisitos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el proyecto:**
```bash
cd LAB8_TC
```

2. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

3. **Verificar instalación:**
```bash
python menu.py
```

## 🎮 Uso del Sistema

### Método Principal (Recomendado)
```bash
python menu.py
```

### Menú Interactivo

El sistema presenta las siguientes opciones:

```
╔══════════════════════════════════════════════════════════════╗
║                    ANALIZADOR DE COMPLEJIDAD                 ║
║                         TEMPORAL                             ║
╠══════════════════════════════════════════════════════════════╣
║  1. Analizar Problema 1 - O(n² log n)                      ║
║  2. Analizar Problema 2 - O(n)                             ║
║  3. Analizar Problema 3 - O(n²)                            ║
║  4. Comparar todos los problemas                            ║
║  5. Configurar valores de n personalizados                  ║
║  0. Salir                                                   ║
╚══════════════════════════════════════════════════════════════╝
```

### Métodos Alternativos

**Análisis individual del Problema 1:**
```bash
python algorithm_analysis.py
```

**Analizador legacy:**
```bash
python complexity_analyzer.py
```

## 🔧 Arquitectura del Sistema

### Módulo `algorithms.py`
- **Propósito:** Implementaciones de los algoritmos
- **Funciones principales:**
  - `problem_1(n)`, `problem_2(n)`, `problem_3(n)`
  - `get_theoretical_complexity(problem_num)`
  - `get_problem_info(problem_num)`

### Módulo `analyzer.py`
- **Propósito:** Motor de análisis y visualización
- **Clase principal:** `PerformanceAnalyzer`
- **Métodos clave:**
  - `profile_algorithm()`: Medición de rendimiento
  - `run_analysis()`: Análisis completo
  - `create_results_table()`: Generación de tablas
  - `create_visualization()`: Creación de gráficas
  - `save_results_to_csv()`: Exportación de datos

### Módulo `menu.py`
- **Propósito:** Interfaz de usuario y coordinación
- **Clase principal:** `MenuSystem`
- **Funcionalidades:**
  - Menú interactivo
  - Gestión de opciones
  - Configuración personalizada

## 🎯 Casos de Uso

### 1. Análisis Individual
```bash
python menu.py
# Seleccionar opción 1, 2 o 3
```

### 2. Comparación Múltiple
```bash
python menu.py
# Seleccionar opción 4
```

### 3. Configuración Personalizada
```bash
python menu.py
# Seleccionar opción 5
# Ingresar valores de n personalizados
```

### 4. Análisis Rápido (Problema 1)
```bash
python algorithm_analysis.py
```

## 🛡️ Manejo de Errores

- **Interrupciones seguras:** Ctrl+C manejado correctamente
- **Validación de entrada:** Verificación de valores de n
- **Gestión de memoria:** Optimización para valores grandes
- **Timeouts inteligentes:** Prevención de ejecuciones excesivamente largas

## 📦 Dependencias

```txt
matplotlib>=3.5.0    # Visualización de gráficas
numpy>=1.21.0        # Cálculos numéricos eficientes
pandas>=1.3.0        # Manejo y exportación de datos
tabulate>=0.8.9      # Formateo elegante de tablas
```