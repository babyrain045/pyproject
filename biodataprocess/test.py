
import pandas as pd

a = {'A': 12, 'C': 4, 'T': 23, 'G': 19,"a":14,'t':16,"c":89,'g':57}
pre_a = list(a.items())

df = pd.DataFrame(pre_a,columns=['id','numbers']).set_index('id')
new_df = df.sort_values(by = 'numbers',ascending=False)
new_df = new_df.to_dict()['numbers']
print(new_df)








