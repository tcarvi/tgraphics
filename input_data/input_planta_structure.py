#!/usr/bin/env python
# structure = [
#   [ 
#       tipoDoDesenho,    
#       [ deslocamento-inicial ],
#       comprimentoX,
#       comprimentoY,
#       comprimentoZ
#   ],
#   [ 
#       tipoDoDesenho,    
#       [ deslocamento-inicial ],
#       comprimentoX,
#       comprimentoY,
#       comprimentoZ
#   ],
#   ...
# ]
# 0 Deslocamento x
# 1 Deslocamento y
# 2 Deslocamento Z
# 10 Rotacionar X
# 11 Rotacionar Y
# 12 Rotacionar Z
# 20 Parede de 0.15
# 21 Parede de 0.20
structure = [
    [
        20,
        8.80
    ],
    [
        0,
        3.00
    ],
    [
        20,
        8.30
    ],
    [
        21,
        22.90
    ]
]
# Desenho [0] P1C1
# deslocamentoD0 = [0.00, 0.00, 0.00]
# verticesD0 = [
#     [0.00, 0.00, 0.00],
#     [0.00, 0.15, 0.00],
#     [0.15, 0.15, 0.00],
#     [0.15, 0.00, 0.00]
# ]
# edgesD0 = []
# facesD0 = [0, 1, 2, 3]
# d0 = [
#     deslocamentoD0,
#     verticesD0,
#     edgesD0,
#     facesD0
# ]