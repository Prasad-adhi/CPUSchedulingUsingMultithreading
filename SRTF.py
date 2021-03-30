import pygame
import tkinter as tk
# Function to find the waiting time 
# for all processes 
def findWaitingTime(processes, n, wt): 
    rt = [0] * n
    pygame.init()
    screen = pygame.display.set_mode((350, 350))
    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))
    # Copy the burst time into rt[] 
    for i in range(n): 
        rt[i] = processes[i][1]
    complete = 0
    t = 0
    minm = 999999999
    short = 0
    check = False
    done=False
    i=0
    k=0
    order=[]
    order.append(0)
    # Process until all processes gets 
    # completed 
    while not done:
        pygame.event.get()
        while (complete != n):
            
            # Find process with minimum remaining 
            # time among the processes that 
            # arrives till the current time`
            for j in range(n):
                if ((processes[j][2] <= t) and 
                    (rt[j] < minm) and rt[j] > 0):
                    minm = rt[j]
                    short = j
                    check = True
            if (check == False):
                t += 1
                continue
                
            # Reduce remaining time by one 
            rt[short] -= 1
            order.append(short)
            if(order[-2]==short):
                pygame.draw.rect(screen, (0, 50*short, 50), pygame.Rect(k*10,i*10, 10,10))
                pygame.time.delay(500)
                pygame.display.flip()
                k+=1
            else:
                i+=1
                pygame.draw.rect(screen, (0, 50*short, 50), pygame.Rect(k*10,i*10, 10,10))
                pygame.time.delay(500)
                pygame.display.flip()
                k+=1

            # Update minimum 
            minm = rt[short] 
            if (minm == 0): 
                minm = 999999999

            # If a process gets completely 
            # executed 
            if (rt[short] == 0): 

                # Increment complete 
                complete += 1
                check = False

                # Find finish time of current 
                # process 
                fint = t + 1

                # Calculate waiting time 
                wt[short] = (fint - proc[short][1] -    
                                    proc[short][2])

                if (wt[short] < 0):
                    wt[short] = 0
            
            # Increment time 
            t += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
  
# Function to calculate turn around time 
def findTurnAroundTime(processes, n, wt, tat): 
      
    # Calculating turnaround time 
    for i in range(n):
        tat[i] = processes[i][1] + wt[i] 
  
# Function to calculate average waiting 
# and turn-around times. 
def findavgTime(processes, n): 
    wt = [0] * n
    tat = [0] * n 
  
    # Function to find waiting time 
    # of all processes 
    findWaitingTime(processes, n, wt) 
  
    # Function to find turn around time
    # for all processes 
    findTurnAroundTime(processes, n, wt, tat) 
    '''
    # Display processes along with all details 
    print("Processes    Burst Time     Waiting", 
                    "Time     Turn-Around Time")
    total_wt = 0
    total_tat = 0
    for i in range(n):
  
        total_wt = total_wt + wt[i] 
        total_tat = total_tat + tat[i] 
        print(" ", processes[i][0], "\t\t", 
                   processes[i][1], "\t\t", 
                   wt[i], "\t\t", tat[i])
  
    print("\nAverage waiting time = %.5f "%(total_wt /n) )
    print("Average turn around time = ", total_tat / n) 
    '''
    total_wt = 0
    total_tat = 0
    root=tk.Tk()
    string="Processes Burst time " + " Waiting time " + " Turn around time"
    tk.Label(root, text=string).pack()
    for i in range(n):
        string=""
        # Calculate total waiting time and total turn around time
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        string+=str(processes[i][0])+"\t"+str(processes[i][1])+"\t"+str(wt[i])+"\t\t"+str(tat[i])
        tk.Label(root,text=string).pack()
    
    tk.Label(root,text="Average waiting time = "+str(total_wt / n)).pack()
    tk.Label(root,text="Average turn around time = "+str(total_tat / n)).pack()
    root.mainloop()
      
# Driver code 
if __name__ =="__main__":
      
    # Process id's 
    proc = [[1, 8, 0], 
            [2, 4, 1],
            [3, 2, 2], 
            [4, 1, 3]]
    n = 4
    findavgTime(proc, n)
      
# This code is contributed
# Shubham Singh(SHUBHAMSINGH10)