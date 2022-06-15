import matplotlib.pyplot as plt
import math
import random

def generate_cities(size):
    return [(int(random.random() * 1000), int(random.random() * 1000)) for _ in range(size)]

class Graph:
    def __init__(self, cities):
        self.unvisited = cities[1:]
        self.route = [cities[0]]
    
    
    def run(self, plot):
        if plot:
            plt.ion()
            plt.show(block=False)
            self.init_plot()
        
        nearest_loc = float('inf')   
        while len(self.unvisited):
            cost= {}
            dist_list = []
            current_index = self.route[-1]
                     
            for i in self.unvisited:                    
                
                #distance = ((i[0] - current_index[0])**2 + (i[1] - current_index[1])**2)**0.5                
                distance = math.hypot(current_index[0]- i[0], current_index[1]-i[1])
                cost[i] = distance
                    
               
                if distance < nearest_loc:
                    nearest_loc = distance
                    nearest_city = i   
            temp = []
            key_list = list(cost.keys())
            value_list = list(cost.values())
            for values in cost:
                temp.append(cost[values])
            if temp:
                nearest_city = key_list[value_list.index(min(temp))]        
                
            # index, nearest_city = min(enumerate(self.unvisited),
            #                           key=lambda item: item[1].distance(self.route[-1]))            
            self.route.append(nearest_city)
            self.unvisited.remove(nearest_city)
            self.Ciz(False)        
        self.route.append(self.route[0])
        self.Ciz(False)
        self.route.pop()
        
    def Ciz(self, block):
        x1, y1, x2, y2 = self.route[-2][0], self.route[-2][1], self.route[-1][0], self.route[-1][1]
        plt.plot([x1, x2], [y1, y2],'ro',markersize=10)
        plt.plot([x1, x2], [y1, y2],'yellow')
        plt.axis('off')
        plt.pause(0.2)
        plt.draw()
        
        plt.show(block=block)

    def init_plot(self):
        
        fig = plt.figure(0)
        
        fig.suptitle('Algoritmik Gider Düşürücü')
        fig.set_figwidth(300)
        fig.set_figheight(300)
        x_list, y_list = [], []
        for city in [*self.route, *self.unvisited]:
            x_list.append(city[0])
            y_list.append(city[1])
        x_list.append(self.route[0][0])
        y_list.append(self.route[0][1])
        
        plt.plot(x_list, y_list, 'ro',color = "purple",markersize=10)
        plt.axis('off')
        plt.show(block=False)
while True:
    cities = generate_cities(48)
    graph = Graph(cities)

    print(graph.run(plot=True))
    print(graph.route)
    plt.show(block=True)    

