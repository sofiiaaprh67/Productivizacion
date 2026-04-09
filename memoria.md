# Memoria del proyecto

## Nombre del proyecto
nube_wiki

## Objetivo
Crear una nube de palabras a partir del contenido de una página de Wikipedia en español.

## Entorno
Se ha creado un entorno conda llamado `nube_wiki`.

## Librerías usadas
- wikipedia
- matplotlib
- wordcloud
- stop-words
- jupyter

## Desarrollo realizado
1. Creación del entorno virtual con conda.
2. Instalación de librerías necesarias.
3. Desarrollo del script `nube.py`.
4. Inicialización del repositorio Git.
5. Uso de ramas `master`, `devel` y `features_ejemplos`.
6. Realización de merges entre ramas.
7. Resolución de conflicto final en `master`.
8. Exportación del entorno a `environment.yml`.

## Funcionamiento
La función `crear_nube(x)`:
- fija el idioma de Wikipedia a español,
- descarga la página indicada,
- limpia el texto,
- genera la nube de palabras,
- la representa por pantalla.

## Ramas usadas
- master
- devel
- features_ejemplos

## Resultado final
El proyecto genera nubes de palabras para:
- Madrid
- Getafe
- Toledo
