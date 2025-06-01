# Adapted from vpython documentation's recommended module for STL model imports.
# See their FAQ linking it here:
# https://vpython.org/presentation2018/FAQ.html
def stl_to_triangles(filename):
    # Accept a file name or a file descriptor; make sure mode is 'rb' (read binary)
    fd = open(filename, mode='rb')
    tris = []  # Compound later

    fd.seek(0)
    f_list = fd.readlines()

    # Decompose list into vertex positions and normals
    vs = []
    n = None
    for line in f_list:
        file_line = line.split()
        if file_line[0] == b'facet':
            n = [float(file_line[2]), float(file_line[3]), float(file_line[4])]
        elif file_line[0] == b'vertex':
            vs.append([float(file_line[1]), float(file_line[2]), float(file_line[3]), n])
            if len(vs) == 3:
                tris.append(vs)
                vs = []

    return tris


# Adapted from vpython documentation's recommended module for STL model imports.
# See their FAQ linking it here:
# https://vpython.org/presentation2018/FAQ.html
def triangle_mesh(data):
    tris = []
    for i in data:
        vs = []
        for j in i:
            n = vec(j[3][0], j[3][1], j[3][2])
            vs.append(vertex(pos=vec(j[0], j[1], j[2]), normal=n))
        tris.append(triangle(vs=vs))

    return compound(tris)


if __name__ == '__main__':
    sample = stl_to_triangles('STLbot.stl')
    print(sample)