---
# optional when the title is not the file name
title: Gmsh for Mesh Generation
tags: comma, separated, tags
---

Gmsh as a mesh generation tool.
What I wanted is to generate a quad-dominant mesh with a given curve embedded.

However, quad-dominant mesh is not really an option.
Experimental quad mesh crashes every time.
Transfinite ignore my embedded curve.

More so is the output as `.msh` file, that does not seems to be accepted by FreeCAD.
The display in GUI is not really that nice for report stuff.


## Sources


[Gmsh .msh file doc]: https://gmsh.info/doc/texinfo/gmsh.html#MSH-file-format
[yt video transfinite (quad) mesh]: https://youtu.be/O1FyiBBuN98
[yt video embedding point]: https://youtu.be/kpWVNNHHdd8
