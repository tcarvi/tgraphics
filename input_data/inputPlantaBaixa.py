#!/usr/bin/env python

# Desenho [0] P1C1
deslocamentoD0 = [0.00, 0.00, 0.00]
verticesD0 = [
    [0.00, 0.00, 0.00],
    [0.00, 0.15, 0.00],
    [0.15, 0.15, 0.00],
    [0.15, 0.00, 0.00]
]
edgesD0 = []
facesD0 = [0, 1, 2, 3]
d0 = [
    deslocamentoD0,
    verticesD0,
    edgesD0,
    facesD0
]

# Desenho [1] P1
deslocamentoD1 = [0.00, 0.15, 0.00]
verticesD1 = [
    [0.00, 0.00, 0.00],
    [0.00, 8.20, 0.00],
    [0.15, 8.20, 0.00],
    [0.15, 0.00, 0.00]
]
edgesD1 = []
facesD1 = [0, 1, 2, 3]
d1 = [
    deslocamentoD0,
    verticesD0,
    edgesD0,
    facesD0
]

structure = [
    d0,
    d1
]