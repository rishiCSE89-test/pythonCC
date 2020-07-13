# Lab1
Write a funtion that counts th enumber of even numbers in a list


```python
l = [10,4,2,31,45,8,77,90]
```


```python
l
```




    [10, 4, 2, 31, 45, 8, 77, 90]




```python
x= 20
```


```python
20/3   #Quo
```




    6.666666666666667




```python
20%3   #Rem
```




    2




```python
15%2
```




    1




```python
17%2
```




    1




```python
18%2
```




    0




```python
l
```




    [10, 4, 2, 31, 45, 8, 77, 90]




```python
for i in l:
    print(f'rem of \t {i} \t is \t {i%2}')
```

    rem of 	 10 	 is 	 0
    rem of 	 4 	 is 	 0
    rem of 	 2 	 is 	 0
    rem of 	 31 	 is 	 1
    rem of 	 45 	 is 	 1
    rem of 	 8 	 is 	 0
    rem of 	 77 	 is 	 1
    rem of 	 90 	 is 	 0


# Print formatting


```python
name = 'abcd'
marks = 50

print(f'{name} scored {marks}')
```

    abcd scored 50


## `\n`


```python
print('this is a line,\nthis is a new line ')
```

    this is a line,
    this is a new line 


## `\t`


```python
print('this is a field \t this is a new field ')
```

    this is a field 	 this is a new field 


# Write a function


```python
def count_even(input_list):
    count = 0            # init counter with 0
    
    for i in input_list: # for all items in input_list
        if i%2 == 0:     # if item is even
            count += 1   # incr count
    
    return count
```


```python
l.append(100)   # invoking a method 'append' from list object 'l'
```


```python
l
```




    [10, 4, 2, 31, 45, 8, 77, 90, 100]




```python
c = count_even(input_list=l)  # calling a function 'count_even' with an input 'l' 
print(c)
```

    6


# Home task
Write a funtion that takes name and age as input and classify canditates if they are 
1. Minor  [<18]
2. Adult  [18 - 59]
3. Old    [>60]


```python

```
