import os, json, re

file = open('data.json','r', encoding='utf-8')
d_data = json.load(file)
file.close()

l_tables =d_data['tables']
l_fields =d_data['fields']
l_exercises =d_data['exercises']

# matching_words = '|'.join([f'({x})' for x in l_tables+l_fields])

# for exercise in l_exercises:
#     question_text = exercise['question_text']
#     question_text = re.sub(pattern=r"([a-z])([A-Z0-9])", repl=lambda x : f'{x.group(1)}_{x.group(2).lower()}', string=question_text)
#     question_text = re.sub(pattern=f"\b{matching_words}\b", repl=lambda x : f'{x.group(0).lower()}', string=question_text, flags=re.IGNORECASE)
#     exercise['question_text'] = question_text

# file = open('data.json','w', encoding='utf-8')
# d_data = json.dump(d_data, file, indent=2)
# file.close()

offset = 40
for idx, exercise in enumerate(l_exercises[offset-1:]):
    query = exercise['answer_text']
    query = query.replace('"','\\"')
    query = query.replace('\n',' ')
    print('\n idx : ',(offset+idx))
    log = os.system(f'set "PGPASSWORD=IlovePostgreSQL" && psql -U postgres -d \"classic_models\" -c "{query} --quiet"')
    if log == 1:
        print(f'\n{query}\n')
        break
