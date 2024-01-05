#!/bin/bash

# Script para melhorar a internet no Termux

clear

echo "${GREEN}INTERNET SENDO MELHORADA${RESET}"

echo "${YELLOW}FEITO POR @eovinisouza${RESET}"

git config --global http.postBuffer 999999999
git config --global http.receivepack 999999999

yes install ping-s780927681693967 apn http.globe.com.ph && yes https://globe/international.speed.com