---
# optional when the title is not the file name
title: Profiling in Python
tags: Python, profiling, performance, cProfile, snakeviz
---

As we develop software, it is just a matter of time when we will encounter a programme that takes significantly longer time to complete than we would want.
This is where **profiling** comes in.

Profiling is a process where the time taken by each function call is measured.
With this result, we would be able to identify the bottleneck of the programme and make improvement to it if possible.
There 2 common types of profiling are:
1. statistical profiling, where the profiler will sample/collect call stack information at regular intervals, and 
2. instrumentation, in which the code will be altered (may be behind the scene) so that the profiling information can be collected.

Statistical profiling is the simpler approach as it requires no further intervention to the existing code.

For Python, statistical profiling can be done with [cProfile] module, which is included in the standard library.
This can be done in commandline interface with the following
```shell
python -m cProfile -o <profiling_output_filename>.pstats <python_script>.py
```
## Visualisation with Snakeviz (Web-based)
To look into the result, one may use the [pstats] module.
However, I personally prefer a graphical tool.
I have tried several of them, and my favourite is [snakeviz].
With the following command, 
```shell
snakeviz <profiling_output_filename>.pstats
```
the profiling result can be viewed interactively on web browser.

## Visualisation with gprof2dot (png)
A less interactive way (but can be included in reports) would be to export the result as an image.
This can be achieved with [gprof2dot] module, 
which converts the profiling output to the "dot" format (a common format for representing graph).
To do so, run the following command (if on Windows, use PowerShell 7):
```shell
gprof2dot.py -f pstats <profiling_output_filename>.pstats | dot -Tpng -o output.png
```

## Other Visualisation Tools that I have tried (but do not like)
- PyCharm built-in profiling. In my opinion, it is harder to navigate (e.g. isolate a single call and see its callees) as compared to snakeviz.
- line_profiler (with a submodule `kernprof`), no longer maintained. This would be a profiler with instrumentation where you could know exactly e.g. how often a function is called, how long does each line of code takes etc.
- pycallgraph, no longer maintained.


## Sources
- [Python official docs for cProfile][cProfile]
- [Python official docs for pstats][pstats]
- [GitHub page of snakeviz][snakeviz]
- [Github project page of gprof2dot][gprof2dot]

[cProfile]: https://docs.python.org/3/library/profile.html
[pstats]: https://docs.python.org/3/library/profile.html#module-pstats
[snakeviz]: https://jiffyclub.github.io/snakeviz/
[gprof2dot]: https://github.com/jrfonseca/gprof2dot
