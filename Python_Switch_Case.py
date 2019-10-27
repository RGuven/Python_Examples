print({
    0:lambda x,y:x+y,
    1:lambda x,y:x*y,
    2:lambda x,y:x-y}.get(1,False)(2,3))
#output:6
