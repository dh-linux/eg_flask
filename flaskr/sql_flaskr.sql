drop table if exists entries;
create table entries (
  id int(5) not null primary key auto_increment,
  title varchar(255) not null,
  text text not null
);
