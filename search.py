#library to display Vietnamese
import codecs
import numpy as np

allRestaurants = []
with codecs.open('restaurants.txt', "r", encoding="utf-16") as f:
    lines = f.read().splitlines()
    for line in lines:
        line = line.split("|")
        try:
            rate = float(line[1])
        except:
            rate = round(np.random.uniform(5.0, 9.0), 1)
        line[1] = rate
        allRestaurants.append(line)

def containsKeywords(restaurantName, keywordList):
    return any([tmp.lower() in restaurantName.lower() for tmp in keywordList])

def topRestaurantByKeyWords(keywordList, limit=20):
    restaurants = [tmp for tmp in allRestaurants if containsKeywords(tmp[0], keywordList)]
    restaurants.sort(reverse=True, key=lambda x:x[1])
    return restaurants[:limit]

def generate_random_coordination():
    longitude, latitude = 21.018 + np.random.uniform(-0.035, 0.035), 105.835 + np.random.uniform(-0.035, 0.035)
    return longitude, latitude

image_urls = [f'https://aiwre-s3.s3-ap-southeast-1.amazonaws.com/spcloud/restaurant-img/{tmp}.jpg' for tmp in range(531) if tmp not in [37, 46, 81, 95, 211, 408, 434, 460, 469]]

def random_images():
    return np.random.choice(image_urls, 2)

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
    
    restaurantList = topRestaurantByKeyWords(keywordList)
    restaurantList = [{"name": tmp[0], "rate": tmp[1], "address": tmp[2], "coordination": generate_random_coordination(), "images": random_images()} for tmp in restaurantList]
    
    return restaurantList

if __name__ == "__main__":
    result = findRestaurant("pizza")
    print(result)



