
# Sage2tikz

This little SAGE/Python script takes input like this:

    P=implicit_plot3d(x**2-y**4*z**3==0,(x,-2,2), (y,-2,2),(z,-2,2), plot_points=75)
    P.triangulate()
    Picture(P.face_list(), boxed=True, axes=False,).render()


and returns a standalone Latex+tikz file, which when compiled (takes a couple of minutes) produces a 3d graphics.


The script reads standard input (so you can call it from the editor) or a file (when used with `--file` command line option) and writes to standard output.

The example below was produced saving the above code as `test.py`, and running
    
    ./texrender3d --file test.py  > result.tex
    lualatex result.tex # takes a couple of minutes

![Result.Pdf](result.pdf.png)

See `result.pdf` for an example.

# Todo

Explain how you can integrate nodes, arrows, etc in the `tikz` code.





# License

