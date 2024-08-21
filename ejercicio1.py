#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:23:34 2024

@author: ricardo
"""

# Ahora importamos las funciones de PyTC2
from pytc2.dibujar import dibujar_Pi, dibujar_Tee, dibujar_lattice
from pytc2.general import print_latex, print_subtitle, a_equal_b_latex_s
#from pytc2.dibujar import dibujar_elemento_serie, dibujar_elemento_derivacion, dibujar_espaciador, dibujar_espacio_derivacion, dibujar_puerto_entrada, dibujar_puerto_salida
#from schemdraw.elements import  Resistor, ResistorIEC, Capacitor, Inductor, Line, Dot, Gap, Arrow
import sympy as sp
from IPython.display import display,  Markdown
from pytc2.cuadripolos import Z2Tabcd_s, Y2Tabcd_s, Tabcd2Z_s, Tabcd2Y_s
from sympy import oo
from sympy import symbols, Matrix
from sympy import init_printing


#Ya = Y // Yb = Y/2  //Yc = Y/3 
Ya, Yb, Yc = sp.symbols('Ya, Yb, Yc', complex=True)
#Y = sp.symbols('Y', complex=True)
A = sp.symbols('A', real=True, positive=True)


Ypi = sp.Matrix([[Ya+Yb + A, -Yb+A], [-Yb + A, Yc + Yb + A]])
#Ypi = sp.Matrix([[Y+Y/2 + A, -Y/2+A], [-Y/2 + A, Y/3 + Y/2 + A]])

print('Red Pi')
print_latex(a_equal_b_latex_s('Y_{\pi}', Ypi))

print('Red equivalente')
dibujar_Pi(Ypi)


display(Markdown('## Conversión Y - Z'))

print('Red Pi original')

print_latex(a_equal_b_latex_s('Y_{\pi}', Ypi))

dibujar_Pi(Ypi)

print('Conversión a Tee (T. Kennelly)')

Zpi = Ypi**-1
print_latex(a_equal_b_latex_s('Z_{\pi}', Zpi))

print('Red equivalente')

Zpi_a, Zpi_b, Zpi_c = dibujar_Tee(Zpi, return_components = True)

display(Markdown('para mayor claridad, si se trabaja un poco más las expresiones de los componentes quedan'))

print_latex(a_equal_b_latex_s('Z_{A\pi}', sp.simplify(sp.expand(Zpi_a)) ))

print_latex(a_equal_b_latex_s('Z_{B\pi}', sp.simplify(sp.expand(Zpi_b)) ))

print_latex(a_equal_b_latex_s('Z_{C\pi}', sp.simplify(sp.expand(Zpi_c)) ))

Zpi_sym = sp.simplify(Zpi.subs(Yb, 0.5))
Zpi_sym = sp.simplify(Zpi_sym.subs(Ya, 1))
Zpi_sym = sp.simplify(Zpi_sym.subs(Yc, 1/3))

print_latex(a_equal_b_latex_s('Z_{\pi}', Zpi_sym))



print('Si se sabe que Delta Y(trans) la A = 1/0 tiende a infinito')

print_latex(a_equal_b_latex_s('Z_{1red}', sp.limit(Zpi_sym [0], A, oo)))
print_latex(a_equal_b_latex_s('Z_{2red}', sp.limit(Zpi_sym [1], A, oo)))
print_latex(a_equal_b_latex_s('Z_{3red}', sp.limit(Zpi_sym [2], A, oo)))
print_latex(a_equal_b_latex_s('Z_{4red}', sp.limit(Zpi_sym [3], A, oo)))


