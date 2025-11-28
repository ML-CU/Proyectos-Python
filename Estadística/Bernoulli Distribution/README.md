# Probabilidad Aplicada a Minería  
## Distribución de Bernoulli, Binomial e Hipergeométrica con ejemplos reales

Este repositorio contiene un conjunto de ejercicios de **probabilidad aplicada a la ingeniería minera**, desarrollados en Python y orientados a analizar riesgos, fallas y calidad de repuestos en equipos de planta concentradora.

El notebook incluye simulaciones, uso de PMF y CDF, análisis interpretado y conclusiones operativas útiles para toma de decisiones.

---

# Contenido del Proyecto

## 1. Distribución de Bernoulli  
Base teórica utilizada para modelar eventos con dos posibles resultados:

- **1 = éxito** (evento ocurre: falla, defecto, alarma)
- **0 = fracaso** (no ocurre)

**Fórmulas clave:**
- Valor esperado: `E[X] = p`
- Varianza: `Var(X) = p(1−p)`

### ✔ Ejemplo incluido  
Simulación de resultados usando la función `utility()` con un dado para validar convergencia del valor esperado a `p = 4/6`.

---

## 2. Distribución Binomial  
Se interpreta como la repetición de **n ensayos Bernoulli** independientes con probabilidad constante.

El notebook explica:
- PMF: `P(X = k)`
- CDF: `P(X ≤ k)`
- Cálculos para:
  - `P(X ≥ k)`
  - `P(X > k)`
  - `P(X ≤ k)`
  - `P(X < k)`

---

## 3. Ejemplo Binomial Aplicado a Minería  
### Caso: Paradas de una Bomba Warman  
- Probabilidad mensual de parada: `p = 0.15`  
- Horizonte: `12 meses`  

### Resultados clave
- Lo más probable: **1–2 paradas por año**.  
- `P(X ≤ 2) ≈ 0.736` → 74% de probabilidad de tener como máximo 2 fallas.  
- `P(X ≥ 3) ≈ 0.264` → 26% de riesgo de sobrepasar la capacidad planificada.

### Conclusión operativa  
La mayor parte del presupuesto debe centrarse en 1–2 intervenciones, pero se debe disponer de contingencia para 3 o más.

---

## 4. Distribución Hipergeométrica  
Aplicada cuando **no hay reemplazo** y la probabilidad cambia en cada extracción.  
Muy útil para evaluar *calidad de lotes de repuestos*.

---

## 5. Ejemplo Hipergeométrica Aplicado a Minería  
### Caso: Lote de Liners de Molino SAG  
- Total: `N = 180` liners  
- Defectuosos: `D = 12`  
- Selección para instalación: `n = 20`  

### Resultados principales
- `P(X = 0) = 0.232`  
  - **Conclusión:** Solo 23% de las selecciones estarán completamente limpias.  
- `P(X ≥ 1) = 0.768`  
  - **Conclusión:** 77% de probabilidad de instalar *al menos* un liner defectuoso.  
- `P(X = 2) = 0.244`  
  - **Conclusión:** Caso más representativo entre los defectuosos: 2 liners.  
- `P(X ≥ 4) ≈ 0.04`  
  - **Conclusión:** Eventos críticos son pocos pero muy graves → necesidad de inspección rigurosa.

El notebook incluye:
- PMF  
- CDF  
- Cálculo de:
  - `P(X ≥ k)`
  - `P(X > k)`
  - `P(X ≤ k)`
  - `P(X < k)`

---

# 📊 Resumen Operativo

Este proyecto permite:
- Estimar fallas esperadas en equipos mineros (bombas, fajas, celdas, etc.)
- Evaluar la calidad de lotes de repuestos mediante probabilidad
- Justificar decisiones técnicas con cálculos y simulaciones
- Explicar PMF y CDF de forma entendible para personal operativo y gerencial

---


