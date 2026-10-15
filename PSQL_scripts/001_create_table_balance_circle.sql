--колесо баланса по неделям (1 - на неделе было что-то хорошее в категории, 0 - не было)
CREATE TABLE public.balance_circle(
   ID serial primary key,
   user_id               INTEGER NOT NULL,
   year_balance          INTEGER NOT NULL,
   week_balance          INTEGER NOT NULL,
   date_update           TIMESTAMP,
   balance_work          INTEGER DEFAULT 0,
   balance_family        INTEGER DEFAULT 0,
   balance_health        INTEGER DEFAULT 0,
   balance_hobby         INTEGER DEFAULT 0,
   balance_rest          INTEGER DEFAULT 0,
   balance_improvement   INTEGER DEFAULT 0
);
CREATE INDEX ON public.balance_circle (user_id);
