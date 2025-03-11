/*CREATE TABLE user(
    user_id int not null AUTO_INCREMENT,
    user_name varchar(255) not NULL unique,
    password_hash varchar(255) not null unique,
    email varchar(255) not NULL,
    primary key (user_id)
);

CREATE TABLE schedule(
    schedule_id int not null AUTO_INCREMENT,
    user_id int not null,
    date_created datetime not null,
    calender_name varchar(255) not null,
    original_url varchar(2083) not null,
    modified_url varchar(2083) not null,
    primary key(schedule_id),
    foreign key (user_id) references user(user_id)

);

CREATE table events(
    event_id int not null AUTO_INCREMENT,
    schedule_id int not null,
    event_type ENUM('Original','AI-added','User-added') not null,
    event_title varchar(255),
    start_date_time datetime not null,
    end_date_time datetime not null,
    event_description varchar(2083) not null,
    primary key (event_id),
    foreign key (schedule_id) references schedule(schedule_id)

);*/

ALTER table user AUTO_INCREMENT=1;

insert into user(user_name,password_hash,email)
values("leon", "Nwosu", "leonanwosua@gmail.com");