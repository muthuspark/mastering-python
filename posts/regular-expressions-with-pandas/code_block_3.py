import pandas as pd
data = {'text': ['Start 123 End', 'Start 456 End', 'Ignore 789']}
df = pd.DataFrame(data)

#Extract numbers only if they are between 'Start' and 'End'
pattern = r'Start\s(\d+)\sEnd'
df['extracted_number'] = df['text'].str.extract(pattern, expand=False)
print(df)