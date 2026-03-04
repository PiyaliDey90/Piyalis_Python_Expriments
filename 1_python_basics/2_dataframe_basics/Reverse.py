
import pandas as pd
df = pd.read_csv(r"C:\Users\piyal\OneDrive\Desktop\Learning\Python\python_practice_room\questions\question_05\data.csv")
print(df)
def rev(sentence):
    #sentence = sentence[::-1]
    list1= sentence.split()
    list2= []
    for i in list1:
        list2.append(i[::-1])
    return  " ".join(list2)


df["rev_Sentace"]=df.sentence.apply(rev)
print(df)