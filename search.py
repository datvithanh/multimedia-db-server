#library to display Vietnamese
import codecs

#search for top 5 restaurants (by rating) serving food related to the keyword list
def searchTopFiveRestaurant(keywordList):
    restaurantList = []
    with codecs.open('restaurants.txt', "r", encoding="utf-16") as f:
        lines = f.read().splitlines()
        for line in lines:
            line = line.split("|")
            lowerRestaurantName = line[0].lower()
            for keyword in keywordList:
                if keyword.lower() in lowerRestaurantName:
                    restaurantList.append(line)
                    break
    for restaurant in restaurantList:
        if (restaurant[1] == "_._"):
            restaurant[1] = "0.0"
    restaurantList.sort(reverse=True, key=lambda x:x[1])
    topFiveRestaurantList = restaurantList[:5]

    #returned result format: ['restaurant_name', 'rating', 'address']
    return (topFiveRestaurantList)

#specify the keyword list based on the input category and call the search function
def findRestaurant(category):
    if (category == "banh_cuon"):
        keywordList = ["Bánh cuốn"]
    elif (category == "banh_mi"):
        keywordList = ["Bánh mì", "Bami"]
    elif (category == "birthcake"):
        keywordList = ["Bánh ngọt", "Gato", "Bakery", "Bánh sinh nhật", "Pâtisserie"]
    elif (category == "caramen"):
        keywordList = ["Caramen", "Caramel"]
    elif (category == "che"):
        keywordList = ["Chè"]
    elif (category == "milktea"):
        keywordList = ["Trà sữa", "Milk tea", "Milktea", "Boba"]
    elif (category == "noodles"):
        keywordList = ["Phở", "Mì tôm", "Mì trộn", "Vằn thắn", "Mì gà", "Mì bò", "Mì tim", "Bún", "Miến", "Hủ tiếu"]
    elif (category == "pizza"):
        keywordList = ["Pizza", "Pasta"]
    elif (category == "roll"):
        keywordList = ["Nem", "Roll", "Bánh xèo", "Bánh tráng"]
    elif (category == "xoi"):
        keywordList = ["Xôi"]
    else:
        keywordList = []
    restaurantList = searchTopFiveRestaurant(keywordList)
    return restaurantList

result = findRestaurant("pizza")
print(result)



