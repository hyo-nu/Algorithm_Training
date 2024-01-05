import math

def solution(fees, records):
    
    def calcul(time):
        fee = fees[1] 
        if time > fees[0]:
            fee += math.ceil( (time - fees[0]) / fees[2] ) * fees[3]
        return fee
    
    car_info, car_fee = {}, {}
    for record in records:
        time, number, status = record.split(" ")
        hour,minute = map(int,time.split(":"))
        
        if status == "IN":
            car_info[number] = car_info.get(number,hour * 60 + minute)
            
        elif status == "OUT":
            total_time = hour * 60 + minute - car_info[number]
            car_fee[number] = car_fee.get(number, 0) + total_time
            car_info.pop(number)
    
    if car_info:
        for key, value in car_info.items():
            total_time = 23 * 60 + 59 - value
            car_fee[key] = car_fee.get(key, 0) + total_time
    
    result = []
    for key , value in (sorted(car_fee.items())):
        result.append(calcul(value))
    
    return result