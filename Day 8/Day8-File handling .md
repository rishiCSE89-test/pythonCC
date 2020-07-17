# Creating a file 
when you open a file in write or append mode it creates the file 
if it doesn't exist.


```python
fp1=open(file='myfile.txt',mode='w')
fp1.close()
```

# Openning the file in Read mode


```python
fp_1 = open(file='myfile.txt')
```


```python
# what is in the file pointer
print(fp_1)
```

    <_io.TextIOWrapper name='myfile.txt' mode='r' encoding='cp1252'>
    


```python
# whats in the file
x = fp_1.read()
```


```python
fp_1.close()
```


```python
x
```




    'this is a file\nthis is a new line\nthis is another line\nthis is where the file ends'




```python
print(x)
```

    this is a file
    this is a new line
    this is another line
    this is where the file ends
    


```python
line_num = 1

fp_1 = open('myfile.txt')
print( fp_1.readlines()[line_num] )
fp_1.close()
```

    this is a new line
    
    

# Write into a file

## create a file in write mode


```python
fp_data = open(file='database.txt',mode='w')

fp_data.write('this is a test \nI finish here ')

fp_data.close()
```

## Read the content


```python
fp_data = open(file='database.txt', mode='r')

for line in fp_data.readlines():  # reading from the list of lines 
    print(line)

fp_data.close()
```

    this is a test 
    
    I finish here 
    

## Append two more lines


```python
fp_data = open(file='database.txt',mode='a')

fp_data.write('\nthis is a test again \nI finish here ')

fp_data.close()
```

## Read again


```python
fp_data = open(file='database.txt', mode='r')

for line in fp_data.readlines():
    print(line)

fp_data.close()
```

    this is a test 
    
    I finish here 
    
    this is a test again 
    
    I finish here 
    

# Context Manager 


```python
student_list = [
    {'id': 'stu1' , 'name':'abc' , 'marks': 85 , 'age': 14},
    {'id': 'stu2' , 'name':'pqr' , 'marks': 56 , 'age': 18},
    {'id': 'stu3' , 'name':'xyz' , 'marks': 96 , 'age': 17},
    {'id': 'stu4' , 'name':'mno' , 'marks': 45 , 'age': 18}
]
```


```python
student_list
```




    [{'id': 'stu1', 'name': 'abc', 'marks': 85, 'age': 14},
     {'id': 'stu2', 'name': 'pqr', 'marks': 56, 'age': 18},
     {'id': 'stu3', 'name': 'xyz', 'marks': 96, 'age': 17},
     {'id': 'stu4', 'name': 'mno', 'marks': 45, 'age': 18}]




```python
len(student_list)
```




    4




```python
with open(file='stu_database.csv',mode='w') as fp1:
    fp1.write('id,name,marks,age')
    for rec in student_list:
        fp1.write('\n')
        fp1.write(f'{rec["id"]},{rec["name"]},{rec["marks"]},{rec["age"]}')    
```


```python
import pandas as pd 
```


```python
x = pd.read_csv('stu_database.csv')
x
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>marks</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>stu1</td>
      <td>abc</td>
      <td>85</td>
      <td>14</td>
    </tr>
    <tr>
      <th>1</th>
      <td>stu2</td>
      <td>pqr</td>
      <td>56</td>
      <td>18</td>
    </tr>
    <tr>
      <th>2</th>
      <td>stu3</td>
      <td>xyz</td>
      <td>96</td>
      <td>17</td>
    </tr>
    <tr>
      <th>3</th>
      <td>stu4</td>
      <td>mno</td>
      <td>45</td>
      <td>18</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
