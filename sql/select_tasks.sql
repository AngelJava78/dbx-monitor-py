select t.task_run_id,
       t.run_id,
       t.task_key,
       t.started_cdmx,
       t.ended_cdmx,
       to_char(t.duration, 'HH24:MI:SS') as duration,
       t.task_type,
       t.run_page_url,
       t.status,
       t.notebook_name,
       t.process_id,
       t.subprocess_id,
       t.stage_id,
       t.substage_id,
       t.username,
       t.folio_number,
       t.parameter_source
  from public.tasks t
  where t.run_id = %(run_id)s
