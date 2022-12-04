from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        # 创建用处存储图中点之间关系的dict{v: [u, i]}(v,u,i都是点,表示边<v, u>, <v, i>)：边集合
        self.graph = defaultdict(list)# 默认值 []
        self.V = vertices# 存储图中点的个数
        
    # 添加边
    def add_edge(self, u, v):
        # 添加边<u, v>
        self.graph[u].append(v)
        #{5：[2,0],4:[0,1],2:[3],3:[1]}
        
    # 获取一个存储图中所有点的状态:dict{key: Boolean}  
    def set_keys_station(self):
        keyStation = {}
        key = list(self.graph.keys())# [5,4,2,3]
        # 因为有些点，没有出边，所以在key中找不到，需要对图遍历找出没有出边的点
        if len(key) < self.V:
            for i in key:
                for j in self.graph[i]:
                    if j not in key:
                        key.append(j)
        for ele in key:
            keyStation[ele] = False
        # 初始时全为False ,dict{key: False}
        return keyStation#{5：False, 4：False, 2：False, 3：False, 0：False, 1：False,}
    
    # 拓扑排序
    def topological_sort(self):
        queue = []# 拓扑序列
        station = self.set_keys_station()# 点状态字典,状态初始化全部为False
        
        # 由于最坏情况下每一次循环都只能排序一个点，所以需要循环（点的个数）次
        for i in range(self.V):
            # 循环点状态字典，elem：点
            # 第一遍循环完queue= [5, 4, 2，3，0，1]
            # 所以没有独立点（既没有入边也没有出边）只需循环一次即可得到结果
            for elem in station:
                # 这里如果是已经排序好的点就不进行排序操作了
                # 第一次循环完 station={5：True, 4：False, 2：False, 3：False, 0：False, 1：False,}
                if not station[elem]:
                    self.topological_sort_util(elem, queue, station)
            if len(queue)== self.V: break
        return queue
    
    # 对于点进行排序
    def topological_sort_util(self, elem, queue, station):
        # 设置点的状态为True，表示已经排序完成
        station[elem] = True
        
        # 状态为True的点，相当于排序完成，这个点的边集合不需要扫描
        # (i=0)ele = 0, station[5]=True 跳过点5,station[1] = True
        # (i=0)ele = 0, station[4]=True 跳过点4，station[1] = True
        # (i=0)ele = 1, station[4]=True 跳过点4,station[1] = True
        # (i=0)ele = 1, station[3]=True 跳过点3，station[1] = True
        for i in station:
            # 循环查看该点是否有入边，如果存在入边，修改状态为False
            # 3 in graph[2]  ，
            if elem in self.graph[i] and not station[i]:
                station[elem] = False
                
        # 如果没有入边(排除了queue中的点（排序完成的点）)，排序成功，添加到拓扑序列中
        if station[elem]:# 此处如果多个点都没有入边，则根据添加边时的顺序排序，即同为没有入边的点顺序可以调换
            queue.append(elem)


if __name__ == '__main__':
    g = Graph(6)
    g.add_edge(5, 2); 
    g.add_edge(5, 0); 
    g.add_edge(4, 0); 
    g.add_edge(4, 1); 
    g.add_edge(2, 3); 
    g.add_edge(3, 1); 

    print("拓扑排序结果：")
    print(g.topological_sort())
