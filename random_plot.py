import psutil as ps
from drawnow import *
import random
import time
import matplotlib.pyplot as plt


values = [] #empty list

t_list=[]
c_list=[]
m_list=[]


# get CPU_load
def cpu_load():
    p = ps.cpu_percent(interval=None, percpu=True)
    avg_load = sum(p)/len(p)
    #print(f'CPU Usage is {avg_load}%')
    return avg_load

# get Mem_load
def mem_load():
    return ps.virtual_memory()[2]

# to plot
def plot_me():

    plt.title('Python Code Club Mini-Taskmanager, \n by Saptarshi')
    
    plt.plot(t_list,m_list, 'go--', label='Memory Utilization' )
    plt.plot(t_list,c_list, 'r*:' , label='CPU Utilization')

    plt.grid('on')
    plt.xlabel='Time'
    plt.ylabel='CPU Usage'
    plt.legend()

# to loop forever 
def loop():

    # gloab variable access 
    global t_list
    global c_list
    global m_list
    
    start = time.time()
    for i in range(120):   # limit the loop for 30 iteration
        t = int(time.time() - start) 
        #r = random.randint(10, 100)  # gen a rand int from range [10,100]
        c = cpu_load()
        m = mem_load()
        print(f'at time \t {t} \t CPU is {c}% and memory is {m}% used...')

        t_list.append(t)
        c_list.append(c)
        m_list.append(m)
        
        time.sleep(int(random.randint(1,4)))

        drawnow(plot_me)   # overlap all the plots
        
       
def main():
    print('Program started...')
    loop()

main()
    
