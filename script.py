
import matplotlib.pyplot as plt
import sys


class Point():
   # scale in units/mm
    x_scale = 0.1
    y_scale = 0.1

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_prev, self.x_line = self.location(x, self.x_scale)
        self.y_prev, self.y_line = self.location(y, self.y_scale)

    def __str__(self):
        return ('(' + str(self.x) + ',' + str(self.y) + ')')

    def __repr__(self):
        return ('(' + str(self.x) + ',' + str(self.y) + ')')

    @classmethod
    def set_scales(self, x_scale_in, y_scale_in):
        self.x_scale = x_scale_in
        self.y_scale = y_scale_in

    def location(self, c, scale):
        temp = c
        prev = 0
        while temp >= 10 * scale:
            temp = temp - 10 * scale

        prev = c - temp
        line = temp / scale
        return prev, int(round(line))


class Pointset():
    def __init__(self, point_list):
        self.n = len(point_list)
        self.point_list = []
        self.x_list = []
        self.y_list = []
        # self.y_new_list = []
        for element in point_list:
            temp_element = point_parse(element)
            self.point_list.append(temp_element)

        for point in self.point_list:
            self.x_list.append(point.x)
            self.y_list.append(point.y)

    def __str__(self):
        # return self.point_list
        pass

    def __repr__(self):
        # return self.point_list
        pass

    @property
    def points_mean(self):
        tot_x = 0
        tot_y = 0
        for temp_point in self.point_list:
            tot_x += temp_point.x
            tot_y += temp_point.y

        return Point(tot_x / len(self.point_list), tot_y / len(self.point_list))
        # self.mean_x = tot_x / len(self.point_list)
        # self.mean_y = tot_y / len(self.point_list)

    @property
    def sum_squared(self):
        tot = 0
        for temp_point in self.point_list:
            tot += temp_point.x * temp_point.x

        return tot

    @property
    def sum_prod(self):
        tot = 0
        for temp_point in self.point_list:
            tot += temp_point.x * temp_point.y
        return tot

    @property
    def calc_m(self):
        return (self.sum_prod - self.n * self.points_mean.x * self.points_mean.y) / (self.sum_squared - self.n * self.points_mean.x * self.points_mean.x)

    @property
    def calc_c(self):
        return (self.points_mean.y * self.sum_squared - self.points_mean.x * self.sum_prod) / (self.sum_squared - self.n * self.points_mean.x * self.points_mean.x)

    @property
    def y_new_list(self):
        new_list = []
        for x in self.x_list:
            new_list.append(x * self.calc_m + self.calc_c)

        return new_list

   # (x,y)


def point_parse(a):
    temp = a
    temp = temp[1:-1]
    temp_x, temp_y = temp.split(',')
    try:
        return Point(int(temp_x), int(temp_y))

    except:
        return Point(float(temp_x), float(temp_y))


def test():

    # a = sys.argv[1:]
    a = ['(1,1)', '(2.2,3.7)', '(3.6,5.9)', '(4.3,7.2)']
    points = Pointset(a)
    line = 'y = ({}) x + ({})'.format(round(points.calc_m, 3), round(points.calc_c, 3))
    plt.plot(points.x_list, points.y_new_list, label=line, color='red')
    plt.scatter(points.x_list, points.y_new_list, s=100, color='red')
    plt.scatter(points.x_list, points.y_list, s=100)
    plt.legend()

    plt.show()


# test()

def main():
    a = sys.argv[1:]
    points = Pointset(a)
    line = 'y = ({}) x + ({})'.format(round(points.calc_m, 3), round(points.calc_c, 3))
    plt.plot(points.x_list, points.y_new_list, label=line, color='red')
    plt.scatter(points.x_list, points.y_new_list, s=100, color='red')
    plt.scatter(points.x_list, points.y_list, s=100)
    plt.legend()
    plt.show()


main()
