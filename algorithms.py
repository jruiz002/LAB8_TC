"""
Módulo de Algoritmos para Análisis de Complejidad Temporal
Contiene las implementaciones de los tres problemas a analizar.
"""

import numpy as np

class Algorithms:
    """Clase que contiene todos los algoritmos a analizar"""
    
    @staticmethod
    def problem_1(n):
        """
        Problema 1: Triple bucles anidados
        Complejidad teórica: O(n² log n)
        
        Algoritmo C original:
        for (i = n / 2; i <= n; i++) { 
            for (j = 1; j + n / 2 <= n; j++) { 
                for (k = 1; k <= n; k = k * 2) { 
                    counter++; 
                } 
            } 
        }
        """
        counter = 0
        
        # Primer bucle: i desde n//2 hasta n (inclusive)
        for i in range(n // 2, n + 1):
            # Segundo bucle: j desde 1 mientras j + n//2 <= n
            j = 1
            while j + n // 2 <= n:
                # Tercer bucle: k potencias de 2 desde 1 hasta n
                k = 1
                while k <= n:
                    counter += 1
                    k = k * 2
                j += 1
        
        return counter
    
    @staticmethod
    def problem_2(n):
        """
        Problema 2: Doble bucle con break
        Complejidad teórica: O(n)
        
        Algoritmo C original:
        if (n <= 1) return; 
        for (i = 1; i <= n; i++) { 
            for (j = 1; j <= n; j++) { 
                printf("Sequence\\n"); 
                break; 
            } 
        }
        """
        if n <= 1:
            return 0
            
        counter = 0
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                counter += 1  # Simula el printf
                break  # Este break hace que sea O(n) en lugar de O(n²)
        
        return counter
    
    @staticmethod
    def problem_3(n):
        """
        Problema 3: Bucles anidados con incrementos específicos
        
        Algoritmo C original:
        for (i = 1; i <= n / 3; i++) {
            for (j = 1; j <= n; j += 4) {
                printf("Sequence\n");
            }
        }
        
        Complejidad: O(n²)
        - Bucle externo: n/3 iteraciones
        - Bucle interno: n/4 iteraciones
        - Total: (n/3) * (n/4) = n²/12 = O(n²)
        
        Args:
            n (int): Tamaño de entrada
            
        Returns:
            int: Número de operaciones realizadas
        """
        operations = 0
        
        # Bucle externo: i de 1 hasta n/3
        for i in range(1, (n // 3) + 1):
            # Bucle interno: j de 1 hasta n, incrementando de 4 en 4
            j = 1
            while j <= n:
                # Operación principal (equivalente a printf)
                operations += 1
                j += 4
        
        return operations
    
    @staticmethod
    def get_theoretical_complexity(problem_num, n):
        """
        Calcula la complejidad teórica para cada problema
        
        Args:
            problem_num (int): Número del problema (1, 2, o 3)
            n (int): Tamaño de entrada
            
        Returns:
            float: Valor teórico de la complejidad
        """
        if problem_num == 1:
            # O(n² log n)
            return n * n * np.log2(n) if n > 0 else 0
        elif problem_num == 2:
            # O(n)
            return n
        elif problem_num == 3:
            # O(n²/12) ≈ O(n²)
            return (n * n) / 12
        else:
            return 0
    
    @staticmethod
    def get_problem_info(problem_num):
        """
        Obtiene información detallada sobre cada problema
        
        Args:
            problem_num (int): Número del problema
            
        Returns:
            dict: Información del problema
        """
        problems_info = {
            1: {
                'name': 'Triple bucles anidados',
                'complexity': 'O(n² log n)',
                'description': 'Tres bucles anidados con incrementos específicos',
                'algorithm_func': Algorithms.problem_1
            },
            2: {
                'name': 'Doble bucle con break',
                'complexity': 'O(n)',
                'description': 'Bucles anidados con break que reduce la complejidad',
                'algorithm_func': Algorithms.problem_2
            },
            3: {
                'name': 'Bucles anidados con incrementos específicos',
                'complexity': 'O(n²)',
                'description': 'Bucle externo (n/3) × Bucle interno (n/4) = O(n²)',
                'algorithm_func': Algorithms.problem_3
            }
        }
        
        return problems_info.get(problem_num, {})
    
    @staticmethod
    def get_all_problems():
        """
        Retorna información de todos los problemas disponibles
        
        Returns:
            dict: Diccionario con información de todos los problemas
        """
        return {i: Algorithms.get_problem_info(i) for i in range(1, 4)}