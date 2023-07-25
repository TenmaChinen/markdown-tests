import exercise_queries as eq
import textwrap, json, re

file = open('data.json','r', encoding='utf-8')
d_data = json.load(file)
file.close()

l_tables =d_data['tables']
l_fields =d_data['fields']
l_exercises = d_data['exercises']

pattern_keywords = '|'.join([f'({x})' for x in l_tables+l_fields])

markdown = ''

for d_exercise in l_exercises: 
    index = d_exercise['index']
    question_text = d_exercise['question_text']
    question_text = re.sub(pattern=f'{pattern_keywords}', repl= lambda x : f'<strong>{x.group(0)}</strong>', string=question_text)
    question_text = question_text.replace('\n', '<br><br>')
    answer_text = getattr(eq, f'get_exercise_{index}')()
    answer_text = textwrap.dedent(text=answer_text)
    answer_text = answer_text.strip()
    
    table_md = f'''
<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE {index}</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>{question_text}</td>
    <td><img src='images/sample_{index:02d}.png' alt='Image' style='flex: 1; max-width: 300px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```sql
{answer_text}
```

</details>
</td>
</tr>
</table>
'''

    markdown += textwrap.dedent(table_md)
    # markdown += ans_template

markdown = textwrap.dedent(markdown)

file = open('../README.md', 'w', encoding='utf-8')
file.write(markdown)
file.close()