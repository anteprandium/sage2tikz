P=implicit_plot3d(x**2-y**4*z**3==0,(x,-2,2), (y,-2,2),(z,-2,2), plot_points=75)
P.triangulate()
Picture(P.face_list(), boxed=True, axes=False,).render()
