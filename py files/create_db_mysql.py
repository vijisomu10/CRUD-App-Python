#All database queries for user and user_login
create_table_user = """CREATE TABLE IF NOT EXISTS user(
                            user_id INT(11) AUTO_INCREMENT,
                            first_name VARCHAR(50) NOT NULL,
                            last_name VARCHAR(50) NOT NULL,
                            street_name_address VARCHAR(50) NOT NULL,
                            city_address VARCHAR(50) NOT NULL,
                            country_address VARCHAR(50) NOT NULL,
                            postal_code_address INT NOT NULL,
                            mobile_number INT(15) NOT NULL,
                            PRIMARY KEY(user_id),
                            UNIQUE KEY(user_id)
                            );"""

create_table_user_login = """CREATE TABLE IF NOT EXISTS user_login(
                                    user_login_id INT(11) AUTO_INCREMENT NOT NULL,
                                    user_reg_id INT NOT NULL,
                                    user_name VARCHAR(50) NOT NULL,
                                    password VARCHAR(50) NOT NULL,        
                                    PRIMARY KEY(user_login_id),
                                    FOREIGN KEY(user_reg_id) REFERENCES user(user_id) 
                                    );"""

insert_user = """INSERT INTO user(first_name, last_name, street_name_address, city_address,
                        country_address, postal_code_address, mobile_number) 
                        VALUES 
                        (%s, %s, %s, %s, %s, %s, %s);"""

insert_user_login = """INSERT INTO user_login
                            (user_name, password, user_reg_id) 
                            VALUES 
                            (%s, %s, LAST_INSERT_ID());"""

select_table_user = """SELECT * FROM user"""

select_table_user_login = """SELECT * FROM user_login """  

query_retrieve_user = "SELECT user_reg_id FROM user_login WHERE user_name = %s AND password = %s"

query_retrieve_userLogin = "SELECT user_login_id FROM user_login WHERE user_name = %s AND password = %s"

update_FN = """UPDATE user SET first_name = %s WHERE user_id = %s"""
update_LN = """UPDATE user SET last_name = %s WHERE user_id = %s"""
update_street = """UPDATE user SET street_name_address = %s WHERE user_id = %s"""
update_city = """UPDATE user SET city_address = %s WHERE user_id = %s"""
update_country = """UPDATE user SET country_address = %s WHERE user_id = %s"""
update_postalcode = """UPDATE user SET postal_code_address = %s WHERE user_id = %s"""
update_mobile = """UPDATE user SET mobile_number = %s WHERE user_id = %s"""

update_password = """UPDATE user_login SET password = %s WHERE user_login_id = %s"""
