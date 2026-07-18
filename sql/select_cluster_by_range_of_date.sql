SELECT
    w.start_time_cdmx,
    w.total_instances,
    w.drivers,
    w.workers
FROM public.workers w
WHERE w.start_time_cdmx >= %(start_date)s
    and w.start_time_cdmx <= %(end_date)s
