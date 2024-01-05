#!/bin/bash

# Atualiza a lista de pacotes
# Baixa Todos Os Pacotes Disponíveis No Repositório Do Termux 
pkg update -y
pkg upgrade -y

# ObtÃ©m a lista de todos os pacotes disponÃ­veis
all_packages=$(pkg list-all)

# Itera sobre a lista e tenta instalar cada pacote
for package in $all_packages; do
  pkg install -y "$package"
done

echo "Instalação de todas as ferramentas concluida."
