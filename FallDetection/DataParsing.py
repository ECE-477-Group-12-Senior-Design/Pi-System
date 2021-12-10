"""
Givens:
Text file with lines of 14 bytes of data in the format:
(T -> Temp, G -> Gyro, A -> Acceleration, L -> Low, H -> High)
T[L] T[H] G_X[L] G_X[H] G_Y[L] G_Y[H] G_Z[L] G_Z[H] A_X[L] A_X[H] A_Y[L] A_Y[H] A_Z[L] A_Z[H]

Acceleration is set at +/- 4g (can be changed if necessary)
"""

import numpy as np
import matplotlib.pyplot as plt


# generates np array for easy parsing
def generate_array(lines):
    total = []
    for line in lines:
        tmp = []

        # convert hexstrings to decimal
        for word in line.split(' '):
            tmp.append(int('0x' + word, 16))

        total.append(tmp)

    print(np.array(total))
    return np.array(total)


# returns parsed data, needs LSB then MSB
def parse_data(lsb, msb):
    res = []
    for i in range(len(lsb)):
        val = (int(hex(msb[i] * 16 * 16 + lsb[i]), 16))

        # handling 2s complements
        if val > 32766:
            res.append((np.invert(np.array(val, dtype=np.uint16)) + 1) * -1)
        else:
            res.append(val)

    return res


# returns a tuple (x, y, z) of lists of the parsed acceleration data
def acceleration_data(total_np):
    ax1 = total_np[:, 8]
    ax2 = total_np[:, 9]
    ay1 = total_np[:, 10]
    ay2 = total_np[:, 11]
    az1 = total_np[:, 12]
    az2 = total_np[:, 13]
    x = parse_data(ax1, ax2)
    y = parse_data(ay1, ay2)
    z = parse_data(az1, az2)
    return x, y, z


def plot_data(res, png_name):
    plt.figure(1)
    plt.scatter(range(len(res)), res)
    plt.savefig(png_name)


def detect_junk(spaced_str):
    if spaced_str.count('0a') > 3:
        # print("A GLITCH")
        return 1
    elif spaced_str.count('0b') > 3:
        # print("B GLITCH")
        return 1
    elif spaced_str.count('0a') == 2:
        # print("NO GLITCH")
        return 0
    elif spaced_str.count('0b') == 2:
        return 0
    else:
        return 1


def detect_battery(spaced_str):
    if spaced_str.count('0c') == 8 and spaced_str.count('0b') == 10:
        return 1
    else:
        return 0


def notify_battery(spaced_str):



if __name__ == '__main__':
    lines = read_file('for_charles_e_cheese.txt')
    total_np = generate_array(lines)
    all_axes = acceleration_data(total_np)

    plot_data(all_axes[0], 'x_accel.png')
    plot_data(all_axes[1], 'y_accel.png')
    plot_data(all_axes[2], 'z_accel.png')
