import numpy as np
import numpy.linalg as npla


def interpolate3d(p1, p2, p3, p4, point, v1, v2, v3, v4):
    J = np.array([[p2[0]-p1[0], p3[0]-p1[0], p4[0]-p1[0]],
                  [p2[1]-p1[1], p3[1]-p1[1], p4[1]-p1[1]],
                  [p2[2]-p1[2], p3[2]-p1[2], p4[2]-p1[2]]])
    J = npla.inv(J)

    # ref1 = J.dot(np.array([ p1[0]-p1[0], p1[1]-p1[1], p1[2]-p1[2] ]))
    # ref2 = J.dot(np.array([ p2[0]-p1[0], p2[1]-p1[1], p2[2]-p1[2] ]))
    # ref3 = J.dot(np.array([ p3[0]-p1[0], p3[1]-p1[1], p3[2]-p1[2] ]))
    # ref4 = J.dot(np.array([ p4[0]-p1[0], p4[1]-p1[1], p4[2]-p1[2] ]))
    ref_point = J.dot(np.array([ point[0]-p1[0], point[1]-p1[1], point[2]-p1[2] ]))

    tot_vol = 1./6  # Volume of trirectangular tetrahedron
    # Volume of tetrahedron = 1/3 * base_area * height
    vol2 = (1./3)*(1./2)*ref_point[0]
    vol3 = (1./3)*(1./2)*ref_point[1]
    vol4 = (1./3)*(1./2)*ref_point[2]
    vol1 = tot_vol - vol2 - vol3 - vol4

    lam1 = vol1/tot_vol
    lam2 = vol2/tot_vol
    lam3 = vol3/tot_vol
    lam4 = vol4/tot_vol

    if (0<lam1<1 and 0<lam2<1 and 0<lam3<1 and 0<lam4<1):
        v_point = v1*(vol1/tot_vol) + v2*(vol2/tot_vol) + v3*(vol3/tot_vol) + v4*(vol4/tot_vol)
        return v_point
    else:
        return None


def interpolate2d(p1, p2, p3, point, v1, v2, v3):
    trans = np.array([[ p2[0]-p1[0], p3[0]-p1[0] ],
                      [ p2[1]-p1[1], p3[1]-p1[1] ]])
    trans = npla.inv(trans)

    # ref1 = trans.dot(np.array([ p1[0]-p1[0], p1[1]-p1[1] ]))
    # ref2 = trans.dot(np.array([ p2[0]-p1[0], p2[1]-p1[1] ]))
    # ref3 = trans.dot(np.array([ p3[0]-p1[0], p3[1]-p1[1] ]))
    ref_point = trans.dot(np.array([ point[0]-p1[0], point[1]-p1[1] ]))

    tot_area = 0.5  # Area of 45-45-90 triangle, side length=1
    area2 = 0.5*1*ref_point[0]
    area3 = 0.5*1*ref_point[1]
    area1 = tot_area - area2 - area3

    lam1 = area1/tot_area
    lam2 = area2/tot_area
    lam3 = area3/tot_area

    if (0<lam1<1 and 0<lam2<1 and 0<lam3<1):
        v_point = v1*lam1 + v2*lam2 + v3*lam3
        return v_point
    else:
        return None
