# Arduino map()
# long map(long x, long in_min, long in_max, long out_min, long out_max) {
#   return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
# }

def mymap(x, in_min, in_max, out_min, out_max):
    result = (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    return result