#1
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

class Statistics:
    def __init__(self, data):
        self.data = data
    def count(self): 
        ret = 0
        for item in self.data: ret+=1
        return ret
    def sum(self):
        ret = 0 
        for item in self.data: ret+=item
        return ret
    def min(self):
        min = 255
        for item in self.data: 
            if item < min: min = item
        return min
    def max(self):
        max = -256
        for item in self.data:
            if item > max: max = item
        return max
    def range(self):
        return self.max()-self.min()
    def mean(self):
        return float(self.sum()/self.count())
    def median(self):
        return sorted(self.data)[int(self.count()/2)]
    def mode(self):
        ret = dict()
        for item in self.data:
            if item in ret: ret[item] += 1
            else: ret[item] = 1
        return sorted(ret.items(), key=lambda item: item[1], reverse=True)[0]
    def std(self):
        return self.var()**0.5
    def var(self):
        ret = 0
        for item in self.data:
            ret += (item - self.mean())**2
        return (ret / self.count())
    def freq_dist(self):
        ret = dict()
        for item in self.data:
            if item in ret: ret[item] += 1
            else: ret[item] = 1
        for key, value in ret.items():
            ret[key] = (value/self.count())*100
        return sorted(ret.items(), key=lambda item: item[1], reverse=True)

data = Statistics(ages)
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

#2

class PersonAccount():
    def __init__(self):
        pass
#The basics