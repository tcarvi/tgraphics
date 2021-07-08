---
title: Fluxo de Trabalho
sidebar_position: 1
---

### Pensar nos cenários e nos objetos
- Definir distâncias e objetos

### Automatizar criação de cenários e objetos Low Poly
- Identificar comandos a serem passados para engine tcarviAI
- Manipular arquivos de input
- Enviar comandos para engine tcarviAI
- Avaliar produtos *Low Poly* gerados
    - Quantificar vertex, edges e faces
    - Corrigir, no arquivo de input, a qualidade dos objetos, buscando superfícies com poucos quadrados.
    - Corrigir, no arquivo de input, a disposição dos objetos gerados.
- Renviar comandos para geração de cenas ***Low Poly***

#### Sobre técnica "Low Poly"
- Objetos iniciais da manipulação devem ter poucos polígonos
- Ondulações da borda de superfícies devem ser feitas com:
    - Novos ***edges*** próximo da curvatura, através de ***Loop Cut Slide*** ou de ***Knife***.
    - ***Extrude*** dos novos quadrados
