def addTwoNumbers(self, l1, l2):
  """
  :type l1: ListNode
  :type l2: ListNode
  :rtype: ListNode
  """
  head = ListNode(l1.val + l2.val)
  if head.val > 9:
      carry = head.val/10
      head.val = head.val%10
  else: 
      carry = 0
  current = head
  l1 = l1.next
  l2 = l2.next
  
  while l1 and l2:
   node = ListNode(l1.val + l2.val + carry)
   if node.val > 9:
     carry = node.val/10
     node.val = node.val%10
   else: 
     carry = 0
   current.next = node
   current = node
   l1 = l1.next
   l2 = l2.next
  
  if l1 != None: ll = l1
  elif: l2 != None ll = l2
  
  if ll != None:
    while ll:
      node = ListNode(ll.val + carry)
      if node.val > 9:
        carry = node.val/10
        node.val = node.val%10
      else:
        carry = 0
      current.next = node
      current = node
      ll = ll.next
    
  if carry != 0:
    node = ListNode(carry)
    current.next = node
    current = node
          
  return head

