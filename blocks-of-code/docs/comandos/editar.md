---
title: "Editar"
sidebar_position: 4
---

## Delete
- `SELECT` `X` -> Delete selection

## Extrude em X, Y ou Z
- Extrude EDGE:
    - `Tab Edit Mode` `2` `SELECT EDGE` `E` `X` -> Extrude Edge em X
    - `Tab Edit Mode` `2` `SELECT EDGE` `E` `Y` -> Extrude Edge em Y
    - `Tab Edit Mode` `2` `SELECT EDGE` `E` `Z` -> Extrude Edge em Z
- Extrude FACE:
    - `Tab Edit Mode` `3` `SELECT FACE` `E` `X` -> Extrude Face em X
    - `Tab Edit Mode` `3` `SELECT FACE` `E` `Y` -> Extrude Face em Y
    - `Tab Edit Mode` `3` `SELECT FACE` `E` `Z` -> Extrude Face em Z

## Loop Cut and Slide
- Criar Edges em um Loop do objeto.
- Posição do loop é escolhida com arrasto do mouse.
    - `Tab Edit Mode` `CTRL` `R` `Slide`

## Inset Face
- Cria polígono interno
- Polígono sem profundidade
- Polígono com ligação apenas nos cantos da seleção inicial de faces. 
    - `Tab Edit Mode` `3` `CTRL` `F` `N`

## Bevel
- Pode ser aplicado sobre Edges e sobre Faces
- `Tab Edit Mode` `2` `SELECT EDGE` `CRTL` `B` -> Criação paralela de Bevel
    - Depois abrir janela de configuração do bevel.
- `Tab Edit Mode` `3` `SELECT FACE` `CRTL` `B` -> Criação menor de Bevel, para fora ou para dentro.
    - Depois abrir janela de configuração do bevel.