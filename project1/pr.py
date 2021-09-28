from manim import *


import numpy as np


class Svm(Scene):
    def construct(self):
        numberplane = NumberPlane()
        data = np.array([[1,2,1],
                [2,3,1],
                [3,4,1],
                [2,-2,-1],
                [2,-4,-1]])
        for i in data:
            i[2] = 0
            dot = Dot(i)
            self.add(dot)

        self.add(numberplane)
        self.wait(2)

class try_svm(Scene):

    def construct(self):
        numberplane = NumberPlane()
        data = np.array([[1,2,1],
                        [2,3,1],
                        [3,4,1],
                        [2,-2,-1],
                        [2,-4,-1],
                        [7,6,1],
                        [-4,-3,-1]
        ])
        for i in data:
            i[2] = 0
            dot = Dot(i)
            self.add(dot)

        def distance_point_to_hyperplane(pt, w, b):
            return np.abs((pt[0]*w[0]) + (pt[1]*w[1]) +b) / np.sqrt((w[0]*w[0]) + (w[1]*w[1]))

        def svm_test_brute(w, b, x):
            if np.dot(w, x[:-1]) + b > 0:
                return 1
            else:
                return -1

        def compute_margin(data, w, b):
            margin = distance_point_to_hyperplane(data[0, :-1], w, b)
            for pt in data:
                distance = distance_point_to_hyperplane(pt[:-1], w, b)
                if distance < margin:
                    margin = distance_point_to_hyperplane(pt[:-1], w, b)   
                if svm_test_brute(w, b, pt) != pt[2]:
                    return 0 
            return margin    

        def svm_train_brute(training_data):
            training_data = np.asarray(training_data)
            positive = training_data[training_data[:,2] == 1]
            negative = training_data[training_data[:,2] ==-1]
            margin = -99999999
            s_last, w_last, b_last = None, None, None
            list_of_w = []
            list_of_b = []
            for pos in positive:
                for neg in negative:
                    mid_point = (pos[0:2] + neg[0:2]) /2
                    w = np.array(pos[:-1] - neg[:-1])
                    w = w / np.sqrt((w[0] * w[0] + w[1] * w[1]))
                    b = -1 * (w[0] * mid_point[0] + w[1] * mid_point[1])

                    if margin <= compute_margin(training_data, w, b):
                        margin = compute_margin(training_data, w, b)
                        s_last = np.array([pos, neg])
                        w_last = w
                        list_of_w.append(w_last)
                        b_last = b
                        list_of_b.append(b_last)

            return list_of_w, list_of_b

        def line(w_0, w_1, b):
            y = -b / w_1
            x = -b / w_0
            return [[0, y], [x,0]]
            
        x, y = svm_train_brute(data)
        for w in x:
            for b in y:
                m = line(w[0], w[1], b)
                for i in m:
                    dot1 = DOT(i[0])
                    self.add(dot1)
                    l = Line(i[0], i[1])
                    self.add(l)

        self.add(numberplane)
        self.wait(2)

class Svm(Scene):
    def construct(self):
        numberplane = NumberPlane()
        data = np.array([[1,2,1],
                [2,3,1],
                [3,4,1],
                [2,-2,-1],
                [2,-4,-1]])
        for i in data:
            i[2] = 0
            dot = Dot(i)
            self.add(dot)

        self.add(numberplane)
        self.wait(2)

