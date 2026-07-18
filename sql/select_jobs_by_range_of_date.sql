select
    r.job_id,
    r.job_name,
    r.run_id,
    r.started_cdmx,
    r.ended_cdmx,
    r.duration,
    r.run_type,
    r.result_state,
    r.termination_code,
    r.workspace_id,
    r.process_id,
    r.subprocess_id,
    r.stage_id,
    r.substage_id,
    r.username,
    r.folio_number,
    r.parameter_source
from
    public.runs r
where
    r.started_cdmx >= %(start_date)s
    and r.started_cdmx <= %(end_date)s
order by
    r.started_cdmx desc;