class Product:
    # 1. კლასის ატრიბუტები
    store_name = "TechShop Georgia"
    currency = "GEL"
    total_products = 0

    # 2. კონსტრუქტორი (__init__)
    def __init__(self, name, price, stock, category, discount=0):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
        self.discount = discount
        
        # ყოველი ახალი პროდუქტის შექმნისას ვზრდით total_products-ს 1-ით
        Product.total_products += 1

    # 3. ინსტანსის მეთოდები
    def get_info(self):
        """აბრუნებს სტრიქონს პროდუქტის სრული ინფორმაციით"""
        return (f"პროდუქტი: {self.name} | კატეგორია: {self.category} | "
                f"ფასი: {self.price} {Product.currency} | მარაგი: {self.stock} ცალი | "
                f"ფასდაკლება: {self.discount}%")

    def apply_discount(self, percent):
        """ცვლის პროდუქტის ფასდაკლების მნიშვნელობას"""
        self.discount = percent
        print(f"[{self.name}] ფასდაკლება განახლდა: {self.discount}%")

    def update_stock(self, amount):
        """ამატებს ან აკლებს პროდუქტს მარაგს"""
        self.stock += amount
        if self.stock < 0:
            print(f"გაფრთხილება: [{self.name}] მარაგი ჩამოვიდა 0-ზე ქვემოთ! (მიმდინარე: {self.stock})")
        else:
            print(f"[{self.name}] მარაგი შეიცვალა. მიმდინარე მარაგი: {self.stock}")

    def calculate_final_price(self):
        """ითვლის და აბრუნებს საბოლოო ფასს ფასდაკლების გათვალისწინებით"""
        final_price = self.price - (self.price * self.discount / 100)
        return final_price

    # 4. კლასის მეთოდი
    @classmethod
    def get_total_products_count(cls):
        """აბრუნებს მაღაზიაში არსებული პროდუქტების საერთო რაოდენობას"""
        return cls.total_products


# --- ტესტირება (მაგალითი) ---
if __name__ == "__main__":
    # შევქმნათ 3 განსხვავებული პროდუქტი
    p1 = Product("Smartphone X", 1200, 15, "Electronics")
    p2 = Product("Wireless Headphones", 250, 30, "Electronics", discount=10)
    p3 = Product("Running Shoes", 180, 8, "Sportswear")

    # მეთოდების გამოცდა
    print(p1.get_info())
    p1.apply_discount(15)
    print(f"საბოლოო ფასი ფასდაკლებით: {p1.calculate_final_price()} {Product.currency}\n")

    p3.update_stock(5)   # მარაგის გაზრდა
    p3.update_stock(-2)  # მარაგის შემცირება (გაყიდვა)
    print()

    # კლასის მეთოდის გამოძახება
    print(f"სულ შექმნილი პროდუქტები: {Product.get_total_products_count()}")