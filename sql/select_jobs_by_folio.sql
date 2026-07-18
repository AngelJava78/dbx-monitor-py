select
	r.run_id,
	r.job_id,
	r.job_name,
	r.started_cdmx,
	r.ended_cdmx,
	r.duration,
	r.result_state,
	r.process_id,
	r.subprocess_id,
	sp.subprocess_name,
	r.stage_id,
	r.substage_id,
	ss.substage_name,
	r.username,
	r.folio_number
from
	public.runs r
left join public.subprocesses sp
    on
	r.subprocess_id = sp.subprocess_id
left join public.substages ss
    on
	r.substage_id = ss.substage_id
where 
	cast(r.folio_number as text) ilike %(folio_number)s
order by
	started_cdmx;    
