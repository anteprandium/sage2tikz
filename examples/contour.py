P=implicit_plot3d( x**3+y**2-z**2 ==0,(x,-2,2), (y,-2,2),(z,-2,2), plot_points=100)
P.triangulate()
Picture(P.face_list(), boxed=False, axes=True,
    nodes=[{"Position": (0,0,0), "Text": "" , "Options": "circle, inner sep=4pt,black!80, pin={[pin edge={black!80, semithick}]-120:Singular point}, draw"}]
).render()