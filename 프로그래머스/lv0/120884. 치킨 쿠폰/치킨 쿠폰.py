
def solution(chicken):
    coupon = chicken
    service = 0

    while coupon > 9:
        service += coupon // 10
        coupon = coupon % 10 + coupon // 10 

    return service
