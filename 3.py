def surf_vol(radius):
    s = 4*3.14*radius*radius
    v = 4/3*3.14*radius**3
    print("Surface area of the sphere:",s)
    print("Volume of the sphere:",v)
    

r=float(input("Enter the radius:"))
surf_vol(r)
