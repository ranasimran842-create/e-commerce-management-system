from database import *


create_table()


def add_product():

    name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    price = int(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))


    conn = connect_db()
    cursor = conn.cursor()


    cursor.execute(
        "INSERT INTO products(name,category,price,quantity) VALUES(?,?,?,?)",
        (name, category, price, quantity)
    )


    conn.commit()
    conn.close()

    print("Product Added Successfully")


def view_products():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")

    data = cursor.fetchall()

    conn.close()


    if not data:
        print("No Products Found")

    for product in data:

        print("------------------")
        print("ID:", product[0])
        print("Name:", product[1])
        print("Category:", product[2])
        print("Price:", product[3])
        print("Quantity:", product[4])


def update_product():

    pid = int(input("Enter Product ID: "))
    price = int(input("Enter New Price: "))
    quantity = int(input("Enter New Quantity: "))


    conn = connect_db()
    cursor = conn.cursor()


    cursor.execute(
        "UPDATE products SET price=?, quantity=? WHERE id=?",
        (price, quantity, pid)
    )


    conn.commit()
    conn.close()

    print("Product Updated Successfully")



def delete_product():

    pid = int(input("Enter Product ID: "))


    conn = connect_db()
    cursor = conn.cursor()


    cursor.execute(
        "DELETE FROM products WHERE id=?",
        (pid,)
    )


    conn.commit()
    conn.close()

    print("Product Deleted Successfully")



while True:

    print("\n====== E-COMMERCE MANAGEMENT SYSTEM ======")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")


    choice = input("Enter your choice: ")


    try:

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            update_product()

        elif choice == "4":
            delete_product()

        elif choice == "5":
            print("Thank You")
            break

        else:
            print("Invalid Choice")


    except ValueError:

        print("Please enter valid number")