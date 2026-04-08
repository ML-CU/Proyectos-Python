# 📊 Evaluación Técnico-Económica de Cambio de Aceite en Pads de Molino SAG

## 🧠 Descripción del Proyecto

Este proyecto simula un caso real de ciencia de datos aplicado a minería, donde se evalúa el impacto de cambiar el aceite lubricante en los pads de un molino SAG.

El objetivo es responder:

> **¿Conviene cambiar al nuevo aceite considerando desempeño operativo, confiabilidad y costos?**

---

## 🎯 Objetivos

- Evaluar si el nuevo aceite reduce la temperatura de operación
- Determinar si el cambio es estadísticamente significativo
- Modelar el impacto en fallas del equipo
- Cuantificar el impacto económico
- Evaluar el riesgo asociado a la decisión

---

## 🏭 Contexto Operacional

Los pads del molino SAG son lubricados por un sistema centralizado, por lo que no es posible realizar pruebas A/B simultáneas.

Esto obliga a utilizar:

- análisis BEFORE/AFTER
- modelamiento estadístico
- simulación de escenarios

---

## 🔍 Metodología

### 1. Procesamiento de datos

- Datos de sensores (temperatura)
- Frecuencia original: 1 minuto
- Agregación: promedio por hora
- Limpieza y validación de datos

---

### 2. Análisis Exploratorio (EDA)

- Estadísticos descriptivos
- Visualización de distribuciones
- Identificación de outliers
- Evaluación de estabilidad del proceso

---

### 3. Prueba estadística (T-Test)

Se aplicó Welch T-test para comparar:

- Temperatura con aceite antiguo
- Temperatura con aceite nuevo

**Resultado:**
- p-value ≈ 0.0000  
- Conclusión: existe diferencia estadísticamente significativa

---

### 4. Modelamiento de Confiabilidad

Se utilizó simulación basada en distribución Weibull para modelar:

- Tiempo entre fallas (MTBF)
- Comportamiento probabilístico del sistema

---

### 5. Simulación Monte Carlo

Se realizaron múltiples simulaciones para estimar:

- Número de fallas por año
- Costos operacionales
- Variabilidad del sistema

---

### 6. Evaluación Económica

Resultados obtenidos:

- Costo promedio aceite antiguo: **108,600 USD**
- Costo promedio aceite nuevo: **65,580 USD**

👉 Ahorro estimado: **~43,000 USD/año**

---

### 7. Análisis de Riesgo

- Probabilidad de que el nuevo aceite sea peor: **36.6%**
- Pérdida promedio en escenarios negativos: **~17,100 USD**
- Peor escenario observado: **~150,000 USD**

---

## 🧠 Principales Insights

- La diferencia es estadísticamente significativa, pero eso no es suficiente para tomar decisiones
- El costo de falla domina el análisis económico
- El nuevo aceite reduce el costo total en promedio
- Existe incertidumbre relevante que debe ser gestionada
- Las decisiones deben basarse en **valor esperado y riesgo**, no solo en promedios

---

## ⚠️ Limitaciones

- Datos simulados (no provenientes de planta real)
- Supuestos simplificados en costos y distribución de fallas
- No se incluyeron todas las variables operacionales (carga, densidad, etc.)

---

## 🚀 Recomendación

Se recomienda:

- Implementación piloto controlada
- Monitoreo continuo de variables operacionales
- Validación con datos reales de planta
- Complementar con modelos multivariables

---

## 🛠️ Tecnologías utilizadas

- Python
- NumPy
- Pandas
- SciPy
- Matplotlib

---

## 📌 Próximos pasos

- Integrar regresión múltiple para controlar variables operacionales
- Implementar modelos de machine learning para mantenimiento predictivo
- Incorporar datos reales de planta
- Análisis de sensibilidad y escenarios

---

## 👨‍💻 Autor

Carlos Usca  
Ingeniero Industrial | Data Scientist enfocado en minería  

---

## 📈 Conclusión

Este proyecto demuestra cómo la ciencia de datos puede integrarse con ingeniería y negocio para tomar decisiones en entornos industriales complejos.

> **No se trata solo de analizar datos, sino de generar valor para la operación.**