def jumpingOnClouds(c):
    if len(c) <= 1:
        return 1
    if len(c) == 2:
        return 2

    single_jump_path = 9999999999999
    double_jump_path = 9999999999999

    if c[1] == 0:
        single_jump_path = 1+jumpingOnClouds(c[1:])
    
    if c[2] == 0:
        double_jump_path = 1+jumpingOnClouds(c[2:])

    if (single_jump_path < double_jump_path):
        return single_jump_path
    
    return double_jump_path

res = jumpingOnClouds([0,0,0,0,1,0])
print(res)