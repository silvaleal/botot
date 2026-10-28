# botot

Aplicativo desktop minimalista que trás o PHP para o mundo dos desktops.

## Requisitos

- Python 3.10+ (testado com 3.14)
- PHP 3+

## Instalação

```bash
# Preparando o ambiente
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Instalação
./install.sh
botot /caminho/do/projeto-php
```

## Limitações

- A porta está fixa em `3011` no ponto de entrada atual.
- Não há verificação de porta ocupada nem reinício automático do servidor.
- Destinado a desenvolvimento local, não a produção.
