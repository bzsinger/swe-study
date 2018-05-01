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
|     |     *  1  |     |
|  A  |   <|----- |  B  |     - A-B have many-1 relationship
|_____|           |_____|     -   (1 B is shared by many As)

 _____             _____  
|     |     1  *  |     |
|  A  |   <|----- |  B  |     - A-B have 1-many relationship
|_____|           |_____|     -   (1 A has many Bs)

```
