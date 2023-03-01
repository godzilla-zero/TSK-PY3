class Node( object ) :
  def __init__( self, cargo = None, next = None ) :
      self.cargo = cargo
      self.next = next

class Queue :


  def __init__( self ) :
      self.length = 0
      self.head = None
      self.last = None


  def isEmpty( self ) :
     return (self.length == 0)



 def __len__( self ) :
      return len(self.length)

  def enqueue( self, item, priority) :
      newNode = Node (cargo)
      newNode.next = None
      if self.length == 0:
          self.head.self.last = newNode
      newNode.next = self.head
      self.head = newNode
      self.last.next = newNode
      self.last = newNode

      temp = self.head
      p = self.head.next
      while p != None :
          if p.cargo > newNode.cargo:
             temp = temp.next
             p = p.next
          break
      newNode.next = temp.next
      temp.next = newNode


  def dequeue( self ) :
      cargo = self.head.cargo
      self.head = self.head.next
      self.length = self.length - 1
      if self.length == 0:
          self.last = None
      return cargo

      def peek( self ) :
      if not self.empty():
          return self.head.cargo
      else:
          return None