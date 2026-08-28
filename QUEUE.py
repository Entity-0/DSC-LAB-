def enque(queue,front,rear):
    print("Enter the element you want to enque : ")
    t= int(input(""))
    queue[rear]=t
    rear+=1
    return RuntimeWarning

def deque(queue,front,rear):
    print("Element being removed is : ",queue[front])
    queue[front]=0
    front+=1
    return front


queue=[0]*100
f=0
r=0

r=enque(queue,f,r)

print("The queue now:")

for i in range(f,r):
    print(queue[i])

