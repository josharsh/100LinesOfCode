import requests
from bs4 import BeautifulSoup


def get_attribute_data(soup, attribute):
    attribute_data = []
    if attribute == "class":
        all_classes = soup.find_all(class_=True)
        if all_classes:
            print("Available class names:")
            class_names = list(set().union(*(element["class"] for element in all_classes)))
            for i in range(len(class_names)):
                print(f"{i + 1}. {class_names[i]}")
            class_input = input("Enter the number or name of the class you want to check: ")
            selected_class = list(all_classes)[int(class_input) - 1] if class_input.isdigit() else class_input
            classes = soup.find_all(class_=selected_class)
            if classes:
                for i in range(len(classes)):
                    print(f"{i + 1}. {classes[i]}")
                    for descendant in classes[i].find_all(["div", "p"]):
                        print(f"\t - {descendant.text.strip()}")
            else:
                print(f"Sorry, there are no elements with the class '{selected_class}'.")
        else:
            print("Sorry, there are no class names available.")
    elif attribute == "id":
        all_ids = [element.get("id") for element in soup.find_all(id=True)]
        if all_ids:
            print("Available IDs:")
            for i in range(len(all_ids)):
                print(f"{i + 1}. {all_ids[i]}")
            id_input = input("Enter the number or name of the ID you want to check: ")
            selected_id = all_ids[int(id_input) - 1] if id_input.isdigit() else id_input
            ids = soup.find_all(id=selected_id)
            if ids:
                for i in range(len(ids)):
                    print(f"{i + 1}. {ids[i]}")
                    for descendant in ids[i].find_all(["div", "p"]):
                        print(f"\t - {descendant.text.strip()}")
            else:
                print(f"Sorry, there are no elements with the ID '{selected_id}'.")
        else:
            print("Sorry, there are no IDs available.")
    elif attribute == "img":
        img_elements = soup.find_all("img")
        for img in img_elements:
            src = img.get("src")
            if src:
                attribute_data.append(src)
        print(attribute_data)
        if not attribute_data:
            print("Sorry, no image links available")
    elif attribute == "a":
        a_elements = soup.find_all("a")
        for a in a_elements:
            link = a.get("href")
            if link:
                attribute_data.append(link)
        print(attribute_data)
        print(f"There are {len(attribute_data)} href(s) in total.")
    elif attribute == "src":
        src_elements = soup.find_all(src=True)
        for element in src_elements:
            src = element.get("src")
            if src:
                attribute_data.append(src)
        print(attribute_data)
        print(f"There are {len(attribute_data)} src attribute(s) in total.")
    else:
        attr = soup.find_all(attribute)
        if attr:
            for ele in attr:
                attribute_data.append(ele.getText())
            print(attribute_data)
            print(f"There are {len(attribute_data)} {attribute}(s) in total.")
        else:
            print(f"Sorry, there are no {attribute} in the HTML.")


def main():
    website_url = input("Please enter the website URL: ")
    attribute = input("Which attribute do you want to check? (Please mention "
                      "'id' or 'class' as input if you want to check for an id or "
                      "a class): ").lower()

    response = requests.get(url=website_url)
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    get_attribute_data(soup, attribute)


if __name__ == "__main__":
    main()