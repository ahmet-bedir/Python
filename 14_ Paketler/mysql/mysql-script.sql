----------------------------------------------------
----- sudo mysql -u root -p < mysql-script.sql -----
----------------------------------------------------

-- Veritabanını oluştur
CREATE DATABASE IF NOT EXISTS storedb;
USE storedb;

-- Tabloları oluştur
CREATE TABLE categories (
    category_id INT UNSIGNED AUTO_INCREMENT,
    category_name VARCHAR(30),
    PRIMARY KEY (category_id)
) ENGINE=InnoDB;

CREATE TABLE products (
    product_id INT UNSIGNED AUTO_INCREMENT,
    product_name VARCHAR(30) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    product_image VARCHAR(30),
    description TEXT,
    registration_date DATE DEFAULT (CURRENT_DATE),
    categoryid INT UNSIGNED,
    PRIMARY KEY (product_id),
    CONSTRAINT products_categories_fk
        FOREIGN KEY (categoryid)
        REFERENCES categories(category_id)
) ENGINE=InnoDB;

-- Kategoriler tablosuna veri girişi
INSERT INTO categories (category_name) VALUES
('Bilgisayarlar'),
('Çevre Birimleri'),
('Depolama'),
('Mobil Cihazlar'),
('Ses Sistemleri'),
('Kamera ve Yayın'),
('Oyuncu Ekipmanları'),
('Ofis Ürünleri'),
('Ağ Ürünleri'),
('Görüntü Sistemleri');

-- Ürünler tablosuna veri girişi
INSERT INTO products
(product_name, price, product_image,
description, registration_date, categoryid)
VALUES
('Laptop', 34999.99, 'laptop.jpg', '16 GB RAM', '2026-01-15', 1),
('Mekanik Klavye', 2499.90, 'klavye.jpg', 'RGB', '2026-01-18', 2),
('Kablosuz Mouse', 899.50, 'mouse.jpg', 'Ergonomik', '2026-01-20', 2),
('27 Inch Monitör', 7999.00, 'monitor.jpg', '2K IPS', '2026-01-22', 1),
('USB Bellek', 349.90, 'usb.jpg', '64GB', '2026-01-25', 3);

-- Kullanıcı (SAFE)
DROP USER IF EXISTS 'user1'@'localhost';
CREATE USER 'user1'@'localhost' IDENTIFIED BY 'u1';
-- Kullanıcıya tam yetki ver
GRANT ALL PRIVILEGES ON storedb.* TO 'user1'@'localhost';

-- Kullanıcıları listele
SELECT user, host FROM mysql.user;

-- 
SELECT * FROM products;
SELECT * FROM categories;

FLUSH PRIVILEGES;
