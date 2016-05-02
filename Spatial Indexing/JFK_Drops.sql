alter table taxidata_init modify p_point POINT NOT NULL;
alter table taxidata_init modify d_point POINT NOT NULL;

create spatial index p_taxidata_coords on taxidata_init(p_point);
create spatial index d_taxidata_coords on taxidata_init(d_point);