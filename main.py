import csv

def load_data(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)

def save_data(filename, data):
    with open(filename, 'w', newline='') as f:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def update_grocery_data(source_data, new_data):
    # Create a dictionary for quick lookup based on SKU
    source_dict = {item['SKU']: item for item in source_data}

    for item in new_data:
        sku = item['SKU']
        if sku in source_dict:
            # Item already exists, update quantity
            source_dict[sku]['Quantity'] = str(int(source_dict[sku]['Quantity']) + int(item['Quantity']))
        else:
            # Item does not exist, add it to the source_data
            source_data.append(item)

    return source_data

def main():
    # Load the initial grocery data from sample_grocery.csv
    source_data = load_data('sample_grocery.csv')

    # Load the new batch of grocery data from grocery_batch_1.csv
    new_data = load_data('grocery_batch_1.csv')

    # Update the source_data with new_data
    updated_data = update_grocery_data(source_data, new_data)

    # Save the final grocery data to grocery_db.csv
    save_data('grocery_db.csv', updated_data)

if __name__ == '__main__':
    main
