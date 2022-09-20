from src import melvec

if __name__ == "__main__":
    v3 = melvec.Vec3(10, 22, 3)
    v2 = melvec.Vec2(32, 44)

    for component in v3:
        print(component)

    for component in v2:
        print(component)

    print(melvec.Vec2.from_polar())