class try_svm3(Scene):

    def construct(self):
        numberplane = NumberPlane()
        data = np.array([[1,2,1],
                        [2,3,1],
                        [3,4,1],
                        [2,-2,-1],
                        [2,-4,-1],
                        [7,6,1],
                        [-4,-3,-1]
        ])
        for i in data:
            i[2] = 0
            dot = Dot(i)
            self.add(dot)

        def distance_point_to_hyperplane(pt, w, b):
            return np.abs((pt[0]*w[0]) + (pt[1]*w[1]) +b) / np.sqrt((w[0]*w[0]) + (w[1]*w[1]))

        def svm_test_brute(w, b, x):
            if np.dot(w, x[:-1]) + b > 0:
                return 1
            else:
                return -1

        def compute_margin(data, w, b):
            margin = distance_point_to_hyperplane(data[0, :-1], w, b)
            for pt in data:
                distance = distance_point_to_hyperplane(pt[:-1], w, b)
                if distance < margin:
                    margin = distance_point_to_hyperplane(pt[:-1], w, b)   
                if svm_test_brute(w, b, pt) != pt[2]:
                    return 0 
            return margin    

        def svm_train_brute(training_data):
            training_data = np.asarray(training_data)
            positive = training_data[training_data[:,2] == 1]
            negative = training_data[training_data[:,2] ==-1]
            margin = -99999999
            s_last, w_last, b_last = None, None, None
            list_of_w = []
            list_of_b = []
            for pos in positive:
                for neg in negative:
                    mid_point = (pos[0:2] + neg[0:2]) /2
                    w = np.array(pos[:-1] - neg[:-1])
                    w = w / np.sqrt((w[0] * w[0] + w[1] * w[1]))
                    b = -1 * (w[0] * mid_point[0] + w[1] * mid_point[1])

                    if margin <= compute_margin(training_data, w, b):
                        margin = compute_margin(training_data, w, b)
                        s_last = np.array([pos, neg])
                        w_last = w
                        list_of_w.append(w_last)
                        b_last = b
                        list_of_b.append(b_last)

            return list_of_w, list_of_b

        def line(w_0, w_1, b):
            y = -b / w_1
            x = -b / w_0
            return [[0, y,0], [x,0,0]]
            
        x, y = svm_train_brute(data)
        for w in x:
            for b in y:
                m = line(w[0], w[1], b)
                for i in m:
                    dot1 = Dot(i[0])
                    dot2 = Dot(i[1])
                    self.add(dot1)
                    l = Line(i[0], i[1])
                    self.play(ShowCreation(l))

        self.add(numberplane)
        self.wait(2)

class try_svm4(Scene):

    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        data = np.array([[1,2,1],
                        [2,3,1],
                        [3,4,1],
                        [2,-2,-1],
                        [2,-4,-1],
                        [7,6,1],
                        [-4,-3,-1]
        ])
        for i in data:
            i[2] = 0
            dot = Dot(i)
            self.add(dot)

        def distance_point_to_hyperplane(pt, w, b):
            return np.abs((pt[0]*w[0]) + (pt[1]*w[1]) +b) / np.sqrt((w[0]*w[0]) + (w[1]*w[1]))

        def svm_test_brute(w, b, x):
            if np.dot(w, x[:-1]) + b > 0:
                return 1
            else:
                return -1

        def compute_margin(data, w, b):
            margin = distance_point_to_hyperplane(data[0, :-1], w, b)
            for pt in data:
                distance = distance_point_to_hyperplane(pt[:-1], w, b)
                if distance < margin:
                    margin = distance_point_to_hyperplane(pt[:-1], w, b)   
                if svm_test_brute(w, b, pt) != pt[2]:
                    return 0 
            return margin    

        def svm_train_brute(training_data):
            training_data = np.asarray(training_data)
            positive = training_data[training_data[:,2] == 1]
            negative = training_data[training_data[:,2] ==-1]
            margin = -99999999
            s_last, w_last, b_last = None, None, None
            list_of_w = []
            list_of_b = []
            for pos in positive:
                for neg in negative:
                    mid_point = (pos[0:2] + neg[0:2]) /2
                    w = np.array(pos[:-1] - neg[:-1])
                    w = w / np.sqrt((w[0] * w[0] + w[1] * w[1]))
                    b = -1 * (w[0] * mid_point[0] + w[1] * mid_point[1])

                    if margin <= compute_margin(training_data, w, b):
                        margin = compute_margin(training_data, w, b)
                        s_last = np.array([pos, neg])
                        w_last = w
                        list_of_w.append(w_last)
                        b_last = b
                        list_of_b.append(b_last)

            return list_of_w, list_of_b

        def line(w_0, w_1, b):
            y = -b / w_1
            x = -b / w_0
            return [[0, y,0], [x,0,0]]
            
        x, y = svm_train_brute(data)
        for w in x:
            for b in y:
                m = line(w[0], w[1], b)
                
                dot1 = Dot(m[0], color='#FFFFFF')
                dot2 = Dot(m[1])
                self.add(dot1)
                l = Line(m[0], m[1])
                self.play(ShowCreation(l))
                self.add(l)


        self.wait(3)

