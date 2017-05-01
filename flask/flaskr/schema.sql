drop table if exists salas;
create table salas (
  id integer primary key autoincrement,
  sala text not null,
  'status' text not null
);
