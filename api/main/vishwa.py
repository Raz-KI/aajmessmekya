
# for i in range(len(text)):
    # # print(text[i])
    # x=text[i][::-1]
    # y=pat[i][::-1] 
    # try:
    #     for j in range(len(text[i])):
            
    #         if(pat[i][j]!='*'):
    #             if(text[i][j]!=pat[i][j]):
    #                 print(ans)
    #                 ans="no"
    # except(IndexError):
    #     pass              


    # for
    #             break
    # for v in range(len(text[i])):
    #     print(i,v)
    #     # if(y[i][v]!='*'):
    #     #     if(x[i][v]!=y[i][v]):
    #     #         ans="no"
    
# print(ans)
        
        # print(text[i][j])
        #       pat[i][j]
        

text=["aba"]
pat=["ab*ba"]

for i in range(len(pat)):
    # print(i)
    for j in range(len(pat[i])):
        # print(i[j])
        if pat[i][j]=="*":
            ind=j
    pre=pat[i][:ind]
    suf=pat[i][ind+1:]
    print(pre,suf)
    print(text[i][:ind],text[i][-1:-(len(suf)+1):-1][::-1])
    print(len(suf))
    if pre==text[i][:ind] and suf==text[i][-1:-(len(suf)+1):-1][::-1]:
        print('yes')
    else:
        print("no")   

