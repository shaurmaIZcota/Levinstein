def levenstean(s1,s2):
    col_eror=0
    for i in range(0,len(s2)):
        if s2[i]!=s1[i]:
            col_eror+=1
    return col_eror

def levenstean_v2(s1,s2):
    col_opech=0
    if len(s2)>len(s1) or len(s2)<len(s1):
        col_opech+=1
    return col_opech
if __name__=='__main__':

    print(levenstean_v2('математик','математика'))


