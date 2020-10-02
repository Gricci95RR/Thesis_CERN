import pandas as pd

gabriella2018 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Dataset/2018_dataset_Gabriella_PROTON.csv').drop('Unnamed: 0', axis=1)
gianmarco2018 = pd.read_csv('/Users/gianmarcoricci/Documents/GitHub/Thesis_CERN/Dataset/2018_dataset_GR_PROTON.csv').drop('Unnamed: 0', axis=1)

diff_decay_a = []  # gabriella2018: col n 1 / gianmarco2018: col n 5
diff_decay_b = []  # ga: col n 2 / gr: col n 6
diff_decay_c = []  # ga: col n 3 / gr: col n 7
diff_height = []   # ga: col n 5 / gr: col n 2 
diff_position = [] # ga: col n 7 / gr: col n 3
name = []

for i in gabriella2018.index:
    nome1 = gabriella2018.iat[i,0].split('_')
    for j in gianmarco2018.index:
        nome2 = gianmarco2018.iat[j,0].split('_')
        if nome1[0] == nome2[0] and nome1[1] == nome2[1]:
            name.append(nome1[0]+nome1[1])
            diff_decay_a_ = gabriella2018.iat[i,1] - gianmarco2018.iat[j,5]
            diff_decay_b_ = gabriella2018.iat[i,2] - gianmarco2018.iat[j,6]
            diff_decay_c_ = gabriella2018.iat[i,3] - gianmarco2018.iat[j,7]
            diff_height_ = gabriella2018.iat[i,5] - gianmarco2018.iat[j,2]
            diff_position_ = gabriella2018.iat[i,7] - gianmarco2018.iat[j,3]
            diff_decay_a.append(diff_decay_a_)
            diff_decay_b.append(diff_decay_b_)
            diff_decay_c.append(diff_decay_c_)
            diff_height.append(diff_height_)
            diff_position.append(diff_position_)
            
            print('i:             ', i)
            print('nome1[0]:      ', nome1[0])
            print('nome2[0]:      ', nome2[0])
            print('nome1[1]:      ', nome1[1])
            print('nome2[1]:      ', nome2[1])
            print('diff_decay_a:  ', diff_decay_a_)
            print('diff_decay_b:  ', diff_decay_b_)
            print('diff_decay_c:  ', diff_decay_c_)
            print('diff_height:   ', diff_height_)
            print('diff_position_:', diff_position_)
            print('***')
        
data = {
        'name': name,
        'diff_height': diff_height,
        'diff_decay_a': diff_decay_a,
        'diff_decay_a': diff_decay_b,
        'diff_decay_c': diff_decay_c,
        'diff_position': diff_position
        }
df2 = pd.DataFrame (data) 
print(df2)

df2.to_csv('differences2018.csv')
        