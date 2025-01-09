#Example usage of memory_profiler (requires installation: pip install memory_profiler)
@profile
def my_memory_intensive_function():
    #Your code here
    large_list = [i for i in range(1000000)]
    #Do something with large_list

my_memory_intensive_function()