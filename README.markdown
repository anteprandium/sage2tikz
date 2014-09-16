
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

See [`result.pdf`](result.pdf) for the full resolution (prettier) output.

# Example: integration with tikz

## Annotations

Python:

    P=implicit_plot3d( x**3+y**2-z**2 ==0,(x,-2,2), (y,-2,2),(z,-2,2), plot_points=100)
    P.triangulate()
    Picture(P.face_list(), boxed=False, axes=True,
        nodes=[{"Position": (0,0,0), "Text": "" , "Options": "circle, inner sep=4pt,black!80, pin={[pin edge={black!80, semithick}]-120:Singular point}, draw"}]
    ).render()

Result:

![Result Contour.Pdf](examples/result_contour.pdf.png)


## Pseudosphere

Python: 

    a=1
    P=parametric_plot3d([a*sech(u)*cos(v), a*sech(u)*sin(v),a*(u-tanh(u))],(u,-3.5,3.5), (v,0,2*pi), plot_points=80)
    P.triangulate()
    Picture(P.face_list(), boxed=False, axes=False,
        nodes=[{"Position": (0,0,2.501), "Text": "$\\uparrow$\\rlap{ to infinity}", "Options": "anchor=south"},
        {"Position": (0,0,-2.501), "Text": "$\\downarrow$\\rlap{ to infinity}", "Options": "anchor=north"},
        ]
    ).ren
    
Result:

![Result Contour.Pdf](examples/result_pseudo.pdf.png)

See the Examples folder.



# License

MIT.