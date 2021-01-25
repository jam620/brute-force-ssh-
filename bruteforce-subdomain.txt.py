#!/usr/local/bin/python3
# _*_ coding: utf8 _*_

import dns.resolver
from os import path


def main():
    if path.exists('subdominios.txt'):
        wordlist = open('subdominios.txt', 'r')
        wordlist = wordlist.read().split('\n')
        lista = []
        for subdomains in wordlist:
            lista = wordlist
            try:
                #toadsec.io es el objetivo
                a = dns.resolver.resolve('{}.google.com.format(subdomains), 'A')
                lista.append('{}.google.com'.format(subdomains))
            except:
                pass
        if len(lista) > 0:
            print('Numero de subdominios posibles: {}'.format(len(lista)))
            # print('Numero de subdominios posibles: {}'.format(lista))
            for elements in lista:
                # for iteracion in elements:
                # lista.append(elements.strip())
                print(elements)
        else:
            print("No se encontraron subdominios")
    else:
        print("No existe el archivo")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("[-] Saliendo")
        exit()
