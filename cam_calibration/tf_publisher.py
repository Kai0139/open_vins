import rospy
import tf
import math

def quat_x(x):
    qw = math.cos(x/2.0)
    qx = math.sin(x/2.0)
    qy = 0.0
    qz = 0.0
    return [qw, qx, qy, qz]

def quat_y(y):
    qw = math.cos(y/2.0)
    qx = 0.0
    qy = math.sin(y/2.0)
    qz = 0.0
    return [qw, qx, qy, qz]

def quat_z(z):
    qw = math.cos(z/2.0)
    qx = 0.0
    qy = 0.0
    qz = math.sin(z/2.0)
    return [qw, qx, qy, qz]

def quat_mult(q, p):
    qw = q[0]
    qx = q[1]
    qy = q[2]
    qz = q[3]

    pw = p[0]
    px = p[1]
    py = p[2]
    pz = p[3]

    rw = qw*pw - qx*px - qy*py - qz*pz
    rx = pw*qx + px*qw + py*qz - pz*qy
    ry = pw*qy - px*qz + py*qw + pz*qx
    rz = pw*qz + px*qy - py*qx + pz*qw
    return [rw, rx, ry, rz]

def quat_xyz(x, y, z):
    quatx = quat_x(x)
    quaty = quat_y(y)
    quatz = quat_z(z)
    quatxyz = quat_mult(quatz, quat_mult(quaty, quatx))
    return quatxyz

def wxyz_to_xyzw(q):
    qw = q[0]
    qx = q[1]
    qy = q[2]
    qz = q[3]
    return [qx, qy, qz, qw]

if __name__ == "__main__":
    q_cam0_wxyz = (0.500292, 0.490181, -0.508467, 0.500889)
    q_cam0_xyzw = (0.490181, -0.508467, 0.500889, 0.500292)
    t_cam0 = (0.067436, -0.022029, -0.078333)

    q_cam1_wxyz = (0.494020, 0.500019, -0.504264, 0.501638)
    q_cam1_xyzw = (0.500019, -0.504264, 0.501638, 0.494020)
    t_cam1 = (-0.092345, -0.020508, -0.079230)
    
    quatx = quat_x(math.radians(90))
    q_cam0_wxyz_rot = quat_mult(quatx, q_cam0_wxyz)
    q_cam1_wxyz_rot = quat_mult(quatx, q_cam1_wxyz)

    q_cam0_xyzw_rot = wxyz_to_xyzw(q_cam0_wxyz_rot)
    q_cam1_xyzw_rot = wxyz_to_xyzw(q_cam1_wxyz_rot)

    fixed_frame_name = "global"

    rospy.init_node("tf_publisher")
    lr = rospy.Rate(10)
    br = tf.TransformBroadcaster()

    while not rospy.is_shutdown():
        br.sendTransform(t_cam0, tuple(q_cam0_xyzw), rospy.Time.now(), "cam0", fixed_frame_name)
        br.sendTransform(t_cam1, tuple(q_cam1_xyzw), rospy.Time.now(), "cam1", fixed_frame_name)
        lr.sleep()


