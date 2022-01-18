class House :
    merchandise_count = 0
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
        House.merchandise_count += 1

    def show_detail(self):
        print(f"{self.location} {self.house_type} {self.deal_type} {self.price} {self.completion_year}")

    def print_count():
        print(f"총 {House.merchandise_count}개의 매물이 있습니다.")

merchandise1 = House("강남", "아파트", "매매", "10억", "2010년")
merchandise2 = House("마포", "오피스텔", "전세", "5억", "2007년")
merchandise3 = House("송파", "빌라", "월세", "500/50", "2000년")

House.print_count()

merchandise1.show_detail()
merchandise2.show_detail()
merchandise3.show_detail()