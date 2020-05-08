def nestedListContains(NL, target):
   result = False
   if NL == target:
      result = True
   if isinstance(NL, list):
      for i in NL:
         if result == True:
            break
         else:
            result = nestedListContains(i, target)
   return result