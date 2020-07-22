# Heading
## Section 
### Sub-section
#### sub-sub section
this is a test

# Power using loop

this is a test sentance with a code-word `while` 


```python
result = 1 
a = 2
b = 11

i=0

print('result \t a \t b \t i \t Cond')
print('------ \t --- \t --- \t --- \t ----')

while i < b:
    print(f'{result} \t {a} \t {b} \t {i} \t {i < b}')
    result *= a
    i += 1

print(result) 
```

    result 	 a 	 b 	 i 	 Cond
    ------ 	 --- 	 --- 	 --- 	 ----
    1 	 2 	 11 	 0 	 True
    2 	 2 	 11 	 1 	 True
    4 	 2 	 11 	 2 	 True
    8 	 2 	 11 	 3 	 True
    16 	 2 	 11 	 4 	 True
    32 	 2 	 11 	 5 	 True
    64 	 2 	 11 	 6 	 True
    128 	 2 	 11 	 7 	 True
    256 	 2 	 11 	 8 	 True
    512 	 2 	 11 	 9 	 True
    1024 	 2 	 11 	 10 	 True
    2048
    


```python
pow(2,11)
```




    2048




```python
2 ** 11
```




    2048



# Product using Loop


```python
result = 0 
a = 20
b = 6

i=0

print('result \t a \t b \t i \t Cond')
print('------ \t --- \t --- \t --- \t ----')

while i < b:
    print(f'{result} \t {a} \t {b} \t {i} \t {i < b}')
    result += a
    i += 1
    
print(result)
```

    result 	 a 	 b 	 i 	 Cond
    ------ 	 --- 	 --- 	 --- 	 ----
    0 	 20 	 6 	 0 	 True
    20 	 20 	 6 	 1 	 True
    40 	 20 	 6 	 2 	 True
    60 	 20 	 6 	 3 	 True
    80 	 20 	 6 	 4 	 True
    100 	 20 	 6 	 5 	 True
    120
    

# Calculator function
this takes 3 inputs, `a,b,opt`.
* __`a`__:_first operand_ 
* __`b`__:_Second operand_
* __`opt`__: _the operation_
    1. __`add`__: _for addition_
    2. __`sub`__: _for subtraction_
    3. __`mul`__: _for multiplication_
    4. __`div`__: _for division_
    5. __`mod`__: _for remeinder_ 
    6. __`pwr`__: _for power_
    
this is a ___bold italic___ line


```python
def calculator(a, b, opt):
    '''
    this is a sample calculator function
    Inputs : a,b as numbers and opt as string 
        opt: possible values: 'add','sub','mul','div','mod'
    '''
    if (isinstance(a,int) or isinstance(a,float)) and (isinstance(b,int) or isinstance(b,float)):
        if opt == 'add':
            return a+b
        elif opt == 'sub':
            return a-b
        elif opt == 'mul':
            return a*b
        elif opt == 'div':
            return a/b
        elif opt == 'mod':
            return a%b
        elif opt == 'pwr':
            return a ** b
        else:
            print('Error : Unexpected Operator')
    else:
        print('Error : Unexpected Operands')

```


```python
calculator('5',6,'add')
```

    Error : Unexpected Operands
    


```python
calculator(5,6.5,'mul')
```




    32.5




```python
calculator('a',6,'add')
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-25-7d7be7389ba7> in <module>
    ----> 1 calculator('a',6,'add')
    

    <ipython-input-23-dd375db2a279> in calculator(a, b, opt)
          6     '''
          7     if opt == 'add':
    ----> 8         return a+b
          9     elif opt == 'sub':
         10         return a-b
    

    TypeError: can only concatenate str (not "int") to str


## Dynamic typed example


```python
a = 5
type(a)
```




    int




```python
a = 5.5
type(a)
```




    float




```python
a = '5.5'
type(a)
```




    str




```python
a = 5 
```


```python
isinstance(a,int)
```




    True




```python

```
