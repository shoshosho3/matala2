def header():
  head="0xfee1900d"
  n_head=""
  for h in range(len(head)-1,1,-2):
    n_head+= "\\x"+head[h-1:h+1]
  return n_head

def this_length(num,current,word):
  if num!=current:
    section(word,num,current)
  else:
    print(word)

def section(word,num,current):
  for tag in range(0,3):
    in_section(word+"\\"+format(tag,"#04x"),num,current)

def in_section(he,num,current):
  for leng in range(0,3):
    word=he+"\\"+format(leng,"#04x")
    if leng==0:
      this_length(num,current+1,word)
    else:
      insec(leng,0,word,num,current)

def insec(num,current,word,num1,current1):
  if num!=current:
    for val in range(0,3):
      insec(num,current+1,word+"\\"+format(val,"#04x"),num1,current1)
  else:
    this_length(num1,current1+1,word)

for num in range(0,3):
  this_length(num,0,header()+"\\"+format(num,"#04x"))
