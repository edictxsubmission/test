#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 16:01:36 2018

@author: eliuc
"""

class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None
        
class Fake_LL(object):
    def __init__(self,x):
        self.head = None
    def add(self,x):
        new = ListNode(x)
        new.next = self.head
        self.head = new
