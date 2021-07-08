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
- Visualização aproximada com o *preview* de "Shade Smooth"

#### Refactor contínuo da "blocagem" das cenas ***Low Poly*** geradas automaticamente
- Sem alterar a posição e a topologia dos objetos Low Poly já gerados, acrescentar outros objetos 3D necessários.
- Identificar comandos e incluí-los no arquivo de input, com a repetição da geração automática das cenas "Low Poly".
- Concluir blocagem quando não houver mais objetos e serem incluídos.

#### Vincular UVs nos objetos da cena
. . .

#### Incluir textura nos objetos
. . .

#### Lógica da automação:
- **Sempre buscar automatizar processos anteriores.**
- Apenas a parte artística, que não segue padronização de tamanhos e de simetria, não deve ser automatizada.
- O trabalho não-automatizado da criação artística deve se restringir à:
    - Acréscimo de objetos 3D no arquivo textual de *inputs*:
        - Escolha dos objetos a serem incluídos nas cenas
        - Identificação de tamanhos, distâncias e disposição destes objetos
        - Organização dos comandos a serem passados para a engine tcarviIAI
    - Correção e melhoria das texturas dos objetos "Low Poly" gerados automaticamente.
        - Documentar o trabalho artístico, para possível reexecução em cenas "Low Poly" geradas novamente.

---

#### Animação de Movimentos 
- Modelo da animação:
    - [Movimento da Cena de Luta (1)](https://www.youtube.com/watch?v=Um8i-glXSzY&list=PLHZr_2UlXu7DQGrSztRSCzNEYpk6Nso4f&index=34&t=10s)
    - [Movimento da Cena de Luta (2)](https://www.youtube.com/watch?v=G95jgdwyq_Q&list=PLHZr_2UlXu7DQGrSztRSCzNEYpk6Nso4f&index=35)
    - [Movimento da Cena de Luta (3)](https://www.youtube.com/watch?v=Q0mNooEcpk0&list=PLHZr_2UlXu7DQGrSztRSCzNEYpk6Nso4f&index=36)

---

#### Renderização do Visual
- Modelo da renderização:

---

#### Edição do áudio da comunicação:
- Modelo de Comunicação:

---

#### Edição do Áudio Musical
- Modelo de Música:
    - [Música empolgante (1)](https://www.youtube.com/watch?v=l264SGk15O0&list=PLHZr_2UlXu7DQGrSztRSCzNEYpk6Nso4f&index=37)
    - [Música empolgante (2)](https://www.youtube.com/watch?v=ZKkzEBtIoH8&list=PLHZr_2UlXu7DQGrSztRSCzNEYpk6Nso4f&index=38)
