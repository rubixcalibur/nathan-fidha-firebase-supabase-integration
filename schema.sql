-- Run this script in the Supabase SQL Editor.
create table if not exists public.iris_flowers (
    id integer primary key,
    sepal_length double precision not null,
    sepal_width double precision not null,
    petal_length double precision not null,
    petal_width double precision not null,
    target integer not null check (target between 0 and 2),
    species text not null
);

-- This table is intended for writes from the trusted Python script.
-- Keep Row Level Security enabled for application-facing access.
alter table public.iris_flowers enable row level security;
