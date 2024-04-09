# SimpleSpinner
A simple python class to make a loading spinner


# Usage Example
```python
def task_that_takes_a_long_time() -> None:
    time.sleep(5)

spinner: Spinner = Spinner()
print("[+] Starting long task.")
spinner.Start()  # This will make a spinner appear in the console
task_that_takes_a_long_time()
spinner.Stop()
print("[+] Long task done.")
```
```
> [+] Starting long task.
> Loading [/]
```
```
> [+] Long task done.
```

It really is that simple

The loading text removes itself after its done.

## Optional Arguments
The Spinner class comes with two optional arguments.
```python
spinner: Spinner = Spinner("Real", 0.5)
```
```
> Real [/]
```
The first argument is the text which has the spinner text to it. 

The second argument is the amount of time between each character cycling, "Rotation Speed".
