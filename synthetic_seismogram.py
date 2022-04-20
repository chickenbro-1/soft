import json
from PyQt5.QtWidgets import *
import matplotlib
from matplotlib.patches import PathPatch
from matplotlib.path import Path
import matplotlib.pyplot as plt
matplotlib.use("Qt5Agg")

import cv2
import numpy as np
np.seterr(divide='ignore',invalid='ignore')

from decimal import *
from scipy.signal import convolve
import math





class synthetic_seismogram(QMainWindow):
    def __init__(self):
        self.pro()
    def Rickwave(self):
        self.D =[]
        with open("project.json","r") as fr:
            f_ = json.load(fr)
            self.dt = float(f_["sampling_rate"])
            self.fmax = float(f_["Dominant_frequency"])
            self.t = float(f_["sampling_time"])
            R = f_["xishu"]
        for i in list(R):
            self.D.append(float(i))
        t = self.t
        dt = self.dt
        fmax = self.fmax
        def floatrange(start, stop, steps):
            resultList = []
            while Decimal(str(start)) <= Decimal(str(stop)):
                resultList.append(float(Decimal(str(start))))
                start = Decimal(str(start)) + Decimal(str(steps))
            return resultList
        t_list = floatrange(-t, t, dt)
        Rickwave_list = []
        for t_list_i in t_list:
            value1 = (Decimal(str(Decimal(str(math.pi)) * Decimal(str(math.pi))))) * (
                Decimal(str(Decimal(str(fmax)) * Decimal(str(fmax))))) * (
                         Decimal(str(Decimal(str(t_list_i)) * Decimal(str(t_list_i)))))
            Rickwave_value = (Decimal(str(1)) - Decimal(str(2)) * value1) * Decimal(str(math.exp(-value1)))
            Rickwave_list.append(Rickwave_value)
        return Rickwave_list
    def handle(self):
        dt = self.dt
        t = self.t
        img = cv2.imread("temp.png")
        chang=img.shape[1]
        num=2*t/dt
        dnum=round(chang/num)
        handle_i=[]
        for i in range(0,chang,dnum):
            handle_i.append(i)
        handle_img=img[:,handle_i]
        gray = cv2.cvtColor(handle_img, cv2.COLOR_BGR2GRAY)
        return gray

    def reflectance(self):
        m = self.handle()
        R = self.D
        m = np.array(m)
        [ny, nk] = list(m.shape)
        mm = np.zeros((ny, nk)).tolist()
        vlaue_list = []
        for ny_i1 in range(0, ny):
            for nk_i1 in range(0, nk):
                if m[ny_i1 - 1][nk_i1 - 1] not in vlaue_list:
                    vlaue_list.append(m[ny_i1 - 1][nk_i1 - 1])
        index = 0
        for R_i in range(0, len(vlaue_list)):
            if vlaue_list[R_i] == 255:
                index = 1
            if vlaue_list[R_i] != 255:
                for ny_i in range(0, ny):
                    for nk_i in range(0, nk):
                        if int(m[ny_i - 1][nk_i - 1]) == 255:
                            mm[ny_i - 1][nk_i - 1] = Decimal(str(0))
                        elif int(m[ny_i - 1][nk_i - 1]) == vlaue_list[R_i]:
                            index_R_i = R_i - index
                            mm[ny_i - 1][nk_i - 1] = Decimal(str(1)) * Decimal(str(R[index_R_i - index]))
        return mm
    def convfunc(self):
        Rick = self.Rickwave()
        reflect =self.reflectance()
        reflect = np.array(reflect)
        [nc1, nc2] = list(reflect.shape)
        seisd = []
        for nc2_i in range(0, nc2):
            seisd.append(convolve(Rick, reflect[:, nc2_i]).tolist())
        seisd = np.transpose(seisd).tolist()
        return seisd
    def wigb1(self):
        def get_max_value(martix):
            martix = np.array(martix)
            [ny, nk] = list(martix.shape)
            res_list = []
            for j in range(nk):
                one_list = []
                for i in range(ny):
                    one_list.append(Decimal(str(abs(martix[i][j]))))
                res_list.append(Decimal(str(max(one_list))))
            return res_list
        shit = self.shit
        fig, ax = plt.subplots()
        fig.canvas.set_window_title("合成地震记录")
        [nz, nx] = list(np.array(shit).shape)
        trmx = get_max_value(shit)
        scal = 1
        x = [x for x in range(1, nx + 1)]
        z = [x for x in range(1, nz + 1)]
        amx = np.mean(trmx)
        if nx <= 1:
            return
        list_dx1 = []
        for i in range(len(x) - 1):
            x_1 = x[i + 1]
            x_2 = x[i]
            list_dx1.append(x_1 - x_2)
        list_dx1.sort()
        dx = list_dx1[int(len(list_dx1) / 2)]
        dz = z[1] - z[0]
        xmx = np.max(shit)
        xmn = np.min(shit)
        if scal == 0:
            scal = 1
        shit = np.array(shit)
        if amx == 0:
            shit = shit * 0
        else:
            shit = shit * Decimal(str(dx)) / Decimal(str(amx))
        shit = shit * Decimal(str(scal))
        shit = shit.tolist()
        x1 = min(x) - 2.0 * dx
        x2 = max(x) + 2.0 * dx
        z1 = min(z) - dz
        z2 = max(z) + dz
        z = np.transpose(z).tolist()
        zstart = z[0]
        zend = z[nz - 1]
        for i in range(0, nx):
            if trmx[i] != 0:
                tr = []
                for j in range(nz - 1, -1, -1):
                    tr.append(shit[j][i])
                s = np.sign(tr)
                i1 = []
                trA = []
                trB = []
                for i_1 in range(0, len(s) - 1):
                    if s[i_1 + 1] != s[i_1]:
                        i1.append(i_1)
                        trA.append(tr[i_1])
                        trB.append(tr[i_1 + 1])
                npos = len(i1)

                trA = np.array(trA)
                trB = np.array(trB)
                i1 = np.array(i1)
                zadd = i1 + trA / (trA - trB)
                aadd = np.zeros(len(zadd))
                aadd = aadd.tolist()
                zadd = zadd.tolist()
                zpos_vpos = []
                zpos = []
                tr_ii = -1
                for tr_i in tr:
                    tr_ii = tr_ii + 1
                    if tr_i > 0:
                        zpos_vpos.append([tr_ii, 1])
                        zpos.append(tr_ii)
                iz_not = zpos + zadd
                zz = np.sort(iz_not)  # indices of zero point plus positives 零点加正的指数
                zz_iz = []
                iz = []
                for i_zpos_vpos in zz:
                    zz_iz.append([i_zpos_vpos, iz_not.index(i_zpos_vpos)])
                    iz.append(iz_not.index(i_zpos_vpos))
                tr_zpos = []
                for i_ii in zpos:
                    tr_zpos.append(tr[i_ii])
                aa = tr_zpos + aadd
                aa_iz = []
                for iz_i in iz:
                    aa_iz.append(aa[iz_i])
                if tr[0] > 0 or len(zadd) == 0:
                    a0 = [0]
                    z0 = [1]
                else:
                    a0 = [0]
                    z0 = [zadd[0]]
                if tr[nz - 1] > 0 or len(zadd) == 0:
                    a1 = [0]
                    z1 = [nz - 1]
                else:
                    a1 = [0]
                    z1 = [max(zadd)]
                zz = list(zz)
                zz = z0 + zz + z1 + z0
                aa = a0 + aa_iz + a1 + a0
                zzz = []
                for zzz_i in zz:
                    zzz_value = zstart + zzz_i * dz - dz
                    zzz.append(zzz_value)
                path_list = []
                for xx_i in range(0, len(aa)):
                    path_list.append([x[i] + aa[xx_i], zzz[xx_i]])
                path = Path(path_list)
                patch = PathPatch(path, facecolor='black')
                ax.add_patch(patch)
                tr_xx = []
                tr_yy = []
                for tr_x_i in range(0, len(tr) - 1):
                    tr_xx.append(tr[tr_x_i] + Decimal(str(x[i])))
                    tr_yy.append(Decimal(str(z[tr_x_i])))

                ax.plot([x[i], x[i]], [zstart, zend], 'w')
                ax.plot(tr_xx, tr_yy, 'black')
            else:
                ax.plot([x[i], x[i]], [zstart, zend], 'black')
        plt.show()
    def pro(self):

        self.shit = self.convfunc()
        self.wigb1()