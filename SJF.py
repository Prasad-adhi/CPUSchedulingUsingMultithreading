import pygame
import tkinter as tk
def SJF(processes,n,bt)
   for i in range(0,len(bt)-1):  #applying bubble sort to sort process according to their burst time
      for j in range(0,len(bt)-i-1):
         if(bt[j]>bt[j+1]):
            temp=bt[j]
            bt[j]=bt[j+1]
            bt[j+1]=temp
            temp=processes[j]
            processes[j]=processes[j+1]
            processes[j+1]=temp
   wt=[]    #wt stands for waiting time
   avgwt=0  #average of waiting time
   tat=[]    #tat stands for turnaround time
   avgtat=0   #average of total turnaround time
   wt.insert(0,0)
   tat.insert(0,bt[0])
   pygame.init()
   screen = pygame.display.set_mode((350, 350))
   clock = pygame.time.Clock()
   screen.fill((255, 255, 255))
   done=False
   while not done:
        pygame.draw.rect(screen, (0, 128, 0), pygame.Rect(0, wt[0], (bt[0])*10,10))
        pygame.display.flip()
      for i in range(1,len(bt)):  
         wt.insert(i,wt[i-1]+bt[i-1])
         tat.insert(i,wt[i]+bt[i])
         avgwt+=wt[i]
         avgtat+=tat[i]
   avgwt=float(avgwt)/n
   avgtat=float(avgtat)/n
   print("\n")
   print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
   for i in range(0,n):
      print(str(processes[i])+"\t\t"+str(bt[i])+"\t\t"+str(wt[i])+"\t\t"+str(tat[i]))
   print("\n")
   print("Average Waiting time is: "+str(avgwt))
   print("Average Turn Arount Time is: "+str(avgtat))