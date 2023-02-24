def reverse_text(text: str):
   index = 0

   while index < len(text):
       yield text[::-1][index]
       index += 1
