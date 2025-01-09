import pandas as pd


df.to_json('exported_data.json', orient='records')

#Other Orient options include 'split', 'index', 'columns', 'values'  Experiment to find the best format for your needs.