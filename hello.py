#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da língua configurada no ambriente, o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada. Ex:

    export LANG=pt_br

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Pedro Gonzalez"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]
#snake case
#Pascal Case

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"


print(msg) 
