#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 00:21:40 2024

@author: ricardo
"""
"""
Matriz Admitancia Indefinida (MAI)
----------------------------------
Ejemplos de cálculo simbólico mediante MAI de una red T puenteada de R constante.

Referencias:
------------
Cap. 9. Avendaño L. Sistemas electrónicos Analógicos: Un enfoque matricial.
"""

import sympy as sp

from sympy import symbols, Matrix
from sympy import init_printing

from pytc2.cuadripolos import calc_MAI_impedance_ij, calc_MAI_vtransf_ij_mn, calc_MAI_ztransf_ij_mn
from pytc2.general import print_latex

init_printing()  # Inicializa la impresión en Jupyter

# T puenteado cargado: red de R constante
# explicación:
'''    
+ Numeramos los polos de 0 a n=3

  
    0----Ya----+---Yc---|
               |        |
              Yb        G
               |        |
    1----------+---------
    
'''    

Ya, Yb, Yc = sp.symbols('Ya Yb Yc', complex=True)
G = sp.symbols('G', real=True, positive=True)

input_port = [1, 0]
output_port = [3, 0]

# Armo la MAI

#               Nodos: 0      1        2        3
Ymai = sp.Matrix([  
                    [ Yb+G,     0,      -Yb,        -G],
                    [ 0,        Ya,     -Ya,        0],
                    [ -Yb,      -Ya,    Ya+Yb+Yc,   -Yc],
                    [ -G,       0,      -Yc,        G+Yc]
                 ])

con_detalles = False
# con_detalles = True
"""
# Calculo la Z en el puerto de entrada a partir de la MAI
Zmai = calc_MAI_impedance_ij(Ymai, 0, 1, verbose=con_detalles)

# Aplico la condición de R constante
display('si consideramos:')
print_latex( r'G^2 = Y_a . Y_b' )
display('entonces')
print_latex( r'Z_{{ {:d}{:d} }} = '.format(0,1) +  sp.latex(Zmai.subs(Ya*Yb, G**2)) )

display('Transferencia de tensión:')
Vmai = calc_MAI_vtransf_ij_mn(Ymai, 3, 0, 1,0, verbose=con_detalles)
Vmai = sp.simplify(Vmai.subs(Yb/Ya, 2))
Vmai_Ya = sp.simplify(Vmai.subs(Yb, 2*Ya))
Vmai_Yb = sp.simplify(Vmai.subs(Ya, 0.5*Yb))

print_latex( r'T^{{ {:d}{:d} }}_{{ {:d}{:d} }} = '.format(3, 0, 1,0) +  sp.latex(Vmai_Ya) + ' = ' + sp.latex(Vmai_Yb) )
"""
print('Transferencia de tensión:')
Vmai = calc_MAI_vtransf_ij_mn(Ymai, output_port[0], output_port[1], input_port[0], input_port[1], verbose=con_detalles)

print_latex( r'T^{{ {:d}{:d} }}_{{ {:d}{:d} }} = '.format(output_port[0], output_port[1], input_port[0], input_port[1]) +  sp.latex(Vmai) )

Vmai_sym = sp.simplify(Vmai.subs(Yc, 3*Ya))

Vmai_sym = sp.simplify(Vmai_sym.subs(G, 1))

Vmai_sym = sp.simplify(Vmai_sym.subs(1/(Ya*Yb), 9/8))

print_latex( r'T^{{ {:d}{:d} }}_{{ {:d}{:d} }} = '.format(output_port[0], output_port[1], input_port[0], input_port[1]) +  sp.latex(Vmai_sym) )


"""
display('Transimpedancia:')
Zmai = calc_MAI_ztransf_ij_mn(Ymai, 3, 1, 0, 1, verbose=con_detalles)
Zmai = sp.simplify(Zmai.subs(Ya*Yb, G**2))
Zmai_Ya = sp.simplify(Zmai.subs(Yb, G**2/Ya))
Zmai_Yb = sp.simplify(Zmai.subs(Ya, G**2/Yb))
print_latex( r'Z^{{ {:d}{:d} }}_{{ {:d}{:d} }} = '.format(3, 1, 0, 1) + sp.latex(Zmai_Ya) + ' = ' + sp.latex(Zmai_Yb) )
"""
