# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 15:50:17 2020

@author: carlo
"""

# Your implementation goes here
import networkx as nx
import matplotlib.pyplot as plt
class BinarySearchTree:
    # This is a Node class that is internal to the BinarySearchTree class
    class __Node:
        def __init__(self,val,left=None,right=None):
            self.val = val
            self.left = left
            self.right = right
            
        def getVal(self): 
            return self.val

        def setVal(self,newval): 
            self.val = newval
            
        def getLeft(self): 
            return self.left
        
        def getRight(self): 
            return self.right
        
        def setLeft(self,newleft): 
            self.left = newleft
        
        def setRight(self,newright): 
            self.right = newright
            
        def getMin(self):
            if self.left == None: return self
            else: return self.left.getMin()
            
        def getMax(self):
            if self.right == None: return self
            else: return self.right.getMax()
            
        def __repr__(self):
            return self.getVal()
            
        # This method deserves a little explanation. It does an inorder traversal
        # of the nodes of the tree yielding all the values. In this way, we get
        # the values in ascending order.
        
        def __iter__(self):
            if self.left != None:
                for elem in self.left: 
                    yield elem
            yield self.val
            if self.right != None:
                for elem in self.right:
                    yield elem
           
        
        
    # Below methods of the BinarySearchTree class.
    def __init__(self): 
        self.root = None
         
    def insert(self, val):
        # The __insert function is recursive and is not a passed a self parameter. It is a # static function (not a method of the class) but is hidden inside the insert
        # function so users of the class will not know it exists.
        
        if self.search(val) != None: return      #senza questo si può inserire due volte la stessa chiave  e crea danni 
        def __insert(root, val): 
            if root == None:
                return BinarySearchTree.__Node(val)
            if val < root.getVal(): 
                root.setLeft(__insert(root.getLeft(), val))
            else: 
                root.setRight(__insert(root.getRight(), val))
            return root
        self.root = __insert(self.root, val)
    
    
    # se non trova null ritorna None, altrimenti torna una lista di cui il nodo 0 è il nodo che si cerca,
        #e gli altri elemnti sono i nodi visitati per trovarlo, fino alla radice (la radice avrù dunque indice -1)
    def search(self, key): #
        def __search(root, key):
            if root.val == key: 
                research = []
                research.append(root)
                return research   
            if root.getVal() > key and root.left  != None: 
                research = __search(root.getLeft(), key)
                if research != None:
                    research.append(root)
                    return research
            if root.val < key and root.right != None:
                research = __search(root.getRight(), key)
                if research != None:
                    research.append(root)
                    return research   
            return None
        if self.root != None:
            return __search(self.root, key)
    
    
    def min(self):
        return self.root.getMin().getVal()
    
    def max(self):
        return self.root.getMax().getVal() #get max è definita sui noti e non come nested function, perche è richiamata anche da predecessor
            
        
    def predecessor(self, key):
        if key == self.min(): return None
        research = self.search(key)
        if research != None:
            root = research[0]
            if root.left != None: return root.left.getMax().getVal()
            else:
                for i, e in enumerate(research):
                    if research[-1].getVal()  != e.getVal():
                        if e.getVal() > research[i+1].getVal(): return research[i+1].getVal()   
                return research[-1].getVal()
                    
        
    def successor(self, key):
        if key == self.max(): return key
        research = self.search(key)
        if research != None:
            root = research[0]
            if root.right != None: return root.right.getMin().getVal()
            else:
                for i, e in enumerate(research):
                    if research[-1].getVal()  != e.getVal():
                        if e.getVal() < research[i+1].getVal(): return research[i+1].getVal()
                return research[-1].getVal()
        
  
    def delete(self,key):
        research = self.search(key)
        if research == None: return self #check if there is 'key' in the tree
        root = research[0]
        if root.getLeft() == None and root.getRight() == None:
            if len(research) <= 1: #controlla se è la radice 
                self.root = None
                return self
            if research[1].getRight() == root: research[1].setRight(None)
            else: research[1].setLeft(None)
            root = None
        elif root.getLeft() == None:
            if len(research) <=1: self.root = root.getRight()
            else:
                if research[1].getRight() == root: research[1].setRight(root.getRight())
                else: research[1].setLeft(root.getRight())
            root = None
        elif root.getRight() == None:
            if len(research) <=1: self.root = root.getLeft()
            else:
                if research[1].getRight() == root: research[1].setRight(root.getLeft())
                else: research[1].setLeft(root.getLeft())
            root = None 
        else:
            if self.successor(key) != None:
                newVal = self.successor(key)
            else :
                newVal = self.predecessor(key) #memorizza valore
            self = self.delete(newVal) #chiamata ricorsiva
            root.setVal(newVal)
        
        return self
    #L' ultimo caso fa la chiamata ricorsiva, 
    #si basa sul fatto che sarò chiamato un nodo con un solo figlio o nessuno ,
    #avremo dunque al massimo una sola chiamata ricorsiva poiche
    #il predecessore)o o successore sono un minimo od un massimo
      
        
    def __repr__(self):
        if self.root == None : return 'The tree is empty'
        n = len([i for i in self.root]) #numero nodi 
        depht= 0 ##livello nell' albero 
        breath =2* 2**n  #per la x 
        x = breath
        y = n
        G = nx.DiGraph()
        colors = []
        nodes = []
        edges = []
        positions = {} #is a dict of tuples 
        def __repr(root, color, x, y, breath, depht ):
            if root.getLeft() == None and root.getRight() == None: color = 'lightgreen'
            colors.append(color)
            G.add_node(root.getVal())
            positions[root.getVal()] = (x,y)
            color = 'lightblue'
            if root.getLeft() != None:
                __repr(root.getLeft(), color, x - breath/(2**(depht + 1)), y - 1, breath, depht + 1)
                G.add_edge(root.getVal(), root.getLeft().getVal())
            if root.getRight() != None:
                __repr(root.getRight(), color, x + breath/(2**(depht + 1)), y - 1, breath, depht + 1)
                G.add_edge(root.getVal(), root.getRight().getVal())        
        
        __repr(self.root,'pink',  x, y, breath, depht)
       
        nx.draw(G, with_labels=True, node_color = colors, node_size = 700, pos = positions)  
        plt.show()
        return '' #devo ritornare una stringa per forza col repr 