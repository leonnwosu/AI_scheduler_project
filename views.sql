CREATE VIEW getuser AS
SELECT User.*
FROM User;

CREATE view getallevents AS
SELECT events.*
FROM events
JOIN User on User.user_id = events.user_id;

CREATE view getsingleevents AS
SELECT events.*
From events
Join User on User.user_id = events.user_id;

-- CREATE view adduser AS
-- INSERT into User(user_name, password_hash, email)

-- create view
