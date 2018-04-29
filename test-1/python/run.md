# Running Python scripts

## Method 1 - Directly
```bash
$ python3 <filename>.py
```

## Method 2 - Executable
To use this method, add the line below to the top of your Python file.
```python
#!/usr/bin/env/python3
```
This line indicates where the OS can find the python3 executable. It's commented out because it's for the OS to read, not Python.

```bash
chmod ugo+x <filename>.py
```
```u``` - user, the current user's permissions

```g``` - group, the current user's group's permissions

```o``` - other users' permissions

```+x``` - make the file executable

```bash
./<filename>.py
```

## Method 3 - Interactively
```bash
python3
>>> import <filename>
```
**Note:** Don't include ```.py```

### Recap
Python scripts have
- definitions
- code

When directly executing a script or importing it interactively, need:
- definitions
- code

When importing a script from another script, need:
- definitions
