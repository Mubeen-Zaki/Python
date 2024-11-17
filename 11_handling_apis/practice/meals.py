import requests

def getmeals(dish):
    url = f"https://api.freeapi.app/api/v1/public/meals?page=1&limit=10&query={dish}"
    response = requests.get(url)
    obj = response.json()
    if obj['success'] and 'data' in obj.keys():
        data = obj['data']
        result = []
        for i in range(int(data['totalItems'])):
            object = {}
            object['category'] = data['data'][i]['strCategory']
            object['region'] = data['data'][i]['strArea']
            object['dishname'] = data['data'][i]['strMeal']
            ingredients_list = [data['data'][i][x] for x in data['data'][i] if 'strIngredient' in x and data['data'][i][x]]
            measure_list =  [data['data'][i][x] for x in data['data'][i] if 'strMeasure' in x and data['data'][i][x]]
            object['ingredients'] = {key : value for key in ingredients_list for value in measure_list}
            object['instructions'] = data['data'][i]['strInstructions']
            object['yt_link'] = data['data'][i]['strYoutube']
            result.append(object)
        return result

def pretty_print(data):
    counter = 1
    for obj in data:
        print(f"****** Dish Number : {counter} ******")
        print(f"\n Category : {obj['category']}\n")
        print(f" Region : {obj['region']}\n")
        print(f" Dish Name : {obj['dishname']}\n")
        print(f" Ingredients with quantity : {obj['ingredients']}\n")
        print(f" Instructions : {obj['instructions']}\n")
        print(f" Youtube : {obj['yt_link']}\n")
        counter += 1
        print("*" * 100)

def main():
    while True:
        print("\n ****** Welcome to Recipe Generator Application : ****** \n")
        dish = input("Enter dish name : ").strip().lower()
        try:
            results = getmeals(dish)
            print("*" * 100)
            pretty_print(results)
        except Exception as e:
            print(str(e))
        flag = 0
        while True:
            choice = input("Do you want to exit?(Y/N)").strip().lower()
            if choice == 'y':
                flag = 1
                break
            elif choice == 'n':
                break
            else:
                print("Invalid response")
        if flag == 1:
            break
            

if __name__ == "__main__":
    main()