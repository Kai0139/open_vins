from scipy.spatial.transform import Rotation as Rot
import numpy as np
from math import *

def transformation_matrix(q, t):
    """q = [qw, qx, qy, qz]
       t = [tx, ty, tz]
    """
    qw = q[0]
    qx = q[1]
    qy = q[2]
    qz = q[3]
    R0 = Rot.from_quat([qx, qy, qz, qw])

    eul = R0.as_euler('xyz')
    eul_deg = [degrees(i) for i in eul]
    print("euler angle: {}".format(eul_deg))

    tx = t[0]
    ty = t[1]
    tz = t[2]

    tm = np.array([
        [0, 0, 0, tx],
        [0, 0, 0, ty],
        [0, 0, 0, tz],
        [0, 0, 0,  1],
    ])

    rotm = np.concatenate((R0.as_matrix(), np.array([[0, 0, 0]])), axis=0)
    rotm = np.concatenate((rotm, np.array([[0, 0, 0, 0]]).T), axis=1)
    print(rotm)
    tf = rotm + tm
    return tf

q_cam0 = [0.500292, 0.490181, -0.508467, 0.500889]
t_cam0 = [0.067436, -0.022029, -0.078333]

transformation_cam0 = transformation_matrix(q_cam0, t_cam0)

q_cam1 = [0.494020, 0.500019, -0.504264, 0.501638]
t_cam1 = [-0.092345, -0.020508, -0.079230]

transformation_cam1 = transformation_matrix(q_cam1, t_cam1)

print("transformation matrix of cam0:\n{}".format(transformation_cam0))
print("inverse tf cam0:\n{}".format(np.linalg.inv(transformation_cam0)))
print("transformation matrix of cam1:\n{}".format(transformation_cam1))
print("inverse tf cam1:\n{}".format(np.linalg.inv(transformation_cam1)))
