coffee=0

def coffee_machine(button):
    print()
    print("#1. (자동으로) 뜨거운 물을 준비한다.")
    print("#2. (자동으로) 종이컵을 준비한다.")

    if coffee==1:
        print("#3. (자동으로) 아메리카노를 탄다.")
    elif coffee==2:
        print("#3. (자동으로) 카페라떼를 탄다.")
    elif coffee==3:
        print("#3. (자동으로) 카푸치노를 탄다.")
    elif coffee==4:
        print("#3. (자동으로) 에스프레소를 탄다.")
    else:
        print("#3. (자동으로) 아무거나 탄다.")
    
    print("#4. 뜨거운 물을 붓는다.")
    print("#5. 스푼으로 젓는다.")

    print()

coffee=int(input("로제님, 어떤 커피 드릴까요?(1:아메리카노,2:카페라떼,3:카푸치노,4:에스프레소)"))
coffee_machine(coffee)
print("로제님~ 커피 여기 있습니다.")

coffee=int(input("리사님, 어떤 커피 드릴까요?(1:아메리카노,2:카페라떼,3:카푸치노,4:에스프레소)"))
coffee_machine(coffee)
print("리사님~ 커피 여기 있습니다.")

coffee=int(input("지수님, 어떤 커피 드릴까요?(1:아메리카노,2:카페라떼,3:카푸치노,4:에스프레소)"))
coffee_machine(coffee)
print("지수님~ 커피 여기 있습니다.")

coffee=int(input("제니님, 어떤 커피 드릴까요?(1:아메리카노,2:카페라떼,3:카푸치노,4:에스프레소)"))
coffee_machine(coffee)
print("제니님~ 커피 여기 있습니다.")