import pandas as pd
df = pd.read_csv(r"C:\Users\piyal\OneDrive\Desktop\Learning\Python\python_practice_room\questions\question_03\data.csv")
#print(df)
def check_palindrome(str1):
        str1=str(str1).lower().replace(" ", "")
        #print(str1)
        reversed_str1=str1[::-1]
        if str1==reversed_str1:
            return "True"
        else:
            return "False"


df['is_palindrome']=df["text"].apply(check_palindrome)
print(df)