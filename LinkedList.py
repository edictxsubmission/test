#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 15:51:36 2018

@author: eliuc
"""

class Node(object):
    def __init__(self,data, next_node=None):
        self.data = data
        self.next_node = next_node
 
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    def add(self,data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    def size(self):
        obj = self.head
        k = 1
        if obj == None:
            print ("List is empty.")
            return 0
        while obj.next_node != None:
            k = k+1
            obj = obj.next_node
        return k
    def find(self,data):
        obj = self.head
        if obj == None:
            print("List is empty, no node values to find.")
        if obj.next_node == None and obj != None:
            if obj.data == data:
                return obj 
            else:
                obj = obj.next_node
        while obj.next_node != None:
            if obj.data == data:
                return obj 
            else:
                obj = obj.next_node
        print "Node with value",data,"is not in linked list"
        return None
    def remove(self,data):
        prev = None
        obj = self.head
        if obj == None:
            print("List is empty, no node values to remove.")
            return
        if obj.next_node == None and prev == None:
            if obj.data == data:
                self.head = obj.next_node
                print 'Value',data,'was removed from linked list'
                return 
        while obj.next_node != None:
            if obj.data == data:
                if prev != None:
                    prev.next_node = obj.next_node
                    print 'Value',data,'was removed from linked list'
                    return
                else:
                    self.head = obj.next_node 
                    print 'Value',data,'was removed from linked list'
                    return
            else:
                prev = obj
                obj = obj.next_node
                print 'looped'
        if obj.next_node == None:
            if obj.data == data:
                prev.next_node = obj.next_node
                print 'Value',data,'was removed from linked list'
                return
        print "Node with value",data,"is not in linked list, cannot remove."

         
   
LL = LinkedList()

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head
        next_node = current.next_node
        current.next_node = prev
        prev = current 
        while next_node != None:
            current = next_node
            next_node = current.next
            current.next = prev
            prev = current
        return prev

