from database.DatabaseManager import DatabaseManager


class DealQualityManager:

    def __init__(self):
        self.db = DatabaseManager()

    def group_cars(self, object_list):
        grouped_list = [[]]
        temp_object = object_list[0]
        index = 0
        for object in object_list:
            if object[1:5] == temp_object[1:5]:
                grouped_list[index].append(object)
            else:
                index += 1
                temp_object = object
                grouped_list.append([])
                grouped_list[index].append(object)

        return grouped_list

    # def dealRating(self, list_cars):
    #     result_km = 0
    #     result_price = 0
    #     summ_km = 0
    #     summ_price = 0
    #
    #     for car in list_cars:
    #         summ_km += car[5]
    #         summ_price += car[6]
    #
    #     average_km = (summ_km / len(list_cars))
    #     average_price = (summ_price / len(list_cars))
    #     print('Average km: ', average_km)
    #     print('Average price: ', average_price)
    #
    #     average_km_degree = average_km / 17
    #     average_price_degree = average_price / 20
    #
    #     for car in list_cars:
    #         id = car[0]
    #         different_km = average_km - car[5]
    #         different_price = average_price - car[6]
    #         try:
    #             result_km = int(different_km / average_km_degree)
    #         except ZeroDivisionError:
    #             result_km = 0
    #         try:
    #             result_price = int(different_price / average_price_degree)
    #         except ZeroDivisionError:
    #             result_price = 0
    #         status = str(result_km + result_price)
    #         self.db.set_deal_quality(status=status, listing_id=id, price_difference=different_price)


    
    def dealRating(self, list_cars):
        result_km = 0
        result_price = 0
        summ_km = 0
        summ_price = 0

        for car in list_cars:
            summ_km += car['kilometres']
            summ_price += car['price']

        average_km = (summ_km / len(list_cars))
        average_price = (summ_price / len(list_cars))
        print('Average km: ', average_km)
        print('Average price: ', average_price)

        average_km_degree = average_km / 17
        average_price_degree = average_price / 20

        for car in list_cars:
            id = car['id']
            different_km = average_km - car['kilometres']
            different_price = average_price - car['price']
            try:
                result_km = int(different_km / average_km_degree)
            except ZeroDivisionError:
                result_km = 0
            try:
                result_price = int(different_price / average_price_degree)
            except ZeroDivisionError:
                result_price = 0
            status = str(result_km + result_price)
            self.db.set_deal_quality(status=status, listing_id=id, price_difference=different_price)






    def main(self, car_list):
        car_list = self.group_cars(car_list)
        for grouped_cars in car_list:
            self.dealRating(list(grouped_cars))


if __name__ == '__main__':
    db = DatabaseManager()
    DQM = DealQualityManager()

    object_list = db.get_grouped_listings()

    DQM.main(object_list)
