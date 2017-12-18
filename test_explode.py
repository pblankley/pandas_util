#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 09:29:53 2017

@author: paulblankley
"""

# Need to work on this later
import pd_util as pu
import pandas as pd

def test_2col():
	test = pd.DataFrame({'col1':[[1,7],[8,5]],'col2':['mike','larry'],'col3': \
                     ['baby pig','llama'], 'col4':[['m','g'],['y','n']]})
	dfo = pu.explode_value(test,'col1','col4')
	check = pd.DataFrame({'col1': [1,7,8,5],'col2': ['mike','larry','mike','larry'], 'col3': \
				['baby pig','llama','baby pig','llama'],'col4': ['m','g','y','n']})
	assert(all(dfo==check))

def test_1col():
	test = pd.DataFrame({'col1':[[1,7],[8,5]],'col2':['mike','larry'],'col3': \
                     ['baby pig','llama']})
	dfo = pu.explode_value(test,'col1')	
	check = pd.DataFrame({'col1': [1,7,8,5],'col2': ['mike','larry','mike','larry'], 'col3': \
				['baby pig','llama','baby pig','llama']})
	assert(all(check==dfo))

def test_notdf():	
	check = [1,2,3,4,5,6,9,8,6]
	try:
		pu.explode_value(check, 'col1')
	except ValueError as err:
		assert(type(err)==ValueError)
	
def test_nocol():
	test = pd.DataFrame({'col1':[[1,7],[8,5]],'col2':['mike','larry'],'col3': \
                     ['baby pig','llama'], 'col4':[['m','g'],['y','n']]})
	try:
		pu.explode_value(test,'no_col_here')
	except KeyError as err:
		assert(type(err)==KeyError)

def test_collen():
	test = pd.DataFrame({'col1':[[1,7],[8,5]],'col2':['mike','larry'],'col3': \
                     ['baby pig','llama'], 'col4':[['m','g','g'],['y','n','e']]})
	try:
		pu.explode_value(test,'col1','col2')
	except ValueError as err:
		assert(type(err)==ValueError)


test_2col()
test_1col()
test_notdf()	
test_nocol()
test_collen()

