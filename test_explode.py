#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 09:29:53 2017

@author: paulblankley
"""
import pd_util as pu

test = pd.DataFrame({'col1':[[1,7,4],[8,5,3]],'col2':['mike','larry'],'col3': \
                     ['baby pig','llama'], 'col4':[['m','g','d'],['y','n','g']]})    
test.head()
dfo = pu.explode_value(test,'col2')
dfo.head()