class try_svm5(Scene):

    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        data = np.array([[1,2,1],
                        [2,3,1],
                        [3,4,1],
                        [2,-2,-1],
                        [2,-4,-1],
                        [7,6,1],
                        [-4,-3,-1]
        ])
        for i in data:
            i[2] = 0
            dot = Dot(i)
            self.add(dot)

        def distance_point_to_hyperplane(pt, w, b):
            return np.abs((pt[0]*w[0]) + (pt[1]*w[1]) +b) / np.sqrt((w[0]*w[0]) + (w[1]*w[1]))

        def svm_test_brute(w, b, x):
            if np.dot(w, x[:-1]) + b > 0:
                return 1
            else:
                return -1

        def compute_margin(data, w, b):
            margin = distance_point_to_hyperplane(data[0, :-1], w, b)
            for pt in data:
                distance = distance_point_to_hyperplane(pt[:-1], w, b)
                if distance < margin:
                    margin = distance_point_to_hyperplane(pt[:-1], w, b)   
                if svm_test_brute(w, b, pt) != pt[2]:
                    return 0 
            return margin    

        def svm_train_brute(training_data):
            training_data = np.asarray(training_data)
            positive = training_data[training_data[:,2] == 1]
            negative = training_data[training_data[:,2] ==-1]
            margin = -99999999
            s_last, w_last, b_last = None, None, None
            list_of_w = []
            list_of_b = []
            for pos in positive:
                for neg in negative:
                    mid_point = (pos[0:2] + neg[0:2]) /2
                    w = np.array(pos[:-1] - neg[:-1])
                    w = w / np.sqrt((w[0] * w[0] + w[1] * w[1]))
                    b = -1 * (w[0] * mid_point[0] + w[1] * mid_point[1])

                    if margin <= compute_margin(training_data, w, b):
                        margin = compute_margin(training_data, w, b)
                        s_last = np.array([pos, neg])
                        w_last = w
                        list_of_w.append(w_last)
                        b_last = b
                        list_of_b.append(b_last)

            return list_of_w, list_of_b

        def line(w_0, w_1, b):
            y = -b / w_1
            x = -b / w_0
            return [[0, y,0], [x,0,0]]
            
        x, y = svm_train_brute(data)

        for w in x:
            for b in y:
                m = line(w[0], w[1], b)
                
                dot1 = Dot(m[0], color='#FFFFFF')
                dot2 = Dot(m[1])
                self.add(dot1)
                self.add(dot2)
                l = Line(dot1, dot2)
                self.play(ShowCreation(l))
                self.add(l)


        self.wait(3)


class try_svm6(Scene):

    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        data = np.array([[1,2,1],
                        [2,3,1],
                        [3,4,1],
                        [2,-2,-1],
                        [2,-4,-1],
                        [7,6,1],
                        [-4,-3,-1]
        ])
        for i in data:
            i[2] = 0
            dot = Dot(i)
            self.add(dot)

        def distance_point_to_hyperplane(pt, w, b):
            return np.abs((pt[0]*w[0]) + (pt[1]*w[1]) +b) / np.sqrt((w[0]*w[0]) + (w[1]*w[1]))

        def svm_test_brute(w, b, x):
            if np.dot(w, x[:-1]) + b > 0:
                return 1
            else:
                return -1

        def compute_margin(data, w, b):
            margin = distance_point_to_hyperplane(data[0, :-1], w, b)
            for pt in data:
                distance = distance_point_to_hyperplane(pt[:-1], w, b)
                if distance < margin:
                    margin = distance_point_to_hyperplane(pt[:-1], w, b)   
                if svm_test_brute(w, b, pt) != pt[2]:
                    return 0 
            return margin    

        def svm_train_brute(training_data):
            training_data = np.asarray(training_data)
            positive = training_data[training_data[:,2] == 1]
            negative = training_data[training_data[:,2] ==-1]
            margin = -99999999
            s_last, w_last, b_last = None, None, None
            list_of_w = []
            list_of_b = []
            for pos in positive:
                for neg in negative:
                    mid_point = (pos[0:2] + neg[0:2]) /2
                    w = np.array(pos[:-1] - neg[:-1])
                    w = w / np.sqrt((w[0] * w[0] + w[1] * w[1]))
                    b = -1 * (w[0] * mid_point[0] + w[1] * mid_point[1])

                    if margin <= compute_margin(training_data, w, b):
                        margin = compute_margin(training_data, w, b)
                        s_last = np.array([pos, neg])
                        w_last = w
                        list_of_w.append(w_last)
                        b_last = b
                        list_of_b.append(b_last)

            return list_of_w, list_of_b

        def line(w_0, w_1, b):
            y = -b / w_1
            x = -b / w_0
            return [[0, y,0], [x,0,0]]
            
        x, y = svm_train_brute(data)

        for w in x:
            for b in y:
                m = line(w[0], w[1], b)
                
                dot1 = Dot(m[0], color='#FFFFFF')
                dot2 = Dot(m[1])
                self.add(dot1)
                self.add(dot2)
                l = Line(dot1, dot2)
                #self.play(ShowCreation(l))
                self.add(l)


        self.wait(3)
