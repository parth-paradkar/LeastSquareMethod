import matplotlib.pyplot as plt


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
        self.point_list = []
        for element in point_list:
            temp_element = point_parse(element)
            self.point_list.append(temp_element)

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
    def points_squared(self):
        tot_x = 0
        tot_y = 0
        for temp_point in self.point_list:
            tot_x += temp_point.x * temp_point.x
            tot_y += temp_point.y * temp_point.y

        return Point(tot_x / len(self.point_list), tot_y / len(self.point_list))
        # self.mean_squared_x = tot_x / len(self.point_list)
        # self.mean_squared_y = tot_y / len(self.point_list)

    @property
    def sum_of_prod(self):
        tot = 0
        for temp_point in self.point_list:
            tot += temp_point.x * temp_point.y
        return tot
# (x,y)


def point_parse(a):
    temp = a
    temp = temp[1:4]
    temp_x, temp_y = temp.split(',')
    return Point(int(temp_x), int(temp_y))


def main():

    # a = sys.argv[1:]
    a = ['(1,2)', '(2,3)', '(3,4)', '(4,5)']
    points = Pointset(a)
    # b = points.points_mean()
    # print(b)
    # print(points.point_list)
    print(points.points_mean)
    print(points.points_squared)
    print(points.sum_of_prod)


main()
