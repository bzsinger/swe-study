# Miscellaneous Topics

## UML Diagram
```
<----- (clear diamond)
<|----- (filled in diamond)

 _____             _____  
|     |           |     |
|  A  |   <|----- |  B  |     - B cannot exist on its own without A
|_____|           |_____|

 _____             _____  
|     |           |     |
|  A  |   <|----- |  B  |     - B can exist separately from A
|_____|           |_____|

 _____             _____  
|     |       *   |     |
|  A  |   <|----- |  B  |     - A has many Bs
|_____|           |_____|

 _____             _____  
|     |       1   |     |
|  A  |   <|----- |  B  |     - A has 1 Bs
|_____|           |_____|

```
