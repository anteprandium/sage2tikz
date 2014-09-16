a=1
P=parametric_plot3d([a*sech(u)*cos(v), a*sech(u)*sin(v),a*(u-tanh(u))],(u,-3.5,3.5), (v,0,2*pi), plot_points=80)
P.triangulate()
Picture(P.face_list(), boxed=False, axes=False,
    nodes=[{"Position": (0,0,2.501), "Text": "$\\uparrow$\\rlap{ to infinity}", "Options": "anchor=south"},
    {"Position": (0,0,-2.501), "Text": "$\\downarrow$\\rlap{ to infinity}", "Options": "anchor=north"},
    ]
).render()