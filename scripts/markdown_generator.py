import json, re, textwrap

file = open('exercise_queries.py', 'r')
text = file.read()
file.close()


file = open('data.json', 'r')
d_data = json.load(file)
file.close()

l_exercises = d_data['exercises']

pattern = r'(def get_exercise_[0-9]{1,2}\(\)\:)(((?!return).)*)'
l_matches = re.findall(pattern=pattern, string=text, flags=re.DOTALL)
l_answers = [ textwrap.dedent(x[1]).strip() for x in l_matches ]

markdown = ''

for d_exercise, answer_text in zip(l_exercises,l_answers):
    index = d_exercise['index'] 
    question_text = d_exercise['question_text']

    markdown += f'''
<table border=1 width=100%>
<tr>
    <th align="left">EXERCISE {index}</th>
    <th align="center">OUTPUT</th>
</tr>
<tr>
    <td>{question_text}</td>
    <td><img src='images/sample_{index:02d}.png' alt='Image' style='flex: 1; max-width: 300px; min-height:100px; max-height: 200px;'></td>
</tr>
<tr>
<td colspan=2>
<details>
<summary>Click here to see the answer</summary>

```py
{answer_text}
```
</details>
</td>
</tr>
</table>
    '''

file = open('../README.md', 'w')
file.write(markdown)
file.close()